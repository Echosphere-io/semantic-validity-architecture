"""
Semantic Validity Architecture - Reference Validator
Echosphere.io LLC

A minimal proof-of-concept implementation demonstrating the six-constraint
validation architecture. This skeleton provides the structure; full
implementation details are covered by patent-pending claims.
"""

from dataclasses import dataclass
from typing import Optional
from enum import Enum


class ConstraintStatus(Enum):
    """Status of a constraint check."""
    PASSED = "passed"
    FAILED = "failed"
    UNCHECKED = "unchecked"


@dataclass
class Claim:
    """
    A claim to be validated against the six constraints.
    
    Attributes:
        content: The assertion being made
        reference: What the claim refers to (Constraint 1)
        context: Conditions under which the claim applies (Constraint 2)
        grounds: Evidence or premises supporting the claim (Constraint 3)
        inference: Reasoning chain from grounds to conclusion (Constraint 4)
        limits: Scope and boundaries of the claim (Constraint 5)
        purpose: Why this claim matters / what it's for (Constraint 6)
    """
    content: str
    reference: Optional[str] = None
    context: Optional[str] = None
    grounds: Optional[str] = None
    inference: Optional[str] = None
    limits: Optional[str] = None
    purpose: Optional[str] = None


@dataclass
class ValidationResult:
    """Result of validating a claim against all six constraints."""
    referential: ConstraintStatus = ConstraintStatus.UNCHECKED
    contextual: ConstraintStatus = ConstraintStatus.UNCHECKED
    premissive: ConstraintStatus = ConstraintStatus.UNCHECKED
    inferential: ConstraintStatus = ConstraintStatus.UNCHECKED
    constraining: ConstraintStatus = ConstraintStatus.UNCHECKED
    teleological: ConstraintStatus = ConstraintStatus.UNCHECKED
    
    @property
    def is_valid(self) -> bool:
        """A claim is valid only if all six constraints pass."""
        return all([
            self.referential == ConstraintStatus.PASSED,
            self.contextual == ConstraintStatus.PASSED,
            self.premissive == ConstraintStatus.PASSED,
            self.inferential == ConstraintStatus.PASSED,
            self.constraining == ConstraintStatus.PASSED,
            self.teleological == ConstraintStatus.PASSED,
        ])
    
    @property
    def failed_constraints(self) -> list[str]:
        """Return list of constraint names that failed."""
        failed = []
        if self.referential == ConstraintStatus.FAILED:
            failed.append("referential")
        if self.contextual == ConstraintStatus.FAILED:
            failed.append("contextual")
        if self.premissive == ConstraintStatus.FAILED:
            failed.append("premissive")
        if self.inferential == ConstraintStatus.FAILED:
            failed.append("inferential")
        if self.constraining == ConstraintStatus.FAILED:
            failed.append("constraining")
        if self.teleological == ConstraintStatus.FAILED:
            failed.append("teleological")
        return failed


class SemanticValidator:
    """
    Validates claims against the six semantic constraints.
    
    The Six Constraints:
        1. Referential   - WHAT is claimed?
        2. Contextual    - Under what CONDITIONS?
        3. Premissive    - On what GROUNDS?
        4. Inferential   - WHY does it follow?
        5. Constraining  - What are the LIMITS?
        6. Teleological  - What is it FOR?
    
    A claim that passes all six constraints is semantically complete.
    A claim that fails any constraint is caught before delivery.
    """
    
    def __init__(self):
        self.constraints = [
            ("referential", self.check_referential),
            ("contextual", self.check_contextual),
            ("premissive", self.check_premissive),
            ("inferential", self.check_inferential),
            ("constraining", self.check_constraining),
            ("teleological", self.check_teleological),
        ]
    
    def validate(self, claim: Claim) -> ValidationResult:
        """
        Validate a claim against all six constraints.
        
        Args:
            claim: The Claim object to validate
            
        Returns:
            ValidationResult with status for each constraint
        """
        result = ValidationResult()
        
        result.referential = (
            ConstraintStatus.PASSED if self.check_referential(claim) 
            else ConstraintStatus.FAILED
        )
        result.contextual = (
            ConstraintStatus.PASSED if self.check_contextual(claim) 
            else ConstraintStatus.FAILED
        )
        result.premissive = (
            ConstraintStatus.PASSED if self.check_premissive(claim) 
            else ConstraintStatus.FAILED
        )
        result.inferential = (
            ConstraintStatus.PASSED if self.check_inferential(claim) 
            else ConstraintStatus.FAILED
        )
        result.constraining = (
            ConstraintStatus.PASSED if self.check_constraining(claim) 
            else ConstraintStatus.FAILED
        )
        result.teleological = (
            ConstraintStatus.PASSED if self.check_teleological(claim) 
            else ConstraintStatus.FAILED
        )
        
        return result
    
    def check_referential(self, claim: Claim) -> bool:
        """
        Constraint 1: WHAT is claimed?
        
        Checks if the claim's reference is clear and unambiguous.
        The claim must point to something specific and identifiable.
        """
        # Basic check: reference must be provided and non-empty
        return claim.reference is not None and len(claim.reference.strip()) > 0
    
    def check_contextual(self, claim: Claim) -> bool:
        """
        Constraint 2: Under what CONDITIONS?
        
        Checks if the conditions/context are specified.
        Claims without context risk overgeneralization.
        """
        # Basic check: context must be provided and non-empty
        return claim.context is not None and len(claim.context.strip()) > 0
    
    def check_premissive(self, claim: Claim) -> bool:
        """
        Constraint 3: On what GROUNDS?
        
        Checks if grounds/evidence are provided.
        Claims without grounds are unwarranted assertions.
        """
        # Basic check: grounds must be provided and non-empty
        return claim.grounds is not None and len(claim.grounds.strip()) > 0
    
    def check_inferential(self, claim: Claim) -> bool:
        """
        Constraint 4: WHY does it follow?
        
        Checks if the reasoning from grounds to conclusion is valid.
        Claims without valid inference are non-sequiturs.
        """
        # Basic check: inference must be provided and non-empty
        return claim.inference is not None and len(claim.inference.strip()) > 0
    
    def check_constraining(self, claim: Claim) -> bool:
        """
        Constraint 5: What are the LIMITS?
        
        Checks if the scope and boundaries are defined.
        Claims without limits risk overclaiming.
        """
        # Basic check: limits must be provided and non-empty
        return claim.limits is not None and len(claim.limits.strip()) > 0
    
    def check_teleological(self, claim: Claim) -> bool:
        """
        Constraint 6: What is it FOR?
        
        Checks if the purpose/relevance is clear.
        Claims without purpose risk irrelevance.
        """
        # Basic check: purpose must be provided and non-empty
        return claim.purpose is not None and len(claim.purpose.strip()) > 0


if __name__ == "__main__":
    # Quick demonstration
    validator = SemanticValidator()
    
    # Example: An incomplete claim (missing several constraints)
    incomplete_claim = Claim(
        content="The system is reliable.",
        reference="System X",
        # Missing: context, grounds, inference, limits, purpose
    )
    
    result = validator.validate(incomplete_claim)
    print(f"Incomplete claim valid: {result.is_valid}")
    print(f"Failed constraints: {result.failed_constraints}")
    
    # Example: A complete claim (all constraints satisfied)
    complete_claim = Claim(
        content="System X achieves 99.5% uptime.",
        reference="System X production instance",
        context="Under normal operating conditions, Q4 2024",
        grounds="Based on monitoring data from 90-day observation period",
        inference="Uptime calculated as (total_time - downtime) / total_time",
        limits="Excludes scheduled maintenance windows; applies to primary region only",
        purpose="To inform infrastructure capacity planning decisions",
    )
    
    result = validator.validate(complete_claim)
    print(f"\nComplete claim valid: {result.is_valid}")
    print(f"Failed constraints: {result.failed_constraints}")
