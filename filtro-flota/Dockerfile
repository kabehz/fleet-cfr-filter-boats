FROM python:3.11-slim

WORKDIR /app
COPY . .

RUN pip install --no-cache-dir fastapi uvicorn httpx python-jose[cryptography] pydantic

ENV PYTHONUNBUFFERED=1

CMD ["uvicorn", "githubapp_fastapi_trigger:app", "--host", "0.0.0.0", "--port", "8080"]