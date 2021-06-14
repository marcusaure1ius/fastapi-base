from fastapi import FastAPI

from . import endpoints

tags_metadata = [
    {
        'name': 'User',
        'description': 'User endpoints section'
    },
    {
        'name': 'Item',
        'description': 'Item endpoints section'
    }
]

app = FastAPI(
    title='Base API',
    description='This is base realization of fastapi framework',
    version='1.0.0',
    openapi_tags=tags_metadata,
    docs_url='/swagger'
)

app.include_router(endpoints.router)