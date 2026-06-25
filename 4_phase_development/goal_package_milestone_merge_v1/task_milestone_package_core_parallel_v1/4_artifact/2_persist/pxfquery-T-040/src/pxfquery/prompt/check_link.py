import os
import anndata as ad
import scanpy as sc
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import re 
import time
 
from openai import OpenAI
import json



def check_link(client, model, timeout_s=20, print_result=True):
    """
    Health check for given client + model.

    - Uses a tiny English prompt.
    - Expects the model to return "OK" (allowing punctuation/whitespace variations).
    - Returns a standardized dict result.
    """
    t0 = time.monotonic()

    result = {
        "ok": False,
        "model": model,
        "reply": None,
        "latency_ms": None,
        "error_type": None,
        "error_message": None,
    }

    # Basic validation (keep it simple)
    if client is None:
        result["error_type"] = "ValueError"
        result["error_message"] = "client is None"
        if print_result:
            print(json.dumps(result, ensure_ascii=False))
        return result

    if not model or not isinstance(model, str):
        result["error_type"] = "ValueError"
        result["error_message"] = "model must be a non-empty string"
        if print_result:
            print(json.dumps(result, ensure_ascii=False))
        return result

    try:
        # Minimal English prompt for a deterministic check
        messages = [
            {"role": "system", "content": "You are a connectivity test bot. Follow instructions exactly."},
            {"role": "user", "content": "Reply with exactly: OK"},
        ]

        # Note: 修正了你原代码里 model=model 后少逗号的问题
        resp = client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=0,
            max_tokens=5,
            # 如果你用的 SDK 支持 timeout，可打开下面这行；不支持就删掉也没事
            # timeout=timeout_s,
        )

        content = (resp.choices[0].message.content or "").strip()
        result["reply"] = content

        # Normalize: allow "OK", "OK.", "OK!" etc.
        normalized = re.sub(r"[^A-Za-z]", "", content).upper()  # "OK." -> "OK"
        result["ok"] = (normalized == "OK")

    except Exception as e:
        result["error_type"] = type(e).__name__
        result["error_message"] = str(e)

    finally:
        result["latency_ms"] = int((time.monotonic() - t0) * 1000)

    if print_result:
        print(json.dumps(result, ensure_ascii=False))

    return result