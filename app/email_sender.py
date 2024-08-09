from aiosmtplib import SMTP
from email.message import EmailMessage

server_hostname = "127.0.0.1" 
server_port = 2525

async def send_email(from_email: str, to: str, subject: str, body: str):
    message = EmailMessage()
    message["From"] = from_email
    message["To"] = to
    message["Subject"] = subject
    message.set_content(body)

    async with SMTP(hostname=server_hostname, port=server_port) as smtp:
        # await smtp.starttls()
        # await smtp.login("your_email@example.com", "your_password")
        await smtp.send_message(message)
    return "Email sent successfully"
