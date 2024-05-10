import json

from fastapi import APIRouter, Form, Request, responses, status
from fastapi.templating import Jinja2Templates
from pydantic.error_wrappers import ValidationError


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
):
    try:
        return responses.RedirectResponse(
            "/?alert=Successfully%20Registered", status_code=status.HTTP_302_FOUND
        )
    except ValidationError as e:
        errors = [item.get("loc")[0] + ": " + item.get("msg") for item in json.loads(e.json())]
        return templates.TemplateResponse(
            "auth/register.html", {"request": request, "errors": errors}
        )


@router.get("/login")
def login(request: Request):
    return templates.TemplateResponse("/login.html", {"request": request})


@router.post("/login")
def login(
    request: Request,
    email: str = Form(...),
    password: str = Form(...),
):
    response = responses.RedirectResponse(
        "/?alert=Successfully Logged In", status_code=status.HTTP_302_FOUND
    )
    return response
