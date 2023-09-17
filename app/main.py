import os

from typing import Optional

from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

from app.common.logger import get_logger

app = FastAPI()

logger = get_logger(__name__)
parent_dir_path = os.path.dirname(os.path.realpath(__file__))

templates = Jinja2Templates(directory=parent_dir_path + "/templates")
app.mount('/static', StaticFiles(directory=(parent_dir_path + "/static")), name="static")


@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    logger.info(request)
    context = {'request': request}
    return templates.TemplateResponse("home.html", context)


@app.get("/summoner/", response_class=HTMLResponse)
def get_summoner(request: Request):
    logger.info(request)
    context = {'request': request}
    return templates.TemplateResponse("user.html", context)