
# OpsGenius: Autonomous MCP Triage & Action Routing Hub

OpsGenius is a production-grade, decoupled AI automation engine designed to solve one of the biggest headaches growing companies face: **Inbox Chaos**. 

Instead of building a generic, chat-based assistant, this system operates as an enterprise-ready pipeline using the **Model Context Protocol (MCP)** framework. It seamlessly transforms messy, unstructured human language (emails, feedback, bug logs) into type-safe, structured data structures and immediate backend business actions in under three seconds.

---

## The "Why" (The Problem & Impact)

Every day, customer-facing businesses are flooded with hundreds of unstructured communications. Some are critical billing errors, some are technical system bugs, and others are simple feature requests. 

*   **The Bottleneck:** Traditional software cannot read unstructured paragraphs. A human must manually sit down, read every email, determine its urgency, find tracking IDs, route it to the correct department, log a ticket, and type out a response.
*   **The Impact:** This manual process causes critical, revenue-impacting issues to sit forgotten in crowded inboxes for 12+ hours, leading to customer churn and operational friction.
*   **The Solution:** OpsGenius completely automates this lifecycle. It handles data extraction, priority mapping, instant webhook routing, database logging, and contextual email drafting instantly—dropping response latencies down to milliseconds.

---

## 🛠️ The "How" (Architecture & Protocol Matrix)

The application utilizes a modular, decoupled architectural footprint to separate cognitive processing from backend action triggers:

```text
 [Messy Raw Input] ──> [OpenRouter: Gemini 2.5 Flash] ──> [Strict JSON Schema Execution]
                                                                    │
                                                                    ▼
 [Streamlit Host UI] <── [Deterministic Action Logs] <── [FastMCP Protocol Server Tool]
 ```
Ingestion & UI Console (interface.py): Built with Streamlit, providing a clean, dark-mode administrative command layout with responsive metric cards, state badges, and live action logs.

Cognitive Extraction Layer: Routes data to Google's Gemini 2.5 Flash via OpenRouter. By passing a strict structure contract and utilizing upstream Response Healing, it guarantees that the model behaves like a predictable software component, completely removing markdown artifacts or formatting corruption.

Protocol Core (mcp_server.py): Built natively using FastMCP. Instead of standard tight-coupled APIs, the backend logic functions as a standalone, open-standard Model Context Protocol (MCP) Server. It exposes the operational triage as a reusable protocol tool, meaning this exact engine can be plugged into any corporate AI agent ecosystem natively with zero configuration changes.

Project Setup & Installation
Prerequisites
Make sure you have Python installed, then set up your local project directory configuration.
```
1. Clone the Repository
```
Bash
git clone https://github.com/Yasaswini38/AI_Automation_MCP
cd ai_automation_mcp
```
2. Install Project Dependencies
Bash
pip install -r requirements.txt
```
3. Configure Credentials
Create a .env file in the root of the project directory to map your secure API endpoints:
```
Code snippet
OPENROUTER_API_KEY=your_openrouter_api_key_here
```
4. Launch the Live Streamlit Interface
Run the application execution script to bring up your live browser control hub:
```
Bash
streamlit run interface.py
```
Operational Capabilities Demonstrated Live
When you load or paste an email into the input console and trigger the pipeline, the engine performs three concurrent operational tasks natively:

Type-Safe Variable Mining: It instantly isolates the customer's legal name, reference/account keys, and processes a decimal-based numerical sentiment score.

Conditional Webhook Dispatch: If the system detects a Critical/High urgency score or filters the category to Billing, it automatically simulates a high-priority webhook alert to the team's #billing-alerts Slack communication channel. Normal inquiries pass smoothly to tracking logs with no system alarm overhead.

Agentic Writing Drafts: It crafts an empathetic, highly tailored response email contextually matching the customer's exact mood and problem metrics—allowing human support operators to simply hit "Review and Send."




