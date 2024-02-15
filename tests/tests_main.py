from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_create_medication_request():
    response = client.post("/services_requests/", json={"2024-02-15"})
    assert response.status_code == 200
    assert "id" in response.json()


def test_get_medication_requests():
    response = client.get("/services_requests/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_single_medication_request():
    response = client.get("/services_requests/1")
    assert response.status_code == 200
    assert "id" in response.json()


def test_update_medication_request():
    # Create a medication request first
    create_response = client.post("/services_requests/", json={"2024-02-15"})
    request_id = create_response.json()["id"]

    # Update the created medication request
    update_response = client.patch(f"/services_requests/{request_id}", json={"2024-02-20"})
    assert update_response.status_code == 200
    assert "id" in update_response.json()
