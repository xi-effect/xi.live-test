from fastapi import FastAPI

from app.common.cors import CorrectCORSMiddleware
from app.routers import tokens_rst

app = FastAPI()

app.add_middleware(
    CorrectCORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(tokens_rst.router, prefix="/api/tokens")
