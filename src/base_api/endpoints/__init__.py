from fastapi import APIRouter

from . import user_endpoints

router = APIRouter()
router.include_router(user_endpoints.router)