# Email Notification Microservice

## Overview
This microservice allows users to send email notifications. It is designed to be integrated into other applications to provide email sending capabilities.

## How to Request Data from the Microservice

To request data from the microservice, you need to make an HTTP POST request to the `/send-email/` endpoint. The request should include the following JSON payload:

```json
{
    "from_email": "newsletter@yourdomain.com",
    "to": "recipient@example.com",
    "subject": "Email Subject",
    "body": "Email Body"
}


Example Request

Here is an example of how to make a request using Python's requests library:

import requests

def send_email(to, subject, body):
    url = "http://localhost:2525/send-email/"
    payload = {
        "from_email": "newsletter@yourdomain.com",
        "to": to,
        "subject": subject,
        "body": body
    }
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(url, json=payload, headers=headers)
    return response.json()

response = send_email("test@example.com", "Test Subject", "Test Body")
print(response)

How to Receive Data from the Microservice

The response from the microservice will be a JSON object. If the email is sent successfully, the response will include a message confirming the successful sending of the email.

Example Response
{
    "message": "Email sent successfully"
}


Communication Contract

    Endpoint: /send-email/
    Method: POST
    Request Payload:
        from_email (string): The email address of the sender.
        to (string): The email address of the recipient.
        subject (string): The subject of the email.
        body (string): The body content of the email.
    Response:
        message (string): A confirmation message indicating the email was sent successfully.


Running the Microservice

pip install -r requirements.txt
uvicorn app.email_sender:app --host 0.0.0.0 --port 2525


Example CLI Test Program

import requests

def send_email(to, subject, body):
    url = "http://localhost:2525/send-email/"
    payload = {
        "from_email": "newsletter@yourdomain.com",
        "to": to,
        "subject": subject,
        "body": body
    }
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(url, json=payload, headers=headers)
    return response.json()

def main():
    print("Welcome to the Newsletter Signup CLI")
    email = input("Please enter your email address to sign up: ")
    
    subject = "Welcome to our Newsletter!"
    body = "Thank you for signing up for our newsletter. Stay tuned for updates."
    
    response = send_email(email, subject, body)
    
    if response.get("message") == "Email sent successfully":
        print("Confirmation: Your email was successfully sent!")
    else:
        print("Error: There was a problem sending your email.")

if __name__ == "__main__":
    main()



