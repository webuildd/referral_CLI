import argparse
from utils.config_loader import load_config
from utils.email_sender import send_email
from utils.template_engine import render_email
from utils.tracker import log_sent
from utils.preview import preview_emails
from utils.input_handler import get_recipients

def main():
    print("🔧 Loading configuration from .env file...")
    config = load_config()
    recipients = get_recipients(config)

    print("\n--- Preview Mode ---")
    preview_emails(config, recipients)
    confirm = input("\nDo you want to send these emails? (y/n): ")

    if confirm.lower() != 'y':
        print("Aborted.")
        return

    for recipient in recipients:
        try:
            subject, body = render_email(config, recipient)
            success = send_email(config, recipient['email'], subject, body)
        except Exception as e:
            print(f"Error sending to {recipient['email']}: {e}")
            success = False

        log_sent(recipient, success)

    print("\nAll emails processed. Check sent_log.csv for status.")
    print(f"Total attempted: {len(recipients)}")

if __name__ == "__main__":
    main()
