# Plan A Connector — Connector Discovery

**Category:** C48. Environmental, Social & Governance (ESG) Reporting  
**Vendor:** Plan A  
**Official Website:** https://plana.earth

## 1. Официальный API
- **Базовый URL API:** `https://api.plana.earth/v1`
- **Поддерживаемая модель авторизации:** Bearer API Token

## 2. Архитектура сущностей
- Ключевые ресурсы платформы Plan A:
  - источники выбросов (/emissions)
  - объекты/локации (/facilities)
  - показатели активности (/activity-data)
  - ESG-отчеты

## 3. Требования к отказоустойчивости и безопасности
- Соблюдение вендорных лимитов запросов (Rate Limiting) с экспоненциальной задержкой.
- Строгая валидация Pydantic-схем на входе и выходе каждого запроса.
- Тестовая точка проверки подключения: `GET /v1/facilities`.
