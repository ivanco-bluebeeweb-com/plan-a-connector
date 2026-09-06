"""Resource handlers for Plan A Connector."""
from __future__ import annotations
from typing import Any
from imperal_sdk import ActionResult
from app import chat
from schemas import (
    ListEmissionRecordParams, GetEmissionRecordParams,
    EmissionRecordRecord, EmissionRecordList, AuditHealthReport, ConnectionIdParams
)
from handlers_connection import resolve_client

@chat.function("list_emissions", "List emissions in Plan A.", action_type="read", chain_callable=True, event="plan-a-connector.list_emissions", effects=["read:emissions"], data_model=EmissionRecordList)
async def list_emissions(params: ListEmissionRecordParams, ctx) -> ActionResult:
    client = await resolve_client(ctx, params.connection_id)
    try:
        raw_items = await client.list_emissions(limit=params.limit)
        items = []
        for r in raw_items:
            rid = str(r.get("id") or r.get("key") or r.get("uuid") or "unknown")
            rname = r.get("name") or r.get("title") or r.get("label") or rid
            items.append({"id": rid, "name": rname, "status": r.get("status"), "created_at": r.get("createdAt") or r.get("created_at"), "raw": r})
        return ActionResult.ok({"emissions": items, "total": len(items)}, summary=f"Found {len(items)} emissions.")
    except Exception as e:
        return ActionResult.error(f"Error listing emissions: {e}")

@chat.function("get_emissionrecord", "Get details of one EmissionRecord in Plan A.", action_type="read", chain_callable=True, event="plan-a-connector.get_emissionrecord", effects=["read:emissionrecord"], data_model=EmissionRecordRecord)
async def get_emissionrecord(params: GetEmissionRecordParams, ctx) -> ActionResult:
    client = await resolve_client(ctx, params.connection_id)
    try:
        r = await client.get_emissionrecord(params.emissionrecord_id)
        rid = str(r.get("id") or params.emissionrecord_id)
        rname = r.get("name") or r.get("title") or rid
        return ActionResult.ok({"id": rid, "name": rname, "status": r.get("status"), "created_at": r.get("createdAt") or r.get("created_at"), "raw": r}, summary=f"Retrieved EmissionRecord {rid}.")
    except Exception as e:
        return ActionResult.error(f"Error retrieving EmissionRecord: {e}")

@chat.function("audit_emissionrecord_health", "Audit health of Plan A emissions and connectivity.", action_type="read", chain_callable=True, event="plan-a-connector.audit_emissionrecord_health", effects=["read:audit"], data_model=AuditHealthReport)
async def audit_emissionrecord_health(params: ConnectionIdParams, ctx) -> ActionResult:
    client = await resolve_client(ctx, params.connection_id)
    try:
        items = await client.list_emissions(limit=50)
        return ActionResult.ok({
            "healthy": True,
            "total_emissions": len(items),
            "details": {"sample_count": len(items)},
            "summary": f"Plan A healthy. Sampled {len(items)} emissions."
        }, summary=f"Plan A health check passed with {len(items)} emissions.")
    except Exception as e:
        return ActionResult.error(f"Error auditing Plan A health: {e}")
