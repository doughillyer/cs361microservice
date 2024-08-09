import requests

def send_email(to, subject, body):
    url = "http://127.0.0.1:8000/send-email/"
    payload = {
        "from_email": "newsletter@yourdomain.com",  # The sender email address
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
