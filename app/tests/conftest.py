import pytest
from fastapi.testclient import TestClient
from pathlib import Path
import sys

# Garante que o diretório raiz do projeto esteja no sys.path
PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from app.main import app

@pytest.fixture
def client():
    return TestClient(app)
