import pytest
from app import create_app
from app.extensions import db
from app.models.task import Task
import json


@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"  # banco em memória para testes
    
    with app.test_client() as client:
        with app.app_context():
            db.create_all() #cria tabelas no banco de testes
            yield client
def test_create_task(client):
    response = client.post("/tasks/", json={
        "title": "Test task",
        "description": "Test description"
    })
    assert response.status_code == 201
    data = response.get_json()
    assert data["title"] == "Test task"
    assert data["completed"] is False

def test_get_tasks(client):
    # Cria uma task para testar a listagem
    task = Task(title="Sample", description="Sample desc")
    with client.application.app_context():
        db.session.add(task)
        db.session.commit()
    
    response = client.get("/tasks/")
    assert response.status_code == 200
    data = response.get_json()
    assert len(data) == 1
    assert data[0]["title"] == "Sample"