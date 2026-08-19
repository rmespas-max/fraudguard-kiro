# src/interfaces/api.py
from fastapi import APIRouter, Depends
from typing import List
from src.domain.models import Transaction, RiskAssessment, EvaluatedTransaction
from src.application.use_cases import AnalyzeTransactionUseCase, GetTransactionHistoryUseCase
from src.infrastructure.detectors import AIEnhancedFraudDetector, RuleBasedFraudDetector
from src.infrastructure.repositories import InMemoryTransactionRepository

router = APIRouter(prefix="/api/v1/transactions", tags=["Transactions"])

repo_singleton = InMemoryTransactionRepository()
fallback_detector = RuleBasedFraudDetector()
ai_detector = AIEnhancedFraudDetector(fallback_engine=fallback_detector)

def get_analyze_use_case() -> AnalyzeTransactionUseCase:
    return AnalyzeTransactionUseCase(detector=ai_detector, repository=repo_singleton)

def get_history_use_case() -> GetTransactionHistoryUseCase:
    return GetTransactionHistoryUseCase(repository=repo_singleton)

@router.post("/analyze", response_model=RiskAssessment, status_code=200)
def analyze_transaction(
    tx: Transaction,
    use_case: AnalyzeTransactionUseCase = Depends(get_analyze_use_case)
):
    return use_case.execute(tx)

@router.get("", response_model=List[EvaluatedTransaction], status_code=200)
def get_history(
    use_case: GetTransactionHistoryUseCase = Depends(get_history_use_case)
):
    return use_case.execute()
