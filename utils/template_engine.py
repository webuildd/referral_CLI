from jinja2 import Environment, FileSystemLoader

def render_email(config, recipient):
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template('referral_email.txt.j2')
    
    body = template.render(
        name=recipient.get("name", "there"),
        company=config["company"],
        role=config["role"],
        resume_link=config["resume_link"],
        job_link=config["job_link"],
        pitch=config["pitch"],
        sender_name=config["sender_name"]
    )

    subject_line = f"Referral Request for {config['role']} at {config['company']}"
    return subject_line, body
