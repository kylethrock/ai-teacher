from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os

app = FastAPI()

# For testing: allow your LMS origin and localhost. You can tighten later.
ALLOWED_ORIGINS = [
    "https://dva8iy6ikap1n.cloudfront.net",
    "http://localhost:5500",
    "http://127.0.0.1:5500",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

class TeacherReq(BaseModel):
    session_id: str | None = None
    text: str
    module_id: str | None = None

@app.get("/health")
def health():
    return {"ok": True}

@app.post("/teacher/respond")
def teacher_respond(req: TeacherReq):
    # Simple “teacher” response for test
    return {
        "session_id": req.session_id or "test-session",
        "speak_text": f"Teacher heard: '{req.text}'. Nice. Here's the next step.",
        "teacher_question": "Quick check: Name one way to prevent cross-contamination."
    }