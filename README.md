**EmailGenVerifier**

EmailGenVerifier is a Python tool designed to generate realistic random email addresses and verify their existence by connecting to SMTP servers. This can be useful for testing, validation, or other purposes where you need a list of valid email addresses.

**Features**

    Generate realistic random email addresses.
    Verify the existence of email addresses by checking their SMTP servers.
    Customizable for different domains and TLDs.

**Installation**

To use this tool, you need to have Python installed on your system. Additionally, install the required Python libraries:
    
    pip install dnspython

**Usage**

**Generating Random Emails**

The generate_random_email function creates a list of random email addresses using common usernames and the specified domain.

**Verifying Emails**

The verify_email function checks if an email address exists by connecting to its SMTP server and performing a mail transaction.
