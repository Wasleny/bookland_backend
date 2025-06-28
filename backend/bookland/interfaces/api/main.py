from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from contextlib import asynccontextmanager
from bookland.infra.database import init_db

from bookland.interfaces.api.routes.auth import auth_route
from bookland.interfaces.api.routes.admin import admin_user_route
from bookland.interfaces.api.openapi_tags import openapi_tags
from bookland.interfaces.api.routes.user import user_route


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield


app = FastAPI(
    lifespan=lifespan,
    title="Bookland API",
    description="API do Bookland utilizando Clean Architecture, FastAPI e MongoDB",
    version="1.0.0",
    contact={"name": "Wasleny Pimenta", "email": "pimenta.wasleny@gmail.com"},
    licence_info={"name": "MIT", "url": "https://opensource.org/licenses/MIT"},
    openapi_tags=openapi_tags,
)

app.include_router(auth_route.router, prefix="/auth", tags=["Auth"])
app.include_router(admin_user_route.router, prefix="/admin", tags=["Admin"])
app.include_router(user_route.router, prefix="/users", tags=["Users"])


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema

    openapi_schema = get_openapi(
        title=app.title,
        version=app.version,
        description=app.description,
        routes=app.routes,
    )

    openapi_schema["components"]["securitySchemes"] = {
        "HTTPBearer": {"type": "http", "scheme": "bearer"}
    }

    for path in openapi_schema["paths"].values():
        for method in path.values():
            method["security"] = [{"HTTPBearer": []}]

    app.openapi_schema = openapi_schema

    return openapi_schema


app.openapi = custom_openapi
