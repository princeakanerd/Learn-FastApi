
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

app = FastAPI()

# Mount static files directory
app.mount("/static", StaticFiles(directory="static"), name="static")

# Load Jinja2 templates from the 'templates' directory
templates = Jinja2Templates(directory="templates")

conn = MongoClient(
    uri,
    server_api=ServerApi('1'),
    tls=True,
    tlsAllowInvalidCertificates=True,
    tlsAllowInvalidHostnames=True
)




