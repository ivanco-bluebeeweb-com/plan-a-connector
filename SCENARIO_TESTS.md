# PST Testing Scenarios for Plan A Connector

## Part A: Authentication & Connectivity Verification
- **Scenario A1: Valid Credential Connect**: `connect_plan_a_connector` saves token and validates endpoint.
- **Scenario A2: Invalid Token Handling**: Returns HTTP 401/403 with descriptive error.
- **Scenario A3: Multi-Account Isolation**: Different tenants store separate credentials in secure vault.

## Part B: Core Read Operations & Boundary Handling
- **Scenario B1: List Emissions**: `list_emissions` returns typed list with bounds.
- **Scenario B2: Get EmissionRecord**: `get_emissionrecord` returns entity details or 404 error.
- **Scenario B3: Health Audit**: `audit_emissionrecord_health` aggregates active records.

## Part C: Safe Write & Idempotency Testing
- **Scenario C1: Connection Lifecycle**: Clean disconnect via `disconnect_plan_a_connector` without lingering secrets.

## Part D: Regression, Deploy & Platform Verification
- **Scenario D1: Deployment Verification**: Clean pull and 22/22 SDK check passes.
- **Scenario D2: Pricing Enforcement**: Per-action pricing active on catalog.
- **Scenario D3: No Secret Leak**: API tokens masked in responses and logs.
