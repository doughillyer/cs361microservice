from fastapi import FastAPI
from pydantic import BaseModel
from .email_sender import send_email

app = FastAPI()

class EmailRequest(BaseModel):
    from_email: str
    to: str
    subject: str
    body: str

@app.post("/send-email/")
async def send_email_endpoint(email_request: EmailRequest):
    response = await send_email(email_request.from_email, email_request.to, email_request.subject, email_request.body)
    return {"message": response}