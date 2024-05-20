import uvicorn
from fastapi import FastAPI

from app.models.database import engine
from .models import core
from .api_v1 import router as router_v1

core.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(router=router_v1, prefix="/api/v1")

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)
