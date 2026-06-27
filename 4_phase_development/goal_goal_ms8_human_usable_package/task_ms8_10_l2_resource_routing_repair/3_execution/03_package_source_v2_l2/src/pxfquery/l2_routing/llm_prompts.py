"""
prompts.py — Prompt functions for resolver workflow.

All prompts are in English by design.
"""

from __future__ import annotations

import json
import re
import time
from typing import Any, Optional


def llm_parse_intent(client, model: str, user_input: str) -> dict[str, Any]:
    schema = {
        "query_type": "forward|reverse",
        "bio_context": "cell line or disease context, or null",
        "pert_desc": "gene/drug description for forward queries, else null",
        "pert_class": "genetic|drug|null",
        "function_desc": "functional goal text for reverse queries, else null",
        "activate": ["list of function phrases"],
        "suppress": ["list of function phrases"],
        "top_n": "integer or null",
    }
    system_prompt = (
        "You are an intent parser for a perturbation-function query toolkit.\n"
        "Return JSON only.\n"
        f"Schema: {json.dumps(schema, ensure_ascii=True)}\n"
        "Rules:\n"
        "- query_type=forward when user asks what a perturbation does.\n"
        "- query_type=reverse when user asks which perturbations can achieve a function goal.\n"
        "- pert_class=genetic for genes/knockdown/knockout/overexpression.\n"
        "- pert_class=drug for compounds/inhibitors/drug names.\n"
        "- Keep activate/suppress as short phrases if present.\n"
        "- Use null for unknown fields."
    )
    payload = _chat_json(
        client,
        model,
        system_prompt,
        user_input,
        max_tokens=220,
        use_reasoning=False,
    )
    return {
        "query_type": payload.get("query_type"),
        "bio_context": payload.get("bio_context"),
        "pert_desc": payload.get("pert_desc"),
        "pert_class": payload.get("pert_class"),
        "function_desc": payload.get("function_desc"),
        "activate": payload.get("activate") or [],
        "suppress": payload.get("suppress") or [],
        "top_n": payload.get("top_n"),
    }


def llm_map_cell_line(
    client,
    model: str,
    bio_desc: str,
    options: list[str],
    level_name: str,
) -> str:
    system_prompt = (
        "You are selecting one option from a controlled list.\n"
        "Return JSON only with key 'selected'.\n"
        "Pick exactly one option from the list."
    )
    user_prompt = (
        f"Biology context: {bio_desc}\n"
        f"Current level: {level_name}\n"
        f"Options: {options}\n"
        "Select the single best option."
    )
    payload = _chat_json(
        client,
        model,
        system_prompt,
        user_prompt,
        max_tokens=80,
        use_reasoning=False,
    )
    selected = str(payload.get("selected", "")).strip()
    if selected in options:
        return selected
    selected_l = selected.lower()
    for opt in options:
        if opt.lower() == selected_l:
            return opt
    for opt in options:
        if selected_l in opt.lower() or opt.lower() in selected_l:
            return opt
    return options[0]


def llm_map_gene(
    client,
    model: str,
    gene_desc: str,
    gene_candidates: Optional[list[str]] = None,
) -> list[str]:
    candidates_txt = ", ".join(gene_candidates[:200]) if gene_candidates else "(not provided)"
    system_prompt = (
        "Normalize user gene mention to canonical gene symbols.\n"
        "Return JSON only with key 'candidates', a list of likely canonical symbols."
    )
    user_prompt = (
        f"Input mention: {gene_desc}\n"
        f"Candidate symbols reference (optional): {candidates_txt}\n"
        "Return up to 5 likely canonical symbols."
    )
    payload = _chat_json(
        client,
        model,
        system_prompt,
        user_prompt,
        max_tokens=100,
        use_reasoning=False,
    )
    out = payload.get("candidates") or []
    return _normalize_str_list(out, max_items=5)


def llm_map_drug(client, model: str, drug_desc: str) -> list[str]:
    system_prompt = (
        "Map a drug description to candidate concrete drug names.\n"
        "Return JSON only with key 'candidates' as a list."
    )
    user_prompt = f"Drug description: {drug_desc}\nReturn up to 8 candidate drug names."
    payload = _chat_json(
        client,
        model,
        system_prompt,
        user_prompt,
        max_tokens=120,
        use_reasoning=False,
    )
    return _normalize_str_list(payload.get("candidates") or [], max_items=8)


def llm_normalize_drug(client, model: str, drug_name: str) -> list[str]:
    system_prompt = (
        "Normalize a drug synonym/brand/translated name into standard generic names.\n"
        "Return JSON only with key 'candidates' as a list."
    )
    user_prompt = f"Input drug name: {drug_name}\nReturn up to 5 normalized generic names."
    payload = _chat_json(
        client,
        model,
        system_prompt,
        user_prompt,
        max_tokens=100,
        use_reasoning=False,
    )
    return _normalize_str_list(payload.get("candidates") or [], max_items=5)


def llm_map_function(
    client,
    model: str,
    function_desc: str,
    function_list_str: str,
    max_items: int = 3,
) -> list[str]:
    system_prompt = (
        "Select exact var_name values from a fixed function list.\n"
        "Return JSON only with key 'var_names'.\n"
        "Do not invent names outside the list."
    )
    user_prompt = (
        f"Target description: {function_desc}\n"
        "Function list:\n"
        f"{function_list_str}\n"
        f"Return up to {max_items} exact var_name values."
    )
    payload = _chat_json(
        client,
        model,
        system_prompt,
        user_prompt,
        max_tokens=120,
        use_reasoning=False,
    )
    return _normalize_str_list(payload.get("var_names") or [], max_items=max_items)


def llm_summarize_forward(
    client,
    model: str,
    result,
    max_words: int = 180,
    include_numbers: bool = False,
) -> str:
    if not getattr(result, "found", False):
        return f"No result found. {getattr(result, 'note', '')}".strip()
    if include_numbers:
        activated = "\n".join(
            f"- {k}: {v:.3f}" for k, v in result.top_activated.head(10).items()
        )
        suppressed = "\n".join(
            f"- {k}: {v:.3f}" for k, v in result.top_suppressed.head(10).items()
        )
    else:
        activated = "\n".join(f"- {k}" for k in result.top_activated.head(10).index)
        suppressed = "\n".join(f"- {k}" for k in result.top_suppressed.head(10).index)
    resolver_meta = getattr(result, "resolver_meta", {})
    prompt = (
        "Write a concise scientific interpretation.\n"
        "Do NOT repeat raw table style output.\n"
        f"Summarize in <= {max_words} words.\n"
        f"Perturbation: {result.perturbation}\n"
        f"Cell line: {result.cell_line}\n"
        f"Evidence meta: {json.dumps(resolver_meta, ensure_ascii=True)}\n"
        f"Top activated:\n{activated}\n"
        f"Top suppressed:\n{suppressed}\n"
        "State whether this is exact evidence or proxy-based evidence."
    )
    text = _chat_text(client, model, prompt, max_tokens=320, use_reasoning=True)
    if text.strip():
        return text
    raise RuntimeError("LLM forward summary returned empty content")


def llm_summarize_reverse(
    client,
    model: str,
    result,
    max_words: int = 180,
    include_numbers: bool = False,
) -> str:
    if not getattr(result, "found", False):
        return f"No result found. {getattr(result, 'note', '')}".strip()
    top_df = result.candidates_df.head(5)
    rows = []
    for _, row in top_df.iterrows():
        if include_numbers:
            rows.append(
                f"- {row['cmap_name']} @ {row['cell_iname']}, sim={row['similarity']:.3f}, drivers={row['driving_terms']}"
            )
        else:
            rows.append(
                f"- {row['cmap_name']} @ {row['cell_iname']}, drivers={row['driving_terms']}"
            )
    resolver_meta = getattr(result, "resolver_meta", {})
    prompt = (
        f"Summarize in <= {max_words} words.\n"
        f"Activate targets: {result.activate}\n"
        f"Suppress targets: {result.suppress}\n"
        f"Cell line: {result.cell_line}\n"
        f"Evidence meta: {json.dumps(resolver_meta, ensure_ascii=True)}\n"
        "Top candidates:\n"
        + "\n".join(rows)
        + "\nUse scientific language and explicitly mention evidence quality."
    )
    text = _chat_text(client, model, prompt, max_tokens=320, use_reasoning=True)
    if text.strip():
        return text
    raise RuntimeError("LLM reverse summary returned empty content")


def _chat_json(
    client,
    model: str,
    system_prompt: str,
    user_prompt: str,
    *,
    max_tokens: int = 220,
    use_reasoning: bool = False,
) -> dict[str, Any]:
    text = _chat_text(
        client,
        model,
        user_prompt,
        system_prompt=system_prompt,
        max_tokens=max_tokens,
        use_reasoning=use_reasoning,
    )
    parsed = _safe_json_load(text)
    if isinstance(parsed, dict):
        return parsed
    raise ValueError(f"LLM response was not a JSON object: {text[:300]}")


def _chat_text(
    client,
    model: str,
    user_prompt: str,
    system_prompt: Optional[str] = None,
    *,
    max_tokens: int = 220,
    use_reasoning: bool = False,
) -> str:
    messages = []
    if system_prompt:
        messages.append({"role": "system", "content": system_prompt})
    messages.append({"role": "user", "content": user_prompt})
    kwargs = {
        "model": model,
        "messages": messages,
        "temperature": 0,
        "max_tokens": int(max_tokens),
    }
    if use_reasoning and str(model).startswith("MiniMax-"):
        kwargs["extra_body"] = {"reasoning_split": True}
    last_err: Exception | None = None
    for i in range(3):
        try:
            resp = client.chat.completions.create(**kwargs)
            text = (resp.choices[0].message.content or "").strip()
            text = re.sub(r"<think>.*?</think>", "", text, flags=re.DOTALL | re.IGNORECASE).strip()
            return text
        except Exception as e:  # pragma: no cover - network/provider transient failures
            last_err = e
            if i < 2:
                time.sleep(0.6 * (i + 1))
                continue
            break
    if last_err is not None:
        raise last_err
    return ""


def _safe_json_load(text: str) -> Any:
    if not text:
        raise ValueError("LLM returned empty content")
    clean = re.sub(r"^\s*```(?:json)?\s*", "", text, flags=re.IGNORECASE)
    clean = re.sub(r"\s*```\s*$", "", clean)
    try:
        return json.loads(clean)
    except Exception:
        pass
    m = re.search(r"\{.*\}", clean, flags=re.DOTALL)
    if m:
        try:
            return json.loads(m.group(0))
        except Exception:
            pass
    raise ValueError(f"Could not parse JSON from LLM response: {text[:300]}")


def _normalize_str_list(values: list[Any], max_items: int) -> list[str]:
    out: list[str] = []
    for v in values:
        s = str(v).strip()
        if not s:
            continue
        if s not in out:
            out.append(s)
        if len(out) >= max_items:
            break
    return out

