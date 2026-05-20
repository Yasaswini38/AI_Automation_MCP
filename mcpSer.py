import os
import json
from datetime import datetime
from fastmcp import FastMCP
from pydantic import BaseModel, Field
from typing import List, Optional


mcp = FastMCP("OpsGenius Automation Router")


class TriageResult(BaseModel):
    customer_name: str
    account_id: Optional[str]
    category: str
    sentiment_score: float
    urgency: str
    tags: List[str]
    automated_reply_draft: str


@mcp.tool()
def execute_system_triage(analyzed_json_str: str) -> str:
    """
    Executes business automation logic based on structured data results.
    Takes a verified stringified JSON payload matching the triage specs.
    """
    try:
        data = json.loads(analyzed_json_str)
        c_urgency = data.get("urgency", "Low").lower()
        category = data.get("category", "General Praise")
        name = data.get("customer_name", "Valued Client")
        
        actions_fired = []
        
        if c_urgency in ["critical", "high"] or category == "Billing":
            actions_fired.append(f"ALERT DISPATCHED: Ticket escalated to high-priority operational Slack channel: #{category.lower()}-alerts.")
        else:
            actions_fired.append("STATUS LOGGED: Dispatched tracking payload to normal service tables.")
            
        ticket_id = f"TICK-{datetime.now().strftime('%M%S')}"
        actions_fired.append(f" RECORD CREATED: Logged {ticket_id} for user reference.")
        
        execution_report = {
            "status": "SUCCESS",
            "ticket_id": ticket_id,
            "actions_executed": actions_fired,
            "payload_data": data
        }
        return json.dumps(execution_report)
        
    except Exception as e:
        return json.dumps({"status": "ERROR", "message": f"Tool Execution Aborted: {str(e)}"})

if __name__ == "__main__":
    mcp.run()