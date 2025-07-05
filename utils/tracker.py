import csv
import os
from datetime import datetime

def log_sent(recipient, success):
    file_exists = os.path.isfile("sent_log.csv")
    with open("sent_log.csv", "a", newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["email", "name", "status", "timestamp"])  # Write header once
        writer.writerow([
            recipient["email"],
            recipient.get("name", ""),
            "Success" if success else "Failed",
            datetime.now().isoformat()
        ])
