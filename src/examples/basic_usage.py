"""
Basic Usage Example - Semantic Validity Architecture
Echosphere.io LLC

This example demonstrates how to use the SemanticValidator to check
claims against the six constraints.
"""

from validator import SemanticValidator, Claim


def main():
    # Initialize the validator
    validator = SemanticValidator()
    
    print("=" * 60)
    print("Semantic Validity Architecture - Basic Usage Example")
    print("=" * 60)
    
    # -----------------------------------------------------------------
    # Example 1: A typical AI hallucination (incomplete claim)
    # -----------------------------------------------------------------
    print("\n--- Example 1: Incomplete Claim (Typical AI Output) ---\n")
    
    ai_hallucination = Claim(
        content="Napoleon was the first emperor of France.",
        reference="Napoleon Bonaparte",
        # Missing: context, grounds, inference, limits, purpose
        # This is what AI often does - states facts without grounding
    )
    
    result = validator.validate(ai_hallucination)
    
    print(f"Claim: \"{ai_hallucination.content}\"")
    print(f"Valid: {result.is_valid}")
    print(f"Failed constraints: {result.failed_constraints}")
    print("\nThis claim would be CAUGHT before delivery because it lacks:")
    print("  - Context (when/where does this apply?)")
    print("  - Grounds (what evidence supports this?)")
    print("  - Inference (how do we get from evidence to conclusion?)")
    print("  - Limits (what are the boundaries of this claim?)")
    print("  - Purpose (why does this matter?)")
    
    # -----------------------------------------------------------------
    # Example 2: A semantically complete claim
    # -----------------------------------------------------------------
    print("\n--- Example 2: Complete Claim (Passes All Six) ---\n")
    
    complete_claim = Claim(
        content="The Q3 revenue exceeded projections by 12%.",
        reference="Q3 2024 revenue for North American retail division",
        context="Fiscal year 2024, compared to board-approved projections from January",
        grounds="Audited financial statements, SAP revenue reports, projection documents",
        inference="Actual ($142M) minus projected ($127M) equals $15M overage; $15M/$127M = 11.8%, rounded to 12%",
        limits="North America only; excludes one-time asset sale of $3M; retail division only, not wholesale",
        purpose="To inform Q4 resource allocation and 2025 projection methodology",
    )
    
    result = validator.validate(complete_claim)
    
    print(f"Claim: \"{complete_claim.content}\"")
    print(f"Valid: {result.is_valid}")
    print(f"Failed constraints: {result.failed_constraints}")
    print("\nThis claim PASSES because it specifies:")
    print(f"  ✓ Reference: {complete_claim.reference}")
    print(f"  ✓ Context: {complete_claim.context}")
    print(f"  ✓ Grounds: {complete_claim.grounds}")
    print(f"  ✓ Inference: {complete_claim.inference}")
    print(f"  ✓ Limits: {complete_claim.limits}")
    print(f"  ✓ Purpose: {complete_claim.purpose}")
    
    # -----------------------------------------------------------------
    # Example 3: Partially complete claim
    # -----------------------------------------------------------------
    print("\n--- Example 3: Partially Complete Claim ---\n")
    
    partial_claim = Claim(
        content="Customer satisfaction improved significantly.",
        reference="Customer satisfaction scores",
        context="Q2 to Q3 2024",
        grounds="NPS survey results",
        # Missing: inference, limits, purpose
    )
    
    result = validator.validate(partial_claim)
    
    print(f"Claim: \"{partial_claim.content}\"")
    print(f"Valid: {result.is_valid}")
    print(f"Failed constraints: {result.failed_constraints}")
    print("\nThis claim fails because:")
    print("  - No inference: How does survey data prove 'significant' improvement?")
    print("  - No limits: Which customers? Which products? Which regions?")
    print("  - No purpose: Why are we measuring this? What decision does it inform?")
    
    # -----------------------------------------------------------------
    # Summary
    # -----------------------------------------------------------------
    print("\n" + "=" * 60)
    print("KEY INSIGHT")
    print("=" * 60)
    print("""
The six constraints work together to ensure semantic validity:

  1. Referential   → WHAT is claimed?
  2. Contextual    → Under what CONDITIONS?
  3. Premissive    → On what GROUNDS?
  4. Inferential   → WHY does it follow?
  5. Constraining  → What are the LIMITS?
  6. Teleological  → What is it FOR?

A claim missing ANY constraint is incomplete and potentially invalid.
This is how we catch hallucinations, drift, and overclaiming BEFORE
they reach the user.
""")


if __name__ == "__main__":
    main()
