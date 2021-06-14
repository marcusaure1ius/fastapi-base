import uvicorn

from .config.settings import settings


uvicorn.run(
    'base_api.app:app',
    host=settings.server_host,
    port=settings.server_port,
    reload=True
)