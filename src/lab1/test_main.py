from fastapi.testclient import TestClient

from .main import app

client = TestClient(app)


def test_read_items():
    response = client.get("/items/")
    assert response.status_code == 200
    assert response.json() == {
        "Test": {
            "id": "Test",
            "title": "Title",
            "description": "Description",
        }
    }


def test_read_item():
    response = client.get("/items/Test")
    assert response.status_code == 200
    assert response.json() == {
        "id": "Test",
        "title": "Title",
        "description": "Description",
    }
    

def test_read_nonexistent_item():
    response = client.get("/items/wat")
    assert response.status_code == 404
    assert response.json() == {"detail": "Item not found"}
    

def test_create_item():
    response = client.post(
        "/items/",
        json={
            "id": "Item",
            "title": "Cool Item", 
            "description": "Cool Item Description"
        },
    )
    assert response.status_code == 200
    assert response.json() == {
        "id": "Item",
        "title": "Cool Item",
        "description": "Cool Item Description",
    }


def test_create_existing_item():
    response = client.post(
        "/items/",
        json={
            "id": "Test",
            "title": "Title",
            "description": "Description",
        },
    )
    assert response.status_code == 409
    assert response.json() == {"detail": "Item already exists"}


def test_update_item():
    response = client.put(
        "/items/Test",
        json={
            "id": "Test",
            "title": "Testitle",
            "description": "Testescripion",
        },
    )
    assert response.status_code == 200
    assert response.json() == {
        "id": "Test",
        "title": "Testitle",
        "description": "Testescripion",
    }


def test_update_nonexistent_item():
    response = client.put(
        "/items/wat",
        json={
            "id": "Wat",
            "title": "Wat",
            "description": "Wat",
        },
    )
    assert response.status_code == 404
    assert response.json() == {"detail": "Item not found"}

def test_delete_item():
    response = client.delete("/items/Test")
    assert response.status_code == 200
    assert response.json() == None

def test_delete_nonexistent_item():
    response = client.delete("/items/wat")
    assert response.status_code == 404
    assert response.json() == {"detail": "Item not found"}
