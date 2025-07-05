import os
from dotenv import load_dotenv

def load_config(env_path=".env"):
    load_dotenv(env_path)

    config = {
        "sender_name": os.getenv("SENDER_NAME"),
        "sender_email": os.getenv("SENDER_EMAIL"),
        "app_password": os.getenv("APP_PASSWORD"),
        "company": os.getenv("COMPANY"),
        "role": os.getenv("ROLE"),
        "resume_link": os.getenv("RESUME_LINK"),
        "job_link": os.getenv("JOB_LINK"),
        "pitch": os.getenv("PITCH"),
        "email_list": os.getenv("EMAIL_LIST")
    }

    # Optional: Basic check for required values
    missing = [key for key, value in config.items() if not value]
    if missing:
        print(f"❌ Missing values in .env: {', '.join(missing)}")
        exit(1)

    return config
