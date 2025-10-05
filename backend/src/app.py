from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI(title="Ai Aipplication",version="1.0.0")

app.add_middleware(CORSMiddleware,allow_origins=["*"],allow_credentials=True)
