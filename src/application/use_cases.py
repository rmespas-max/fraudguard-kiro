from typing import List
from src.domain.models import (
    Transaction,
    RiskAssessment,
    EvaluatedTransaction,
    FraudDetectorPort,
    TransactionRepositoryPort
)

class AnalyzeTransactionUseCase:
    def __init__(self, detector: FraudDetectorPort, repository: TransactionRepositoryPort):
        self.detector = detector
        self.repository = repository

    def execute(self, transaction: Transaction) -> RiskAssessment:
        assessment = self.detector.evaluate(transaction)
        record = EvaluatedTransaction(transaction=transaction, assessment=assessment)
        self.repository.save(record)
        return assessment

class GetTransactionHistoryUseCase:
    def __init__(self, repository: TransactionRepositoryPort):
        self.repository = repository

    def execute(self) -> List[EvaluatedTransaction]:
        return self.repository.get_all()
