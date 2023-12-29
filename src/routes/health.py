from fastapi import APIRouter, Request, HTTPException, status

health_router = APIRouter()

@health_router.get("/health")
async def health(request: Request):
    """The health endpoint"""

    app = request.app

    try:
      await app.db.admin.command('ping')
    except Exception as e:
        print(e)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Unable to ping mongo")

     

    try:
        await app.cache.ping()
    except Exception as e:
        print(e)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Unable to ping redis")
    
    return {"msg": "I am up and running."}
