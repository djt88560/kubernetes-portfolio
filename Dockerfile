FROM python:3.12-slim-bookworm

WORKDIR /app

COPY pyproject.toml uv.lock ./

RUN pip install uv \
 && uv venv /app/.venv \
 && uv sync --frozen

ENV PATH="/app/.venv/bin:$PATH"

COPY Backend Backend

RUN useradd -m app && chown -R app:app /app
USER app

CMD ["uvicorn", "Backend.main:app", "--host", "0.0.0.0", "--port", "8000"]