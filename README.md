# HAGAME

This is the backend for the HAGAME project, built with FastAPI. It provides a modular, scalable, and secure API for human-vs-AI game scenarios, advanced cognitive modeling, and LLM-powered services.

---

## Architecture & Technology Stack

- **Language:** Python 3.10+
- **Framework:** FastAPI (async, high performance, Pydantic validation)
- **Database:** PostgreSQL (with JSONB support)
- **Async ORM:** SQLAlchemy (async) or Tortoise ORM
- **Task Queue:** Celery (with Redis or RabbitMQ)
- **LLM SDKs:** OpenAI, Google AI
- **Cache:** Redis (for session, rate limit, and caching)
- **Containerization:** Docker, Docker Compose
- **Monitoring:** Prometheus, Grafana
- **Logging:** ELK Stack or Grafana Loki
- **Dependency Management:** [uv](https://github.com/astral-sh/uv) with `pyproject.toml`

---

## Environment Setup

1. Ensure you have Python 3.10+ installed.
2. Install dependencies using `uv`:

```bash
uv pip install -r pyproject.toml
```

3. Copy `.env.example` to `.env` and fill in your configuration:

```bash
cp .env.example .env
```

**Required variables:**
- `DATABASE_URL`: PostgreSQL async URL (e.g. `postgresql+asyncpg://user:password@localhost:5432/hagame_db`)
- `SECRET_KEY`: Secret key for JWT
- `ALGORITHM`: JWT algorithm (default: HS256)
- `ACCESS_TOKEN_EXPIRE_MINUTES`: JWT expiration in minutes (default: 60)

---

## Running the Application

```bash
uvicorn main:app --reload
```

Visit [http://localhost:8000/](http://localhost:8000/) for the health check (`{"status": "ok"}`) and [http://localhost:8000/docs](http://localhost:8000/docs) for the OpenAPI documentation.

---

## System Modules & API Overview

### 1. User Authentication & Profile Management
- **Purpose:** Secure user registration, login (JWT), and management of user profiles and cognitive profiles.
- **Key Endpoints:**
  - `POST /auth/register` — Register a new user
  - `POST /auth/login` — Obtain JWT access token
  - `GET /auth/me` — Retrieve current user info (JWT required)
  - `GET/PUT /users/me/profile` — Get or update user profile
  - `GET/PUT /users/me/cognitive-profile` — Get or update cognitive profile
- **Features:**
  - JWT-based authentication
  - Pydantic validation
  - Logging of all key actions
  - Consistent error handling

### 2. Game Core Framework
- **Purpose:** Define, manage, and run game definitions and instances, supporting plugin/strategy patterns for extensibility.
- **Key Endpoints:**
  - `GET/POST /games/definitions` — List or create game definitions
  - `GET /games/definitions/{game_def_id}` — Get a game definition by ID
  - `POST /games/instances` — Create a new game instance
  - `GET /games/instances/{instance_id}` — Get a game instance by ID
  - `GET /games/my-instances` — List all game instances for the current user
- **Features:**
  - Async endpoints
  - Pydantic schemas
  - JWT protection
  - Extensible game engine design

### 3. AI Engine
- **Purpose:** Provide adaptive prediction, cognitive modeling, quantum uncertainty, collective wisdom aggregation, and explainable AI (XAI) services.
- **Key Endpoints:**
  - `GET /ai-models/` — List all AI models
  - `POST /ai-models/` — Create a new AI model
  - `GET /ai-models/{model_id}` — Get an AI model by ID
- **Features:**
  - Modular AI engine (prediction, cognitive modeling, XAI, etc.)
  - Integration with LLMs for advanced reasoning and feedback

### 4. LLM Integration Service
- **Purpose:** Centralized gateway for all LLM API calls (OpenAI, Gemini, etc.), prompt management, and LLM call logging.
- **Key Endpoints:**
  - `POST /llm/call` — Call an LLM API
  - `GET /llm/logs` — List all LLM call logs for the current user
- **Features:**
  - Centralized API key management
  - Prompt versioning and management
  - Error handling and retries
  - Caching of LLM responses

### 5. Async Task Processing (Planned)
- **Purpose:** Offload long-running or resource-intensive operations to background tasks using Celery.
- **Planned Use Cases:**
  - AI model training and batch predictions
  - Cognitive profile analysis and updates
  - Generating detailed feedback reports
  - Long-running LLM interactions
  - Data aggregation and statistics
- **Integration:**
  - Celery with Redis or RabbitMQ as broker and backend
  - Task definitions in `tasks.py` (to be implemented)

### 6. Monitoring & Logging
- **Purpose:** Provide observability, performance monitoring, and structured logging for all modules.
- **Stack:**
  - **Monitoring:** Prometheus, Grafana
  - **Logging:** ELK Stack (Elasticsearch, Logstash, Kibana) or Grafana Loki
- **Features:**
  - Structured logging for all key actions and errors
  - Metrics for API performance and background tasks

---

## Data Models

The backend uses async ORM models (SQLAlchemy/Tortoise) with Pydantic schemas for validation. Key entities include:
- **User:** Authentication and profile data
- **CognitiveProfile:** Dynamic user cognitive modeling (JSONB)
- **GameDefinition:** Game rules, parameters, and configuration (JSONB)
- **GameInstance:** Game session state, status, and results (JSONB)
- **AIModel:** AI model configuration and metadata
- **UserDecisionLog:** User actions and context during games
- **Feedback:** System- or LLM-generated feedback for users

---

## Future Work

Planned features and modules (see `docs/roadmap.md` for details):
- Developer API/SDK
- Multimodal interaction support
- Emotion intelligence analysis
- Advanced AI model integration
- Federated learning support

---

## References
- [Project Roadmap](docs/roadmap.md)
- [OpenAPI Docs](http://localhost:8000/docs)

---

## License

This project is licensed under the **Apache License 2.0**. You are free to use, modify, and distribute this software under the terms of the license.

See the [LICENSE](LICENSE) file for the full license text and details.

For questions or contributions, please refer to the technical documentation and roadmap, and follow the project coding and architectural guidelines strictly.

