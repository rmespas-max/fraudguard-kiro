# FraudGuard Kiro - Sistema Inteligente de Detección de Fraude

Microservicio backend desarrollado en Python con FastAPI para el análisis y clasificación de transacciones financieras en tiempo real (<200 ms) mediante arquitecturas desacopladas y motores híbridos de Inteligencia Artificial.

---

## 1. Especificación del Proyecto (Kiro SDD)

El desarrollo del proyecto está guiado por las especificaciones formales ubicadas en `.kiro/specs/fraud-detection/`:
- `requirements.md`: Definición del problema, requisitos funcionales y criterios de aceptación.
- `design.md`: Decisiones arquitectónicas (Clean Architecture) y patrones de diseño (Strategy, Repository).
- `tasks.md`: Lista secuencial de tareas de implementación.

---

## 2. Arquitectura de la Solución

El sistema se divide en cuatro capas estrictamente desacopladas:
1. **Domain**: Entidades `Transaction`, `RiskAssessment` y puertos abstractos (`FraudDetectorPort`, `TransactionRepositoryPort`).
2. **Application**: Casos de uso orquestadores (`AnalyzeTransactionUseCase`, `GetTransactionHistoryUseCase`).
3. **Infrastructure**: Adaptadores concretos (`AIEnhancedFraudDetector`, `RuleBasedFraudDetector`, `InMemoryTransactionRepository`).
4. **Interfaces**: Controladores y endpoints REST implementados con FastAPI.

---

## 3. Instalación y Ejecución Local

### Prerrequisitos
- macOS con Python 3.10+ instalado.
- Git y GitHub CLI (`gh`).

### Pasos de Ejecución
```zsh
# 1. Clonar el repositorio
git clone [https://github.com/](https://github.com/)<tu-usuario>/fraudguard-kiro.git
cd fraudguard-kiro

# 2. Crear y activar entorno virtual
python3 -m venv .venv
source .venv/bin/activate

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Iniciar el servidor
uvicorn src.main:app --reload --port 8000
