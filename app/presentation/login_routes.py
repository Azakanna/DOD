import json

from fastapi import APIRouter, Depends, Form, Request, responses, status
from fastapi.templating import Jinja2Templates
from pydantic.error_wrappers import ValidationError
from sqlalchemy.orm import Session

from app.application.schemas import UserCreate
from app.db.crud import authenticate_user, create_new_user, get_users
from app.db.session import get_db


templates = Jinja2Templates(directory="app/templates")
router = APIRouter()


@router.get("/register")
def register(request: Request):
    return templates.TemplateResponse("/register.html", {"request": request})


@router.post("/register")
def register(
    request: Request,
    email: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db),
):
    try:
        user = UserCreate(email=email, password=password)
        create_new_user(user=user, db=db)
        return responses.RedirectResponse(
            "/?alert=Successfully%20Registered", status_code=status.HTTP_302_FOUND
        )
    except ValidationError as e:
        errors = [item.get("loc")[0] + ": " + item.get("msg") for item in json.loads(e.json())]
        return templates.TemplateResponse(
            "register.html", {"request": request, "errors": errors}
        )


@router.get("/login")
def login(request: Request):
    return templates.TemplateResponse("/login.html", {"request": request})


@router.post("/login")
def login(
    request: Request,
    email: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db),
):
    errors = []
    user = authenticate_user(email=email, password=password, db=db)
    if not user:
        errors.append("Incorrect email or password")
        return templates.TemplateResponse(
            "login.html", {"request": request, "errors": errors}
        )

    return responses.RedirectResponse(
        "/?alert=Successfully Logged In", status_code=status.HTTP_302_FOUND
    )

@router.get("/users")
def users(db: Session = Depends(get_db)):
    return get_users(db)