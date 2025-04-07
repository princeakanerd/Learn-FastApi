from fastapi import APIRouter
from models.note import Note
from fastapi import FastAPI,Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from config.db import conn
from fastapi.templating import Jinja2Templates
from typing import Union


from schemas.note import notesEntity , noteEntity

note = APIRouter()
templates = Jinja2Templates(directory="templates")

@note.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    docs = conn.notes.notes.find()
    newDocs = []
    for doc in docs:
        newDocs.append({
            "id" : doc["_id"] ,
            "note" : doc["note"]
        })
    return templates.TemplateResponse("index.html", {"request": request , "newDocs" : newDocs})

@note.post("/", response_class=HTMLResponse)
async def read_root(request: Request):
