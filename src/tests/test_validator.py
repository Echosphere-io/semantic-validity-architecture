"""
Tests for Semantic Validity Architecture Validator
Echosphere.io LLC

Run with: pytest test_validator.py -v
"""

import pytest
import sys
sys.path.insert(0, '..')

from validator import SemanticValidator, Claim, ValidationResult, ConstraintStatus


class TestClaim:
    """Tests for the Claim dataclass."""
    
    def test_claim_creation_minimal(self):
        """Test creating a claim with only required field."""
        claim = Claim(content="Test claim")
        assert claim.content == "Test claim"
        assert claim.reference is None
        assert claim.context is None
        assert claim.grounds is None
        assert claim.inference is None
        assert claim.limits is None
        assert claim.purpose is None
    
    def test_claim_creation_complete(self):
        """Test creating a fully specified claim."""
        claim = Claim(
            content="Test claim",
            reference="ref",
            context="ctx",
            grounds="gnd",
            inference="inf",
            limits="lim",
            purpose="pur",
        )
        assert claim.content == "Test claim"
        assert claim.reference == "ref"
        assert claim.context == "ctx"
        assert claim.grounds == "gnd"
        assert claim.inference == "inf"
        assert claim.limits == "lim"
        assert claim.purpose == "pur"


class TestValidationResult:
    """Tests for the ValidationResult dataclass."""
    
    def test_default_status_is_unchecked(self):
        """Test that default status is UNCHECKED."""
        result = ValidationResult()
        assert result.referential == ConstraintStatus.UNCHECKED
        assert result.contextual == ConstraintStatus.UNCHECKED
        assert result.premissive == ConstraintStatus.UNCHECKED
        assert result.inferential == ConstraintStatus.UNCHECKED
        assert result.constraining == ConstraintStatus.UNCHECKED
        assert result.teleological == ConstraintStatus.UNCHECKED
    
    def test_is_valid_all_passed(self):
        """Test is_valid returns True when all constraints pass."""
        result = ValidationResult(
            referential=ConstraintStatus.PASSED,
            contextual=ConstraintStatus.PASSED,
            premissive=ConstraintStatus.PASSED,
            inferential=ConstraintStatus.PASSED,
            constraining=ConstraintStatus.PASSED,
            teleological=ConstraintStatus.PASSED,
        )
        assert result.is_valid is True
    
    def test_is_valid_one_failed(self):
        """Test is_valid returns False when any constraint fails."""
        result = ValidationResult(
            referential=ConstraintStatus.PASSED,
            contextual=ConstraintStatus.PASSED,
            premissive=ConstraintStatus.FAILED,  # One failure
            inferential=ConstraintStatus.PASSED,
            constraining=ConstraintStatus.PASSED,
            teleological=ConstraintStatus.PASSED,
        )
        assert result.is_valid is False
    
    def test_is_valid_unchecked_means_invalid(self):
        """Test is_valid returns False when any constraint is unchecked."""
        result = ValidationResult(
            referential=ConstraintStatus.PASSED,
            contextual=ConstraintStatus.PASSED,
            premissive=ConstraintStatus.PASSED,
            inferential=ConstraintStatus.UNCHECKED,  # Not checked
            constraining=ConstraintStatus.PASSED,
            teleological=ConstraintStatus.PASSED,
        )
        assert result.is_valid is False
    
    def test_failed_constraints_empty_when_all_pass(self):
        """Test failed_constraints is empty when all pass."""
        result = ValidationResult(
            referential=ConstraintStatus.PASSED,
            contextual=ConstraintStatus.PASSED,
            premissive=ConstraintStatus.PASSED,
            inferential=ConstraintStatus.PASSED,
            constraining=ConstraintStatus.PASSED,
            teleological=ConstraintStatus.PASSED,
        )
        assert result.failed_constraints == []
    
    def test_failed_constraints_lists_failures(self):
        """Test failed_constraints lists all failed constraints."""
        result = ValidationResult(
            referential=ConstraintStatus.FAILED,
            contextual=ConstraintStatus.PASSED,
            premissive=ConstraintStatus.FAILED,
            inferential=ConstraintStatus.PASSED,
            constraining=ConstraintStatus.PASSED,
            teleological=ConstraintStatus.FAILED,
        )
        assert "referential" in result.failed_constraints
        assert "premissive" in result.failed_constraints
        assert "teleological" in result.failed_constraints
        assert len(result.failed_constraints) == 3


class TestSemanticValidator:
    """Tests for the SemanticValidator class."""
    
    @pytest.fixture
    def validator(self):
        """Create a validator instance for tests."""
        return SemanticValidator()
    
    def test_validate_empty_claim_fails_all(self, validator):
        """Test that a claim with no constraints fails all checks."""
        claim = Claim(content="Empty claim")
        result = validator.validate(claim)
        
        assert result.is_valid is False
        assert len(result.failed_constraints) == 6
    
    def test_validate_complete_claim_passes_all(self, validator):
        """Test that a fully specified claim passes all checks."""
        claim = Claim(
            content="Complete claim",
            reference="Specific reference",
            context="Specific context",
            grounds="Specific grounds",
            inference="Specific inference",
            limits="Specific limits",
            purpose="Specific purpose",
        )
        result = validator.validate(claim)
        
        assert result.is_valid is True
        assert result.failed_constraints == []
    
    def test_validate_partial_claim(self, validator):
        """Test that a partial claim fails missing constraints only."""
        claim = Claim(
            content="Partial claim",
            reference="Has reference",
            context="Has context",
            grounds="Has grounds",
            # Missing: inference, limits, purpose
        )
        result = validator.validate(claim)
        
        assert result.is_valid is False
        assert result.referential == ConstraintStatus.PASSED
        assert result.contextual == ConstraintStatus.PASSED
        assert result.premissive == ConstraintStatus.PASSED
        assert result.inferential == ConstraintStatus.FAILED
        assert result.constraining == ConstraintStatus.FAILED
        assert result.teleological == ConstraintStatus.FAILED
    
    def test_whitespace_only_fails(self, validator):
        """Test that whitespace-only values fail validation."""
        claim = Claim(
            content="Claim with whitespace",
            reference="   ",  # Whitespace only
            context="Valid context",
            grounds="Valid grounds",
            inference="Valid inference",
            limits="Valid limits",
            purpose="Valid purpose",
        )
        result = validator.validate(claim)
        
        assert result.referential == ConstraintStatus.FAILED
        assert result.is_valid is False
    
    def test_check_referential(self, validator):
        """Test referential constraint check in isolation."""
        valid_claim = Claim(content="test", reference="valid ref")
        invalid_claim = Claim(content="test", reference=None)
        empty_claim = Claim(content="test", reference="")
        
        assert validator.check_referential(valid_claim) is True
        assert validator.check_referential(invalid_claim) is False
        assert validator.check_referential(empty_claim) is False
    
    def test_check_contextual(self, validator):
        """Test contextual constraint check in isolation."""
        valid_claim = Claim(content="test", context="valid context")
        invalid_claim = Claim(content="test", context=None)
        
        assert validator.check_contextual(valid_claim) is True
        assert validator.check_contextual(invalid_claim) is False
    
    def test_check_premissive(self, validator):
        """Test premissive constraint check in isolation."""
        valid_claim = Claim(content="test", grounds="valid grounds")
        invalid_claim = Claim(content="test", grounds=None)
        
        assert validator.check_premissive(valid_claim) is True
        assert validator.check_premissive(invalid_claim) is False
    
    def test_check_inferential(self, validator):
        """Test inferential constraint check in isolation."""
        valid_claim = Claim(content="test", inference="valid inference")
        invalid_claim = Claim(content="test", inference=None)
        
        assert validator.check_inferential(valid_claim) is True
        assert validator.check_inferential(invalid_claim) is False
    
    def test_check_constraining(self, validator):
        """Test constraining constraint check in isolation."""
        valid_claim = Claim(content="test", limits="valid limits")
        invalid_claim = Claim(content="test", limits=None)
        
        assert validator.check_constraining(valid_claim) is True
        assert validator.check_constraining(invalid_claim) is False
    
    def test_check_teleological(self, validator):
        """Test teleological constraint check in isolation."""
        valid_claim = Claim(content="test", purpose="valid purpose")
        invalid_claim = Claim(content="test", purpose=None)
        
        assert validator.check_teleological(valid_claim) is True
        assert validator.check_teleological(invalid_claim) is False


class TestRealWorldScenarios:
    """Tests using realistic AI output scenarios."""
    
    @pytest.fixture
    def validator(self):
        return SemanticValidator()
    
    def test_typical_ai_hallucination(self, validator):
        """Test that typical AI hallucination fails validation."""
        # This is what ChatGPT might say - confident but ungrounded
        hallucination = Claim(
            content="The company was founded in 1985 and has 500 employees.",
            reference="ACME Corp",
            # Missing everything else - classic hallucination pattern
        )
        result = validator.validate(hallucination)
        
        assert result.is_valid is False
        assert len(result.failed_constraints) >= 4
    
    def test_grounded_factual_claim(self, validator):
        """Test that a properly grounded claim passes."""
        grounded = Claim(
            content="ACME Corp reported $50M revenue in Q3.",
            reference="ACME Corp Q3 2024 financial results",
            context="Q3 fiscal year 2024, as reported to SEC",
            grounds="10-Q filing dated October 15, 2024",
            inference="Direct extraction from line item 'Total Revenue' on page 5",
            limits="Unaudited figures; USD; excludes discontinued operations",
            purpose="To answer user query about ACME's recent financial performance",
        )
        result = validator.validate(grounded)
        
        assert result.is_valid is True


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
