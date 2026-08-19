# System Design: FraudGuard Kiro

## 1. Estilo Arquitectónico
Se implementa **Clean Architecture** (Puertos y Adaptadores):
- **Domain**: Entidades `Transaction`, `RiskAssessment` y puertos abstractos (`FraudDetectorPort`, `TransactionRepositoryPort`).
- **Application**: Casos de uso `AnalyzeTransactionUseCase` y `GetTransactionHistoryUseCase`.
- **Infrastructure**: Implementaciones concretas (`AIEnhancedFraudDetector`, `RuleBasedFraudDetector`, `InMemoryTransactionRepository`).
- **Interfaces**: Controladores FastAPI expuestos bajo `/api/v1/transactions`.

## 2. Patrones de Diseño
- **Strategy Pattern**: Permite alternar dinámicamente entre el detector basado en IA y el detector heurístico de respaldo.
- **Repository Pattern**: Desacopla la lógica del almacenamiento de datos.
- **Dependency Injection**: Los casos de uso reciben sus dependencias en el constructor.
