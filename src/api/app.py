__all__ = ["app"]

from pathlib import Path
from typing import Annotated

from fastapi import FastAPI, Form, Request
from fastapi.templating import Jinja2Templates
from fastapi_swagger import patch_fastapi
from pydantic import BaseModel
from starlette.responses import HTMLResponse

import src.logging_  # noqa: F401
from src.api.chat import Message, chat_instance

app = FastAPI(
    title="Anonymous chat",
    swagger_ui_oauth2_redirect_url=None,
    docs_url=None,
    redoc_url=None,
)
patch_fastapi(app, redirect_from_root_to_docs=False)
this_file_path = __file__
templates_dir = Path(this_file_path).parent.parent / "templates"
templates = Jinja2Templates(directory=templates_dir)


class SendMessageForm(BaseModel):
    message: str


@app.post("/api/messages")
async def send_message(form: Annotated[SendMessageForm, Form()]) -> None:
    chat_instance.add_message(form.message)


@app.get("/api/messages")
async def get_all_messages() -> list[Message]:
    return [msg for msg in chat_instance.get_all_messages()]


@app.get("/api/messages/count")
async def message_count() -> int:
    return chat_instance.get_message_count()


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(request, name="index.html", context={})
