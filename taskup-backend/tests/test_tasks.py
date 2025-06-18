import pytest
from app import create_app
from app.extensions import db
from app.models.task import Task
from app.config.test_config import TestConfig
import json


@pytest.fixture
def client():
    app = create_app()
    app = create_app()
    app.config.from_object(TestConfig)
    
    with app.test_client() as client:
        with app.app_context():
            db.create_all() #cria tabelas no banco de testes
            yield client
            
            db.session.remove()
            db.drop_all()   
            
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
    
#Get single task by ID 
def test_get_single_task(client):
    with client.application.app_context():
        task = Task(title = 'Get single task', description = 'Get single task description')
        db.session.add(task)
        db.session.commit()
        task_id = task.id
    response = client.get(f'/tasks/{task_id}')
    assert response.status_code == 200
    data = response.get_json()
    assert data['title'] == 'Get single task'
    
#UPDTATE TASK
def test_update_task(client):
    with client.application.app_context():
        task = Task(title = 'oLD tITLE ', description = 'oLD description')
        db.session.add(task)
        db.session.commit()
        task_id = task.id
    response = client.put(f'/tasks/{task_id}',json ={
        "title": "New title",
        "description": "New description",
        "completed": True
    })
    assert response.status_code == 200
    data = response.get_json()
    assert data['title'] == 'New title'
    assert data['description'] == 'New description'
    assert data['completed'] is True

#DELETE Task
def test_delete_task(client):
    with client.application.app_context():
        task = Task(title = 'To Delete')
        db.session.add(task)
        db.session.commit()
        task_id = task.id
        
    response = client.delete(f'/tasks/{task_id}')
    assert response.status_code == 200
    
    response = client.get(f'/tasks/{task_id}')
    assert response.status_code == 404


#Verifica se a API retorna erro se não tem o título na task
def test_create_task_missing_title(client):
    response = client.post("/tasks/", json={
        "description": "Missing title"
    })
    assert response.status_code == 400
    data = response.get_json()
    assert "error" in data