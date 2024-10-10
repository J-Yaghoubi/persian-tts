from fastapi import FastAPI

from app.routes.tts import router as tts_router

app = FastAPI(
    title="Persian Text-to-Speech API",
    description="API to convert Persian text into speech",
    version="1.0.0",
)


app.include_router(tts_router)
