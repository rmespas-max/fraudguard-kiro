# Requirements Specification: FraudGuard Kiro

## 1. Problema del Negocio
Las instituciones financieras y pasarelas de pago sufren pérdidas por transacciones fraudulentas no detectadas en tiempo real. Se requiere un servicio de análisis automatizado de baja latencia (<200 ms) capaz de evaluar transacciones bancarias entrantes mediante un enfoque híbrido (reglas deterministas + inteligencia artificial) y almacenar los eventos evaluados.

## 2. Requisitos Funcionales y Criterios de Aceptación

### Requisito 1: Ingesta y Validación de Transacciones
- **Descripción**: La API debe recibir un payload JSON con los datos de la transacción y validar estrictamente tipos y campos obligatorios.
- **Criterios de Aceptación**:
  - Si faltan campos obligatorios (`transaction_id`, `account_id`, `amount`, `currency`, `country`, `merchant_category`, `device_id`), la API retorna error HTTP 422.
  - Si el monto es menor o igual a 0, la API rechaza la solicitud por validación de esquema.

### Requisito 2: Evaluación de Riesgo con Estrategia Híbrida (IA y Reglas)
- **Descripción**: La API debe calcular un puntaje de riesgo (`risk_score` entre 0.0 y 1.0) y emitir un veredicto (`APPROVED`, `REVIEW`, `REJECTED`).
- **Criterios de Aceptación**:
  - Transacciones con montos habituales (<$1000) y país local se evalúan con score bajo (<0.20) y decisión `APPROVED`.
  - Transacciones de monto elevado (>$5000) o países transfronterizos no habituales generan score >0.75 y decisión `REVIEW` o `REJECTED`.
  - Si el motor de IA falla o excede el tiempo límite, el sistema conmuta automáticamente a un motor de reglas deterministas (fallback) sin interrumpir el servicio.

### Requisito 3: Persistencia y Consulta de Eventos
- **Descripción**: Cada transacción analizada debe registrarse con su veredicto, fecha de creación y motor utilizado.
- **Criterios de Aceptación**:
  - La transacción evaluada queda guardada inmediatamente en el repositorio de datos.
  - La API expone un endpoint para consultar el historial completo de transacciones procesadas.
