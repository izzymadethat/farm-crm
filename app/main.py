from fastapi import FastAPI
from app.api import contacts_router
from app.db.session import Base, engine
    
app = FastAPI()

# Create tables
Base.metadata.create_all(bind=engine)

app.include_router(contacts_router, prefix="/api", tags=["Contacts"])

@app.get("/")
def index():
    return {"message": "Hello World"}


