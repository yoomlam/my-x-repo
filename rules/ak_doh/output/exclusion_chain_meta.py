# exclusion_chain_meta.py  (transpiler-generated — do not edit)
# Field categories for ExclusionChainDecision scope.
# "decision"        — primary outcome fields (decisions: section)
# "computed_output" — intermediate values tagged output: (computed: section)
# "subscope_output" — invoke: computed fields that are subscope references

SCOPE_METADATA: dict[str, str] = {
    # Computed outputs
    "after_65": "computed_output",
    "after_irwe": "computed_output",
    "after_half": "computed_output",
    "after_blind": "computed_output",
    # Decisions
    "adjusted_earned_income": "decision",
}

DECISION_FIELDS     = [k for k, v in SCOPE_METADATA.items() if v == "decision"]
COMPUTED_OUT_FIELDS = [k for k, v in SCOPE_METADATA.items() if v == "computed_output"]
SUBSCOPE_FIELDS     = [k for k, v in SCOPE_METADATA.items() if v == "subscope_output"]
