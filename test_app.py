import os
import json
import pytest
from app import app as flask_app

@pytest.fixture
def client():
    flask_app.config["TESTING"] = True
    return flask_app.test_client()

def test_generar_excel(client):
    payload = {
        "desde": "ESP000000100",
        "hasta": "ESP000000150",
        "estado": ["Alta Definitiva"]
    }

    response = client.post("/generar", json=payload)
    assert response.status_code == 200
    data = response.get_json()
    assert data["success"] is True
    assert os.path.exists("output/resultado.xlsx")

def test_descargar_excel(client):
    response = client.get("/descargar")
    assert response.status_code == 200
    assert response.content_type == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
