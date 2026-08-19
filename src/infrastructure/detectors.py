from src.domain.models import FraudDetectorPort, Transaction, RiskAssessment

class RuleBasedFraudDetector(FraudDetectorPort):
    def evaluate(self, transaction: Transaction) -> RiskAssessment:
        if transaction.amount > 5000 or transaction.country in ["RU", "NG", "KP"]:
            return RiskAssessment(
                decision="REJECTED",
                risk_score=0.90,
                reasons=["Monto excede límite base", "País de alto riesgo"],
                evaluator_engine="Rule_Engine_Fallback"
            )
        return RiskAssessment(
            decision="APPROVED",
            risk_score=0.05,
            reasons=["Parámetros estándar conformes"],
            evaluator_engine="Rule_Engine_Fallback"
        )

class AIEnhancedFraudDetector(FraudDetectorPort):
    def __init__(self, fallback_engine: FraudDetectorPort):
        self.fallback_engine = fallback_engine

    def evaluate(self, transaction: Transaction) -> RiskAssessment:
        try:
            if transaction.amount > 5000 and transaction.country != "BO":
                return RiskAssessment(
                    decision="REVIEW",
                    risk_score=0.82,
                    reasons=["Anomalía de comportamiento transfronterizo", "Monto atípico"],
                    evaluator_engine="AI_Neural_Engine"
                )
            elif transaction.amount <= 1000:
                return RiskAssessment(
                    decision="APPROVED",
                    risk_score=0.10,
                    reasons=["Comportamiento habitual detectado"],
                    evaluator_engine="AI_Neural_Engine"
                )
            return RiskAssessment(
                decision="APPROVED",
                risk_score=0.35,
                reasons=["Riesgo moderado aceptado"],
                evaluator_engine="AI_Neural_Engine"
            )
        except Exception:
            return self.fallback_engine.evaluate(transaction)
