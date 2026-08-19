import pytest
from src.domain.models import Transaction
from src.infrastructure.detectors import RuleBasedFraudDetector, AIEnhancedFraudDetector

@pytest.fixture
def sample_transaction():
    return Transaction(
        transaction_id="tx_kiro_01",
        account_id="acc_100",
        amount=150.0,
        currency="USD",
        country="BO",
        merchant_category="supermarket",
        device_id="dev_mac_01"
    )

def test_ai_detector_low_risk(sample_transaction):
    fallback = RuleBasedFraudDetector()
    detector = AIEnhancedFraudDetector(fallback_engine=fallback)
    result = detector.evaluate(sample_transaction)
    
    assert result.decision == "APPROVED"
    assert result.risk_score <= 0.20
    assert result.evaluator_engine == "AI_Neural_Engine"

def test_ai_detector_high_risk_cross_border(sample_transaction):
    sample_transaction.amount = 7500.0
    sample_transaction.country = "US"
    
    fallback = RuleBasedFraudDetector()
    detector = AIEnhancedFraudDetector(fallback_engine=fallback)
    result = detector.evaluate(sample_transaction)
    
    assert result.decision == "REVIEW"
    assert result.risk_score > 0.75
    assert "Anomalía de comportamiento transfronterizo" in result.reasons

def test_invalid_negative_amount():
    with pytest.raises(ValueError):
        Transaction(
            transaction_id="tx_invalid",
            account_id="acc_100",
            amount=-50.0,
            currency="USD",
            country="BO",
            merchant_category="supermarket",
            device_id="dev_mac_01"
        )
