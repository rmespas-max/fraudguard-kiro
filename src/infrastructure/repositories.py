from typing import List
from src.domain.models import TransactionRepositoryPort, EvaluatedTransaction

class InMemoryTransactionRepository(TransactionRepositoryPort):
    def __init__(self):
        self._storage: List[EvaluatedTransaction] = []

    def save(self, record: EvaluatedTransaction) -> None:
        self._storage.append(record)

    def get_all(self) -> List[EvaluatedTransaction]:
        return list(self._storage)
