import pytest
from httpx import AsyncClient

from bookland.interfaces.api.messages import author_messages
from bookland.settings import ADMIN_EMAIL, ADMIN_PASSWORD


@pytest.mark.asyncio
async def test_register_and_login(client: AsyncClient):
    # login como admin padrão
    login_payload = {
        "email": ADMIN_EMAIL,
        "password": ADMIN_PASSWORD,
    }
    response = await client.post("auth/login", json=login_payload)
    token = response.json()["token"]

    # criar autor
    author_payload = {"name": "Machado de Assi", "nationality": "Brasil"}
    admin_response = await client.post(
        "/admin/authors/",
        headers={"Authorization": f"Bearer {token}"},
        json=author_payload,
    )

    assert admin_response.status_code == 200

    data = admin_response.json()

    assert data["author"]["name"] == author_payload["name"]

    author_id = data["author"]["id"]

    # pegar autor por id
    admin_response = await client.get(
        f"/admin/authors/{author_id}",
        headers={"Authorization": f"Bearer {token}"},
    )

    assert admin_response.status_code == 200

    data = admin_response.json()

    assert data["author"]["name"] == author_payload["name"]

    # pegar autor por id - não encontrar
    admin_response = await client.get(
        f"/admin/authors/1",
        headers={"Authorization": f"Bearer {token}"},
    )

    assert admin_response.status_code == 404

    # pegar todos os autores
    admin_response = await client.get(
        f"/admin/authors/",
        headers={"Authorization": f"Bearer {token}"},
    )

    assert admin_response.status_code == 200

    data = admin_response.json()

    assert len(data["authors"]) == 1

    # atualizar autor
    author_payload["name"] = "Machado de Assis"
    admin_response = await client.patch(
        f"/admin/authors/{author_id}",
        headers={"Authorization": f"Bearer {token}"},
        json=author_payload,
    )

    assert admin_response.status_code == 200

    data = admin_response.json()

    assert data["author"]["name"] == author_payload["name"]

    # excluir autor
    admin_response = await client.delete(
        f"/admin/authors/{author_id}", headers={"Authorization": f"Bearer {token}"}
    )

    assert admin_response.status_code == 200
