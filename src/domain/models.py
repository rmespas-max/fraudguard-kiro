from abc import ABC, abstractmethod
from datetime import datetime, timezone
from typing import List
from pydantic import BaseModel, Field

class Transaction(BaseModel):
    transaction_id: str
    account_id: str
    amount: float = Field(gt=0, description="El monto debe ser estrictamente positivo")
    currency: str
    country: str
    merchant_category: str
    device_id: str
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class RiskAssessment(BaseModel):
    decision: str  # APPROVED, REVIEW, REJECTED
    risk_score: float
    reasons: List[str]
    evaluator_engine: str

class EvaluatedTransaction(BaseModel):
    transaction: Transaction
    assessment: RiskAssessment

class FraudDetectorPort(ABC):
    @abstractmethod
    def evaluate(self, transaction: Transaction) -> RiskAssessment:
        pass

class TransactionRepositoryPort(ABC):
    @abstractmethod
    def save(self, record: EvaluatedTransaction) -> None:
        pass

    @abstractmethod
    def get_all(self) -> List[EvaluatedTransaction]:
        pass
