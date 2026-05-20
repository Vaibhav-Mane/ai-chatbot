from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
from app.routes.chat import router 
app = FastAPI()

app.include_router(router)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, workers=6, reload=True)
    
