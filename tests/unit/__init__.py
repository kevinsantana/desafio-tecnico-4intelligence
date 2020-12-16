from fastapi.testclient import TestClient

from cadastro_usuarios import app

client = TestClient(app)
