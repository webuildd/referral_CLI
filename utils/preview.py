from utils.template_engine import render_email

def preview_emails(config, recipients):
    print("\n--- Email Previews ---\n")
    for recipient in recipients:
        subject, body = render_email(config, recipient)
        print(f"To: {recipient['email']}")
        print(f"{body}\n{'-'*60}\n")
