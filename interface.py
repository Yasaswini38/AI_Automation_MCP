import streamlit as st
import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="OpsGenius MCP Router", page_icon="⚡", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    div[data-testid="stMetricValue"] { font-size: 24px; color: #ff4b4b; font-weight: bold; }
    .status-badge { padding: 6px 12px; border-radius: 6px; font-weight: 600; font-size: 14px; text-align: center; }
    .critical { background-color: #ff4b4b22; color: #ff4b4b; border: 1px solid #ff4b4b; }
    .normal { background-color: #00f0ff22; color: #00f0ff; border: 1px solid #00f0ff; }
    </style>
""", unsafe_allow_html=True)

st.title("⚡ Model Context Protocol (MCP) Autonomous Hub")
st.caption("Decoupled Intelligent Automation Pipeline running via FastMCP Standards")
st.write("---")

MOCK_TEMPLATES = {
    "Urgent Escalation (Payment Failure)": 
        "Hi Support,\nMy name is Priya Sharma (ID: REF-9021). I just tried to upgrade my subscription to the premium tier, but your system threw an unexpected 504 Gateway error during check out. My card was charged $299 but my account access states I am still on the free plan! Please look into this right now.\nThanks,\nPriya",
    "Feature Request / Feedback":
        "Hello Team,\nThis is David Vance. Love your service! I wanted to drop a quick request to see if we can get customizable webhook payload structures added to our configuration settings panel next quarter.\nBest, David",
}

col1, col2 = st.columns([1, 1], gap="large")

with col1:
    st.subheader("Ingestion Endpoint")
    selected_template = st.selectbox("Load Scenario Template:", list(MOCK_TEMPLATES.keys()))
    input_text = st.text_area("Raw Communication Payload Body:", value=MOCK_TEMPLATES[selected_template], height=220)
    trigger_pipeline = st.button("Run MCP Pipeline Sequence", use_container_width=True)

with col2:
    st.subheader("Active Protocol Tracking Dashboard")
    
    if trigger_pipeline:
        api_key = os.getenv("OPENROUTER_API_KEY")
        if not api_key or "your_openrouter" in api_key:
            st.error("Missing OPENROUTER_API_KEY in environment configurations.")
            st.stop()
            
        with st.spinner("Step 1: Consulting LLM Cognitive Layer via OpenRouter..."):
            url = "https://openrouter.ai/api/v1/chat/completions"
            headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
            
            # Explicit, strict JSON schema template structure
            schema_definition = {
                "type": "object",
                "properties": {
                    "customer_name": {"type": "string"},
                    "account_id": {"type": "string"},
                    "category": {"type": "string"},
                    "sentiment_score": {"type": "number"},
                    "urgency": {"type": "string"},
                    "tags": {"type": "array", "items": {"type": "string"}},
                    "automated_reply_draft": {"type": "string"}
                },
                "required": ["customer_name", "category", "sentiment_score", "urgency", "tags", "automated_reply_draft"]
            }

            payload = {
                "model": "google/gemini-2.5-flash",
                "messages": [
                    {"role": "user", "content": f"Analyze this text and output a JSON object matching the requested schema fields. Text: {input_text}"}
                ],
                "response_format": {
                    "type": "json_schema",
                    "json_schema": {
                        "name": "triage_response",
                        "strict": True,
                        "schema": schema_definition
                    }
                },
                "plugins": [
                    {"id": "response-healing"} # Automatically resolves string literal parsing breaks upstream
                ],
                "temperature": 0.1
            }
            
            try:
                res = requests.post(url, headers=headers, json=payload, timeout=30)
                res.raise_for_status()
                raw_json = res.json()['choices'][0]['message']['content'].strip()
                
                # Direct safe load
                parsed_data = json.loads(raw_json)
                
                # Render analytical panels
                m1, m2, m3 = st.columns(3)
                with m1: st.metric("Identity", parsed_data.get("customer_name", "N/A"))
                with m2: st.metric("Reference ID", parsed_data.get("account_id") if parsed_data.get("account_id") else "None")
                with m3: st.metric("Sentiment", f"{parsed_data.get('sentiment_score', 0.0):.2f}")
                
                st.write("")
                c_urgency = parsed_data.get("urgency", "Low").lower()
                badge_class = "critical" if c_urgency in ["critical", "high"] else "normal"
                st.markdown(f"**Urgency Profile Rating:** <span class='status-badge {badge_class}'>{parsed_data.get('urgency', 'LOW').upper()}</span> | Category Pipeline: `{parsed_data.get('category')}`", unsafe_allow_html=True)
                
                st.write("---")
                st.subheader("Step 2: Simulating Native MCP Server Tool Call")
                
                with st.spinner("Invoking `execute_system_triage` tool matching MCP specs..."):
                    from mcpSer import execute_system_triage
                    
                    mcp_tool_response = execute_system_triage(json.dumps(parsed_data))
                    tool_report = json.loads(mcp_tool_response)
                    
                    if tool_report["status"] == "SUCCESS":
                        st.success(f"**MCP Server Connection Status: Connected via STDIO Channels**")
                        st.info(f"Assigned Ticket ID: `{tool_report['ticket_id']}`")
                        
                        st.write("**Executed Action Hooks Dispatched by Server:**")
                        for action in tool_report["actions_executed"]:
                            st.code(action, language="text")
                            
                        st.markdown("### Autonomous Email Response Generated")
                        st.warning(parsed_data.get("automated_reply_draft"))
                    else:
                        st.error(f"MCP Server tool error: {tool_report['message']}")
                        
            except Exception as ex:
                st.error(f"Execution Error occurred: {str(ex)}")
    else:
        st.info("Awaiting execution sequence trigger. Press the button to run the real end-to-end Model Context Protocol logic.")