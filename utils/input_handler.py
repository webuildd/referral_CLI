import csv

def get_recipients(config):
    path = config.get('email_list')
    recipients = []

    try:
        with open(path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                recipients.append({
                    'name': row.get('name', 'there'),
                    'email': row['email']
                })
    except Exception as e:
        print(f"Error reading CSV: {e}")
        exit(1)

    return recipients
