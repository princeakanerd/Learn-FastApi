from fastapi import FastAPI
from routes.note import note
from fastapi.staticfiles import StaticFiles
app = FastAPI()

# Mount static files directory
app.mount("/static", StaticFiles(directory="static"), name="static")

# Load Jinja2 templates from the 'templates' directory
app.include_router(note)
