"""Extension declaration, capabilities, health check for Plan A Connector."""
from __future__ import annotations
import json
from imperal_sdk import ChatExtension, Extension

ext = Extension(
    "plan-a-connector",
    version="0.1.0",
    display_name="Plan A",
    icon="icon.svg",
    capabilities=["plan_a:manage"],
    description="Official Imperal connector for Plan A (C30. Email Marketing & Newsletter). Manage operations securely."
)

chat = ChatExtension(ext)

@ext.health_check
async def health_check(ctx) -> dict:
    raw = await ctx.secrets.get("plan_a_connections")
    try:
        count = len(json.loads(raw)) if raw else 0
    except Exception:
        count = 0
    return {
        "healthy": True,
        "detail": f"{count} Plan A connection(s) configured." if count else "Not connected yet."
    }
