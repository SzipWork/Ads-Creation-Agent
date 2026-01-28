# Ad Creation Agent
This is an application that automates TikTok ad creation using AI-powered intent extraction and a structured workflow graph. The system processes user messages, extracts ad campaign parameters, validates business rules, and submits ads to the TikTok API.

## Architecture
The system follows a graph-based workflow using LangGraph:
```
User Request → Intent Extraction → OAuth Validation → Business Rules → Music Validation → Submission
```

## Key Components
- FastAPI Server (main.py)
- LangGraph Workflow (graph.py)
- State Management (state.py)
- Processing Nodes (nodes.py)
- LLM Integration (llm.py)
- Service Modules

## Features
- AI-Powered Ad Creation: Uses Gemini 2.5 Flash to extract campaign parameters from natural language
- OAuth Validation: Multiple OAuth token validation scenarios
- Business Rules Enforcement: Music requirements for Conversion campaigns
- Music Validation: Custom music ID validation
- Error Handling: Comprehensive error handling throughout the pipeline
- Structured Output: Consistent JSON responses with conversation history

## Installation
1. Clone the repository
2. Install dependencies:
```
pip install -r requirements.txt
```
3. Set up environment variables in a .env file:
```
GEMINI_API_KEY=your_gemini_api_key
TIKTOK_CLIENT_ID=your_tiktok_client_id
TIKTOK_CLIENT_SECRET=your_tiktok_client_secret
```
4. Run the application:
```
uvicorn app.main:app --reload
```


## Business Rules
- Music Requirement: Conversion campaigns require a valid music ID
- OAuth Validation: Multiple token validation scenarios (expired, missing scope, geo-blocked)
- Ad Text Length: Ad text is limited to 100 characters (enforced by LLM prompt)

## Error Scenarios Handled
- Invalid OAuth tokens (expired, missing scope, geo-restricted)
- Missing music ID for Conversion campaigns
- Invalid music IDs
- LLM generation failures
- TikTok API submission errors

## Project Structure
```
app/
├── config.py              # Environment configuration
├── llm.py                # Gemini LLM integration
├── main.py              # FastAPI application
├── schemas.py           # Pydantic schemas
├── graph/
│   ├── graph.py         # LangGraph workflow definition
│   ├── state.py         # State management
│   └── nodes.py         # Graph nodes implementation
├── services/
│   ├── oauth.py         # OAuth validation
│   ├── music.py         # Music handling
│   └── tiktok_api.py    # TikTok API integration
└── prompts/
    └── ad_agent_prompt.py # LLM prompts
```
