from fastapi import FastAPI
from src.interfaces.api import router

app = FastAPI(
    title="FraudGuard Kiro API",
    description="Sistema inteligente de detección de fraudes en transacciones financieras",
    version="1.0.0"
)

app.include_router(router)

@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "FraudGuard Kiro API"}
