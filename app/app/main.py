import fastapi_plugins
from fastapi import FastAPI
from .utils import update_currencies_cache
from . import api
from .settings import settings
from .database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()
fastapi_plugins.register_middleware(app)


@app.on_event("startup")
async def on_startup() -> None:
    # initialize cache
    await fastapi_plugins.redis_plugin.init_app(app, config=settings)
    await fastapi_plugins.redis_plugin.init()

    # load currencies into cache
    await update_currencies_cache()


@app.on_event('shutdown')
async def on_shutdown() -> None:
    await fastapi_plugins.redis_plugin.terminate()

app.include_router(api.auth.router, prefix="/auth", tags=["auth"])
app.include_router(api.converter.router, prefix="/converter", tags=["converter"])
app.include_router(api.user.router, prefix="/users", tags=["users"])
