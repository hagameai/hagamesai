# HAGAME Backend

This is the backend for the HAGAME project, built with FastAPI.

## Environment Setup

1. Copy `.env.example` to `.env` and fill in your configuration:

```
cp .env.example .env
```

**Required variables:**
- `DATABASE_URL`: PostgreSQL async URL (e.g. `postgresql+asyncpg://user:password@localhost:5432/hagame_db`)
- `SECRET_KEY`: Secret key for JWT
- `ALGORITHM`: JWT algorithm (default: HS256)
- `ACCESS_TOKEN_EXPIRE_MINUTES`: JWT expiration in minutes (default: 60)

## Run locally

```bash
uvicorn main:app --reload
```

## Health Check

Visit [http://localhost:8000/](http://localhost:8000/) to verify the service is running. You should see `{ "status": "ok" }`.

## User Authentication & Profile Management

- **Registration:** `POST /auth/register` — Register a new user (username, email, password)
- **Login:** `POST /auth/login` — Obtain JWT access token
- **Get Current User:** `GET /auth/me` — Retrieve current user info (JWT required)
- **Profile:**
  - `GET /users/me/profile` — Get user profile
  - `PUT /users/me/profile` — Update user profile
- **Cognitive Profile:**
  - `GET /users/me/cognitive-profile` — Get cognitive profile
  - `PUT /users/me/cognitive-profile` — Update or create cognitive profile

All endpoints require JWT authentication except registration and login. See `/docs` for full OpenAPI documentation and example requests/responses.

### Logging & Error Handling
- All key actions (registration, login, profile access/update) are logged with timestamps and context.
- Consistent error responses and error logging for all HTTP errors.

---

## Game Core Framework

- **Game Definition:**
  - `GET /games/definitions` — List all game definitions
  - `POST /games/definitions` — Create a new game definition
  - `GET /games/definitions/{game_def_id}` — Get a game definition by ID
- **Game Instance:**
  - `POST /games/instances` — Create a new game instance
  - `GET /games/instances/{instance_id}` — Get a game instance by ID
  - `GET /games/my-instances` — List all game instances for the current user

All endpoints are async, use Pydantic schemas, and are protected by JWT where appropriate. See `/docs` for full OpenAPI documentation.

---

## AI Engine

- **AI Model Management:**
  - `GET /ai-models/` — List all AI models
  - `POST /ai-models/` — Create a new AI model
  - `GET /ai-models/{model_id}` — Get an AI model by ID

All endpoints are async, use Pydantic schemas, and are protected by JWT where appropriate. See `/docs` for full OpenAPI documentation.

---

## Next Steps
- Continue with the next module: **LLM Integration** (centralized LLM API, prompt management, error handling, etc.)