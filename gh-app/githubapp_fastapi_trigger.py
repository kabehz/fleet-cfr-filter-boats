from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
import httpx
import jwt
import time
import os

app = FastAPI()

APP_ID = os.getenv("GITHUB_APP_ID")
INSTALLATION_ID = os.getenv("GITHUB_INSTALLATION_ID")
PRIVATE_KEY = os.getenv("GITHUB_PRIVATE_KEY").replace("\\n", "\n")

class FilterPayload(BaseModel):
    cfr_desde: str
    cfr_hasta: str
    estados: list[str]

def generate_jwt():
    payload = {
        "iat": int(time.time()) - 60,
        "exp": int(time.time()) + (10 * 60),
        "iss": APP_ID
    }
    return jwt.encode(payload, PRIVATE_KEY, algorithm="RS256")

async def get_installation_token(jwt_token):
    url = f"https://api.github.com/app/installations/{INSTALLATION_ID}/access_tokens"
    headers = {
        "Authorization": f"Bearer {jwt_token}",
        "Accept": "application/vnd.github+json"
    }
    async with httpx.AsyncClient() as client:
        res = await client.post(url, headers=headers)
    if res.status_code == 201:
        return res.json()["token"]
    else:
        raise HTTPException(status_code=500, detail=res.text)

@app.post("/trigger-filter/")
async def trigger_filter(payload: FilterPayload):
    jwt_token = generate_jwt()
    token = await get_installation_token(jwt_token)

    dispatch_url = "https://api.github.com/repos/tu-org/filtro-flota/actions/workflows/gh-actions-cfr-ci.yml/dispatches"
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json"
    }
    body = {
        "ref": "main",
        "inputs": {
            "cfr_desde": payload.cfr_desde,
            "cfr_hasta": payload.cfr_hasta
        }
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(dispatch_url, headers=headers, json=body)

    if response.status_code == 204:
        return {"status": "✅ Workflow activado con éxito"}
    else:
        raise HTTPException(status_code=500, detail=response.text)