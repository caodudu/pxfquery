import json
import unittest

import yaml

from pxfquery.route import (
    CellLineSource,
    Confidence,
    Diagnostics,
    Direction,
    EvidenceRouteResponse,
    FunctionResponse,
    FunctionStatus,
    PerturbationResolution,
    PerturbationType,
    ProxyDimension,
    ProxyStep,
    QueryContext,
    ResolutionMethod,
    RouteType,
    SimilarityUnit,
    SourceIndex,
    Suggestion,
    SuggestionType,
    LlmMode,
    FuzzyCandidateBlocked,
    NearTieInfo,
    RankedCandidate,
    ScoreVector,
    THRESHOLD_CELL_LINE,
    THRESHOLD_DRUG_TANIMOTO,
    THRESHOLD_GENE_COSINE,
    STANDARD_MATRICES,
    STANDARD_INDEXES,
    STANDARD_METADATA_TABLES,
    EXPECTED_FUNCTION_TERM_COUNT,
    build_route_response,
    response_to_dict,
    response_to_json,
    response_to_yaml,
)


class RouteContractTests(unittest.TestCase):
    def context(self):
        return QueryContext(
            cell_line="A549",
            cell_line_source=CellLineSource.EXACT,
            tissue_lineage="lung",
            disease="NSCLC",
            perturbation_type=PerturbationType.COMPOUND,
            direction=Direction.FORWARD,
        )

    def resolution(self):
        return PerturbationResolution(
            method=ResolutionMethod.EXACT_MATCH,
            resolved_name="gefitinib",
            resolved_id="BRD-K68045993",
            original_query="gefitinib",
            source_index=SourceIndex.DRUG_INDEX,
            perturbation_type=PerturbationType.COMPOUND,
        )

    def suggestion(self):
        return Suggestion(
            type=SuggestionType.MISSING_FIELD,
            text="Provide a cell line.",
            required_field="cell_line",
            examples=["A549"],
        )

    # --- Enum value tests ---

    def test_all_route_type_values_match_contract(self):
        expected = {"exact-hit", "proxy-hit", "no-hit", "ambiguous-hit", "context-missing", "transfer/suggestion"}
        self.assertEqual({r.value for r in RouteType}, expected)

    def test_all_confidence_values_match_contract(self):
        self.assertEqual({c.value for c in Confidence}, {"high", "medium", "low", "n/a"})

    def test_all_perturbation_type_values_match_contract(self):
        expected = {"compound", "shRNA", "orf_overexpression", "gene", "unknown", "unresolved"}
        self.assertEqual({p.value for p in PerturbationType}, expected)

    def test_direction_values_match_contract(self):
        self.assertEqual({d.value for d in Direction}, {"forward", "reverse"})

    def test_cell_line_source_values_match_contract(self):
        self.assertEqual({c.value for c in CellLineSource}, {"exact", "proxy", "unresolved"})

    def test_resolution_method_values_match_contract(self):
        expected = {"exact_match", "proxy_neighbor", "ambiguous", "unmatched", "not_applicable"}
        self.assertEqual({r.value for r in ResolutionMethod}, expected)

    def test_function_status_values_match_contract(self):
        expected = {"OK", "NO_HIT", "NO_RETRIEVAL", "AMBIGUOUS", "NO_RANKING"}
        self.assertEqual({f.value for f in FunctionStatus}, expected)

    def test_suggestion_type_values_match_contract(self):
        expected = {"reformulated_query", "related_perturbation", "alternative_context", "disambiguation", "missing_field", "llm_explanation", "diagnostic"}
        self.assertEqual({s.value for s in SuggestionType}, expected)

    def test_proxy_dimension_values_match_contract(self):
        self.assertEqual({p.value for p in ProxyDimension}, {"perturbation", "cell_line"})

    def test_similarity_unit_values_match_contract(self):
        self.assertEqual({s.value for s in SimilarityUnit}, {"Tanimoto", "cosine", "lineage"})

    def test_llm_mode_values_match_contract(self):
        self.assertEqual({l.value for l in LlmMode}, {"enabled", "disabled"})

    def test_source_index_values_match_contract(self):
        expected = {"drug_index.json", "gene_index.json", "gene_index_simple.json", "drug_neighbors.json", "gene_neighbors.json", "gene_neighbors_simple.json", "null"}
        self.assertEqual({s.value for s in SourceIndex}, expected)

    # --- Threshold constant tests ---

    def test_threshold_constants_match_contract(self):
        self.assertEqual(THRESHOLD_DRUG_TANIMOTO, 0.40)
        self.assertEqual(THRESHOLD_GENE_COSINE, 0.50)
        self.assertEqual(THRESHOLD_CELL_LINE, "same_lineage_disease_subtype")

    def test_standard_resources_match_t021(self):
        self.assertEqual(STANDARD_MATRICES, ("cp_func_ad.h5ad", "sh_func_ad.h5ad", "xpr_func_ad.h5ad"))
        self.assertEqual(STANDARD_INDEXES, (
            "cellline_index.json", "cellline_neighbors.json", "cellline_tree.json",
            "drug_index.json", "drug_neighbors.json",
            "gene_index.json", "gene_index_simple.json",
            "gene_neighbors.json", "gene_neighbors_simple.json",
            "function_index.json",
        ))
        self.assertEqual(STANDARD_METADATA_TABLES, ("cellline_meta_standard.csv", "compound_meta_standard.csv", "gene_info_standard.csv"))
        self.assertEqual(EXPECTED_FUNCTION_TERM_COUNT, 91)

    # --- Dataclass construction and defaults ---

    def test_evidence_route_response_has_exactly_eight_fields(self):
        response = EvidenceRouteResponse()
        self.assertEqual(
            list(response_to_dict(response).keys()),
            [
                "route_type",
                "query_context",
                "perturbation_resolution",
                "function_response",
                "confidence",
                "proxy_chain",
                "diagnostics",
                "suggestions",
            ],
        )

    def test_evidence_route_response_all_fields_optional(self):
        response = EvidenceRouteResponse()
        self.assertIsNone(response.route_type)
        self.assertIsNone(response.query_context)
        self.assertIsNone(response.perturbation_resolution)
        self.assertIsNone(response.function_response)
        self.assertIsNone(response.confidence)
        self.assertEqual(response.proxy_chain, [])
        self.assertIsNone(response.diagnostics)
        self.assertEqual(response.suggestions, [])

    def test_query_context_defaults(self):
        ctx = QueryContext()
        self.assertIsNone(ctx.cell_line)
        self.assertIsNone(ctx.cell_line_source)
        self.assertIsNone(ctx.tissue_lineage)
        self.assertIsNone(ctx.disease)
        self.assertIsNone(ctx.subtype)
        self.assertIsNone(ctx.perturbation_type)
        self.assertIsNone(ctx.direction)
        self.assertIsNone(ctx.normalization_state)

    def test_perturbation_resolution_defaults(self):
        pr = PerturbationResolution()
        self.assertEqual(pr.method, ResolutionMethod.NOT_APPLICABLE)

    def test_function_response_defaults(self):
        fr = FunctionResponse()
        self.assertEqual(fr.status, FunctionStatus.NO_RETRIEVAL)

    def test_diagnostics_defaults(self):
        d = Diagnostics()
        self.assertIsNone(d.warnings)
        self.assertIsNone(d.missing_fields)
        self.assertIsNone(d.indexes_searched)

    def test_suggestion_defaults(self):
        s = Suggestion()
        self.assertIsNone(s.type)
        self.assertIsNone(s.text)

    def test_proxy_step_from_field_works(self):
        step = ProxyStep(dimension=ProxyDimension.PERTURBATION, from_="imatinib", to="dasatinib")
        self.assertEqual(step.from_, "imatinib")
        self.assertEqual(step.to, "dasatinib")

    def test_ranked_candidate_construction(self):
        rc = RankedCandidate(pert_id="BRD-123", cmap_name="drug_x", score=1.5, rank=1)
        self.assertEqual(rc.pert_id, "BRD-123")
        self.assertEqual(rc.rank, 1)

    def test_score_vector_type_alias(self):
        sv: ScoreVector = {"HALLMARK_APOPTOSIS": 1.234, "HALLMARK_ADIPOGENESIS": -0.567}
        self.assertEqual(len(sv), 2)

    def test_fuzzy_candidate_blocked_construction(self):
        fcb = FuzzyCandidateBlocked(candidate="ZZZ3", reason="similarity below threshold", threshold_applied="cosine >= 0.50")
        self.assertEqual(fcb.candidate, "ZZZ3")

    def test_near_tie_info_construction(self):
        nti = NearTieInfo(score_difference=0.003, top_candidates=[RankedCandidate(pert_id="A", score=1.0, rank=1)])
        self.assertEqual(nti.score_difference, 0.003)

    # --- Build_route_response for all six route types ---

    def test_exact_hit_defaults_match_contract(self):
        response = build_route_response(
            RouteType.EXACT_HIT,
            query_context=self.context(),
            perturbation_resolution=self.resolution(),
        )
        payload = response_to_dict(response)
        self.assertEqual(payload["route_type"], "exact-hit")
        self.assertEqual(payload["confidence"], "high")
        self.assertEqual(payload["function_response"]["status"], "OK")
        self.assertEqual(payload["proxy_chain"], [])
        self.assertEqual(payload["suggestions"], [])

    def test_proxy_hit_requires_and_serializes_proxy_chain(self):
        with self.assertRaisesRegex(ValueError, "proxy_chain"):
            build_route_response(RouteType.PROXY_HIT, query_context=self.context())

        response = build_route_response(
            RouteType.PROXY_HIT,
            query_context=self.context(),
            proxy_chain=[
                ProxyStep(
                    dimension=ProxyDimension.PERTURBATION,
                    from_="imatinib",
                    to="dasatinib",
                    via="drug_neighbors.json Tanimoto neighbor",
                    similarity=0.78,
                    similarity_unit=SimilarityUnit.TANIMOTO,
                    threshold_applied=THRESHOLD_DRUG_TANIMOTO,
                )
            ],
            diagnostics=Diagnostics(warnings=["perturbation_proxy_used"]),
        )
        payload = response_to_dict(response)
        self.assertEqual(payload["confidence"], "medium")
        self.assertEqual(payload["proxy_chain"][0]["from"], "imatinib")
        self.assertNotIn("from_", payload["proxy_chain"][0])

    def test_proxy_hit_defaults(self):
        response = build_route_response(
            RouteType.PROXY_HIT,
            query_context=self.context(),
            proxy_chain=[
                ProxyStep(
                    dimension=ProxyDimension.CELL_LINE,
                    from_="NCI-H226",
                    to="A549",
                    via="lung/NSCLC/adenocarcinoma",
                )
            ],
        )
        payload = response_to_dict(response)
        self.assertEqual(payload["route_type"], "proxy-hit")
        self.assertEqual(payload["confidence"], "medium")
        self.assertEqual(payload["function_response"]["status"], "OK")

    def test_no_hit_defaults_match_contract(self):
        with self.assertRaisesRegex(ValueError, "cell_line"):
            build_route_response(RouteType.NO_HIT)

        response = build_route_response(
            RouteType.NO_HIT,
            query_context=self.context(),
            perturbation_resolution=PerturbationResolution(
                method=ResolutionMethod.UNMATCHED,
                original_query="ZZZ-FAKE-GENE-XYZ",
                source_index=SourceIndex.GENE_INDEX,
                perturbation_type=PerturbationType.GENE,
            ),
        )
        payload = response_to_dict(response)
        self.assertEqual(payload["route_type"], "no-hit")
        self.assertEqual(payload["confidence"], "high")
        self.assertEqual(payload["function_response"]["status"], "NO_HIT")
        self.assertEqual(payload["proxy_chain"], [])

    def test_ambiguous_hit_defaults_match_contract(self):
        with self.assertRaisesRegex(ValueError, "cell_line"):
            build_route_response(RouteType.AMBIGUOUS_HIT)

        response = build_route_response(
            RouteType.AMBIGUOUS_HIT,
            query_context=self.context(),
            perturbation_resolution=PerturbationResolution(
                method=ResolutionMethod.AMBIGUOUS,
                original_query="ACT",
                source_index=SourceIndex.GENE_INDEX,
                perturbation_type=PerturbationType.GENE,
            ),
            diagnostics=Diagnostics(
                ambiguous_perturbation=True,
                candidates=["ACTA1", "ACTB", "ACTG1"],
                candidate_count=3,
            ),
        )
        payload = response_to_dict(response)
        self.assertEqual(payload["route_type"], "ambiguous-hit")
        self.assertEqual(payload["confidence"], "low")
        self.assertEqual(payload["function_response"]["status"], "AMBIGUOUS")
        self.assertEqual(payload["proxy_chain"], [])

    def test_context_missing_requires_diagnostics_and_suggestion(self):
        with self.assertRaisesRegex(ValueError, "diagnostics"):
            build_route_response(RouteType.CONTEXT_MISSING)

        response = build_route_response(
            RouteType.CONTEXT_MISSING,
            diagnostics=Diagnostics(missing_fields=["cell_line"]),
            suggestions=[self.suggestion()],
        )
        payload = response_to_dict(response)
        self.assertEqual(payload["confidence"], "n/a")
        self.assertEqual(payload["function_response"]["status"], "NO_RETRIEVAL")
        self.assertEqual(payload["diagnostics"]["missing_fields"], ["cell_line"])

    def test_context_missing_with_invalid_fields(self):
        response = build_route_response(
            RouteType.CONTEXT_MISSING,
            diagnostics=Diagnostics(
                invalid_fields=[{"field": "cell_line", "value": "ZZZ-INVALID", "reason": "not found"}],
            ),
            suggestions=[self.suggestion()],
        )
        payload = response_to_dict(response)
        self.assertEqual(payload["confidence"], "n/a")
        self.assertEqual(payload["diagnostics"]["invalid_fields"][0]["field"], "cell_line")

    def test_transfer_suggestion_requires_suggestion_payload(self):
        with self.assertRaisesRegex(ValueError, "suggestion"):
            build_route_response(RouteType.TRANSFER_SUGGESTION, query_context=self.context())

        response = build_route_response(
            RouteType.TRANSFER_SUGGESTION,
            query_context=self.context(),
            suggestions=[Suggestion(type=SuggestionType.RELATED_PERTURBATION, text="Try erlotinib.")],
        )
        self.assertEqual(response_to_dict(response)["route_type"], "transfer/suggestion")

    def test_transfer_suggestion_defaults(self):
        response = build_route_response(
            RouteType.TRANSFER_SUGGESTION,
            query_context=self.context(),
            suggestions=[
                Suggestion(type=SuggestionType.REFORMULATED_QUERY, text="Try gefitinib in A549"),
            ],
        )
        payload = response_to_dict(response)
        self.assertEqual(payload["route_type"], "transfer/suggestion")
        self.assertEqual(payload["function_response"]["status"], "NO_HIT")

    # --- Builder overrides ---

    def test_builder_overrides_override_defaults(self):
        response = build_route_response(
            RouteType.EXACT_HIT,
            query_context=self.context(),
            perturbation_resolution=self.resolution(),
            overrides={"confidence": Confidence.LOW},
        )
        self.assertEqual(response.confidence, Confidence.LOW)

    # --- Serializer round-trips ---

    def test_json_serializer_is_parseable_and_preserves_null_fields(self):
        response = EvidenceRouteResponse(route_type=RouteType.NO_HIT)
        payload = json.loads(response_to_json(response))
        self.assertIn("query_context", payload)
        self.assertIsNone(payload["query_context"])

    def test_yaml_serializer_output_is_valid_yaml(self):
        response = build_route_response(
            RouteType.EXACT_HIT,
            query_context=self.context(),
            perturbation_resolution=self.resolution(),
        )
        yaml_str = response_to_yaml(response)
        parsed = yaml.safe_load(yaml_str)
        self.assertEqual(parsed["route_type"], "exact-hit")
        self.assertEqual(parsed["confidence"], "high")

    def test_serializer_round_trip_preserves_field_values(self):
        original = build_route_response(
            RouteType.EXACT_HIT,
            query_context=self.context(),
            perturbation_resolution=self.resolution(),
        )
        d = response_to_dict(original)
        reconstructed = EvidenceRouteResponse(
            route_type=RouteType(d["route_type"]),
            query_context=QueryContext(
                cell_line=d["query_context"]["cell_line"],
                cell_line_source=CellLineSource(d["query_context"]["cell_line_source"]),
                perturbation_type=PerturbationType(d["query_context"]["perturbation_type"]),
                direction=Direction(d["query_context"]["direction"]),
            ),
            perturbation_resolution=PerturbationResolution(
                method=ResolutionMethod(d["perturbation_resolution"]["method"]),
                resolved_name=d["perturbation_resolution"]["resolved_name"],
                resolved_id=d["perturbation_resolution"]["resolved_id"],
                original_query=d["perturbation_resolution"]["original_query"],
                source_index=SourceIndex(d["perturbation_resolution"]["source_index"]),
                perturbation_type=PerturbationType(d["perturbation_resolution"]["perturbation_type"]),
            ),
            function_response=FunctionResponse(status=FunctionStatus(d["function_response"]["status"])),
            confidence=Confidence(d["confidence"]),
            proxy_chain=[],
        )
        self.assertEqual(reconstructed.route_type, original.route_type)
        self.assertEqual(reconstructed.confidence, original.confidence)
        self.assertEqual(reconstructed.query_context.cell_line, original.query_context.cell_line)

    def test_serializer_handles_proxy_step_from_mapping(self):
        step = ProxyStep(
            dimension=ProxyDimension.PERTURBATION,
            from_="imatinib",
            to="dasatinib",
            via="drug_neighbors.json",
        )
        d = response_to_dict(step)
        self.assertIn("from", d)
        self.assertNotIn("from_", d)
        self.assertEqual(d["from"], "imatinib")

    def test_serializer_round_trip_json_with_all_fields(self):
        ctx = self.context()
        response = build_route_response(
            RouteType.EXACT_HIT,
            query_context=ctx,
            perturbation_resolution=self.resolution(),
        )
        json_str = response_to_json(response)
        parsed = json.loads(json_str)
        self.assertEqual(parsed["route_type"], "exact-hit")
        self.assertEqual(parsed["query_context"]["cell_line"], "A549")
        self.assertEqual(parsed["perturbation_resolution"]["original_query"], "gefitinib")

    # --- Builder validation ---

    def test_builder_raises_on_invalid_route_type(self):
        with self.assertRaises(ValueError):
            build_route_response("not-a-route-type")  # type: ignore

    def test_full_evidence_route_response_construction(self):
        response = EvidenceRouteResponse(
            route_type=RouteType.PROXY_HIT,
            query_context=self.context(),
            perturbation_resolution=self.resolution(),
            function_response=FunctionResponse(status=FunctionStatus.OK),
            confidence=Confidence.MEDIUM,
            proxy_chain=[
                ProxyStep(
                    dimension=ProxyDimension.PERTURBATION,
                    from_="imatinib",
                    to="dasatinib",
                    via="drug_neighbors.json",
                    similarity=0.78,
                    similarity_unit=SimilarityUnit.TANIMOTO,
                    threshold_applied=0.40,
                ),
            ],
            diagnostics=Diagnostics(warnings=["perturbation_proxy_used"]),
            suggestions=[
                Suggestion(
                    type=SuggestionType.REFORMULATED_QUERY,
                    text="Try dasatinib in A549",
                ),
            ],
        )
        self.assertIs(response.route_type, RouteType.PROXY_HIT)
        self.assertEqual(len(response.proxy_chain), 1)
        self.assertEqual(len(response.suggestions), 1)

    # --- Edge cases ---

    def test_serializer_all_eight_fields_present_even_when_none(self):
        response = EvidenceRouteResponse(route_type=RouteType.EXACT_HIT)
        d = response_to_dict(response)
        self.assertEqual(d["route_type"], "exact-hit")
        self.assertIsNone(d["query_context"])

    def test_yaml_serializer_round_trips_complex_response(self):
        response = build_route_response(
            RouteType.PROXY_HIT,
            query_context=self.context(),
            proxy_chain=[
                ProxyStep(
                    dimension=ProxyDimension.CELL_LINE,
                    from_="NCI-H226",
                    to="A549",
                    via="lung/NSCLC/adenocarcinoma via cellline_neighbors.json",
                    similarity_unit=SimilarityUnit.LINEAGE,
                ),
            ],
            diagnostics=Diagnostics(warnings=["cell_line_proxy_used"]),
        )
        yaml_str = response_to_yaml(response)
        parsed = yaml.safe_load(yaml_str)
        self.assertEqual(parsed["route_type"], "proxy-hit")
        self.assertEqual(len(parsed["proxy_chain"]), 1)
        self.assertEqual(parsed["proxy_chain"][0]["dimension"], "cell_line")
        self.assertEqual(parsed["diagnostics"]["warnings"], ["cell_line_proxy_used"])

    def test_route_type_enum_identity(self):
        self.assertIs(RouteType("exact-hit"), RouteType.EXACT_HIT)
        self.assertIs(RouteType("proxy-hit"), RouteType.PROXY_HIT)
        self.assertIs(RouteType("no-hit"), RouteType.NO_HIT)
        self.assertIs(RouteType("ambiguous-hit"), RouteType.AMBIGUOUS_HIT)
        self.assertIs(RouteType("context-missing"), RouteType.CONTEXT_MISSING)
        self.assertIs(RouteType("transfer/suggestion"), RouteType.TRANSFER_SUGGESTION)


if __name__ == "__main__":
    unittest.main()
