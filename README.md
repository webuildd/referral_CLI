# 📬 Referral Email CLI Tool

A command-line tool that helps job seekers automate personalized referral email requests to company employees. It uses a common email template, reads recipient details from a CSV file, and sends emails directly through Gmail SMTP.

---

## ✨ Features

- Read employee details (name, email) from a CSV file  
- Personalize each email using a Jinja2 template  
- Load sensitive config from `.env` file (no hardcoding)  
- Preview emails before sending  
- Send emails using Gmail (App Password)  
- Log email status to `sent_log.csv`  

---

## ⚙️ Setup & Installation

### 1. Clone the Repository
```bash
git clone https://github.com/webuildd/referral_CLI
cd referral_CLI
```
### 2. Create and fill the ```.env``` file
```
SENDER_NAME=Your Name
SENDER_EMAIL=your_email@gmail.com
APP_PASSWORD=your_app_password
COMPANY=Google
ROLE=Frontend Developer
RESUME_LINK=https://yourdomain.com/resume.pdf
JOB_LINK=https://careers.google.com/job-id
PITCH=I'm excited about this role and believe my frontend skills align well.
EMAIL_LIST=data/employees.csv
```


### 3. Prepare ```data/employees.csv```

### 4. Prepare the email template in ```templates/referral_email.txt.j2```

---

## How to Use

#### Option 1: Manual run with ```main.py ```
```bash

# Create venv (optional)
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt  # or pip install jinja2 pyyaml python-dotenv

# Run the CLI tool
python main.py
```

#### Option 2: One-Click Setup using ```setup.sh```
```bash
chmod +x setup.sh
./setup.sh
```
This will:

- Set up a virtual environment
- Install dependencies
- Run the tool using main.py


---

## Security Tip
- Do NOT push .env, data/employees.csv, or sent_log.csv to GitHub

- Use Gmail App Password, not your main password

- Always check preview before sending






