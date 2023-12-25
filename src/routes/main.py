from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def root():
    """The root endpoint"""
    return {"msg": "Hello, World!"}


@router.get("/health")
async def health():
    """The health endpoint"""
    return {"msg": "I am up and running."}
