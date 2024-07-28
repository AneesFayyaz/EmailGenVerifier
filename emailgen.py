import random
import string
import smtplib
import dns.resolver

# Lists of common usernames, domains, and TLDs for realistic email generation
usernames = ['anees', 'fayyaz', 'mubashir', 'nazeer', 'nazeeer', 'zaini', 'awan', 'arbaz', 'khan']
domains = ['gmail.com', 'yahoo.com', 'outlook.com', 'example.com', 'mail.com', 'hotmail.com', 'aol.com', 'icloud.com']
tlds = ['com', 'net', 'org', 'info', 'biz', 'us', 'co', 'ca', 'uk']

def generate_random_username():
    """Generate a realistic random username."""
    prefix = random.choice(usernames)
    suffix = ''.join(random.choices(string.digits, k=random.randint(1, 3)))
    return f"{prefix}{suffix}"

def generate_random_email(domain, num_emails=1):
    """Generate realistic random email addresses using the given domain."""
    emails = []
    for _ in range(num_emails):
        username = generate_random_username()
        tld = random.choice(tlds)
        email = f"{username}@{domain}"
        emails.append(email)
    return emails

def get_mx_record(domain):
    """Retrieve the MX record for a given domain."""
    try:
        records = dns.resolver.resolve(domain, 'MX')
        return records[0].exchange.to_text()
    except:
        return None

def verify_email(email):
    """Verify if an email address exists by attempting to connect to its SMTP server."""
    domain = email.split('@')[1]
    mx_record = get_mx_record(domain)
    if not mx_record:
        return False

    try:
        server = smtplib.SMTP()
        server.set_debuglevel(0)
        server.connect(mx_record)
        server.helo('gmail.com')
        server.mail('test@gmail.com')
        code, message = server.rcpt(email)
        server.quit()

        return code == 250
    except:
        return False

# Example usage
domain = "gmail.com"
num_emails = 10
random_emails = generate_random_email(domain, num_emails)

valid_emails = []
for email in random_emails:
    if verify_email(email):
        valid_emails.append(email)

print("Valid emails:")
for email in valid_emails:
    print(email)