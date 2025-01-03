from fastapi import FastAPI
from .database import Base, engine
from .api import router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Social Media App",
    description="Engine Behind Social Media App.Ceated by Badal Kumar Paswan",
    version="1.O",
)
app.include_router(router)
