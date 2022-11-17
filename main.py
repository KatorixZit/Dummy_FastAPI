import uvicorn
from auth_routers import auth_router
from fastapi import FastAPI
from order_routers import order_router

app = FastAPI()

app.include_router(auth_router)
app.include_router(order_router)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
