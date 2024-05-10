from fastapi import FastAPI
from app.presentation.base_routes import router as base_router
from app.presentation.login_routes import router as login_router
from app.db.base import Base
from app.db.session import engine


def create_tables():
    Base.metadata.create_all(bind=engine)


def include_router(app):
    app.include_router(base_router, tags=["Home"])
    app.include_router(login_router, tags=["Authorization"])


def start_application():
    app = FastAPI()
    create_tables()
    include_router(app)
    return app


app = start_application()