import pytest
from httpx import AsyncClient
from datetime import date

from bookland.domain.enums import UserGender
from bookland.interfaces.api.messages import user_messages
from bookland.settings import ADMIN_EMAIL, ADMIN_PASSWORD, ADMIN_NICKNAME


@pytest.mark.asyncio
async def test_register_and_login(client: AsyncClient):
    # auth/register -> success
    register_payload = {
        "name": "Test User",
        "nickname": "test_user",
        "email": "user@example.com",
        "password": "uSer@1234",
        "gender": UserGender.UNSPECIFIED,
        "birthdate": "2002-01-01",
    }

    response = await client.post("/auth/register", json=register_payload)

    assert response.status_code == 200

    data = response.json()

    assert "token" in data
    assert data["user"]["email"] == register_payload["email"]
    assert data["message"] == user_messages.REGISTER_USER_MESSAGE

    # auth/register -> fail
    response = await client.post("/auth/register", json=register_payload)

    assert response.status_code == 400

    # auth/login -> success
    login_payload = {
        "email": ADMIN_EMAIL,
        "password": ADMIN_PASSWORD,
    }

    response = await client.post("auth/login", json=login_payload)

    assert response.status_code == 200

    data = response.json()

    assert "token" in data
    assert data["user"]["nickname"] == ADMIN_NICKNAME

    token = data["token"]

    # auth/login -> fail
    login_payload = {
        "email": "invalid@email.com",
        "password": ADMIN_PASSWORD,
    }

    response = await client.post("auth/login", json=login_payload)

    assert response.status_code == 401

    # users/{user_id}
    protected_response = await client.get(
        f"/users/{data['user']['id']}", headers={"Authorization": f"Bearer {token}"}
    )

    assert protected_response.status_code == 200

    data = protected_response.json()

    assert data["user"]["email"] == ADMIN_EMAIL

    # admin/get-by-email
    protected_response = await client.get(
        "/admin/get-by-email",
        headers={"Authorization": f"Bearer {token}"},
        params={"email": ADMIN_EMAIL},
    )

    assert protected_response.status_code == 200

    data = protected_response.json()

    assert data["user"]["email"] == ADMIN_EMAIL

    # admin/get-by-role
    protected_response = await client.get(
        "/admin/get-by-role",
        headers={"Authorization": f"Bearer {token}"},
        params={"role": "user"},
    )

    assert protected_response.status_code == 200

    data = protected_response.json()

    assert len(data["users"]) == 1

    user_id = data["users"][0]["id"]

    # admin/promote-admin/{id} -> success
    protected_response = await client.patch(
        f"/admin/promote-admin/{user_id}", headers={"Authorization": f"Bearer {token}"}
    )

    assert protected_response.status_code == 200

    data = protected_response.json()

    assert data["user"]["email"] == "user@example.com"
    assert data["user"]["role"] == "admin"

    # admin/promote-admin/{id} -> fail
    protected_response = await client.patch(
        f"/admin/promote-admin/1", headers={"Authorization": f"Bearer {token}"}
    )

    assert protected_response.status_code == 404

    # admin/demote-admin/{id}
    protected_response = await client.patch(
        f"/admin/demote-admin/{user_id}", headers={"Authorization": f"Bearer {token}"}
    )

    assert protected_response.status_code == 200

    data = protected_response.json()

    assert data["user"]["email"] == "user@example.com"
    assert data["user"]["role"] == "user"
