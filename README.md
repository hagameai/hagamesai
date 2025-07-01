# HAGAMEAI

HAGAMEAI is a training framework for AI game evolution. By constructing diverse game scenario components, from strategic confrontations to simulation, it enhances AI's learning mechanisms, decision-making processes, and its ability to collaborate or compete with humans in complex environments, providing foundational AI support for all game-related scenarios.

Experience AviaFlick, an ecological game based on HAGAMEAI, by visiting: [t.me/HAGAMEAI_CHANNEL](https://t.me/HAGAMEAI_CHANNEL)

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

# HAGAME AI Engine

HAGAME AI Engine is an advanced artificial intelligence system designed for game environments, providing adaptive learning, cognitive modeling, and strategic decision-making capabilities.

## Features

### AI Engine Components

1. **Adaptive Prediction Engine**
   - Real-time prediction of game states and player behavior
   - Adaptive learning from gameplay patterns
   - Multi-model prediction system with confidence scoring

2. **Cognitive Model Builder**
   - Player cognitive profile generation
   - Learning style analysis
   - Skill level assessment and tracking
   - Adaptability measurement

3. **Quantum Uncertainty Generator**
   - Quantum-inspired uncertainty modeling
   - Multi-dimensional uncertainty factors
   - Entanglement-based correlation analysis
   - Dynamic decoherence rate adjustment

4. **Collective Wisdom Aggregator**
   - Pattern recognition across game sessions
   - Strategy effectiveness analysis
   - Meta-learning from collective experiences
   - Trend and anomaly detection

5. **Explainable AI (XAI)**
   - Natural language explanations of AI decisions
   - Feature importance analysis
   - Counterfactual reasoning
   - Confidence level assessment

## Installation

1. Clone the repository:
```bash
git clone https://github.com/hagame/hagamesai.git
cd hagamesai
```

2. Create a virtual environment and activate it:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -e .
```

## Configuration

1. Create a `.env` file in the project root with the following variables:
```env
DATABASE_URL=postgresql+asyncpg://user:password@localhost/hagame
REDIS_URL=redis://localhost:6379/0
SECRET_KEY=your-secret-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

2. Initialize the database:
```bash
alembic upgrade head
```

## Usage

1. Start the API server:
```bash
uvicorn main:app --reload
```

2. Start the Celery worker:
```bash
celery -A core.celery_app worker --loglevel=info
```

## API Documentation

Once the server is running, access the API documentation at:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Development

### Project Structure

```
hagamesai/
├── alembic/              # Database migrations
├── api/                  # API routes and endpoints
├── core/                 # Core functionality
│   ├── ai_engine/        # AI Engine components
│   │   ├── base.py      # Base AI component class
│   │   ├── prediction.py # Adaptive Prediction Engine
│   │   ├── cognitive.py  # Cognitive Model Builder
│   │   ├── quantum.py    # Quantum Uncertainty Generator
│   │   ├── collective.py # Collective Wisdom Aggregator
│   │   └── xai.py       # Explainable AI
│   ├── auth.py          # Authentication
│   ├── config.py        # Configuration
│   └── database.py      # Database setup
├── crud/                 # Database operations
├── models/              # SQLAlchemy models
├── schemas/             # Pydantic schemas
└── tests/               # Test suite
```

### Running Tests

```bash
pytest
```

### Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- The HAGAME Team
- Contributors and maintainers
- The open-source community

## Contact

- Email: team@hagame.ai
- GitHub: [https://github.com/hagame/hagamesai](https://github.com/hagame/hagamesai)

