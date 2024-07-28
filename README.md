# Email Generator and Verifier

## Overview
This project is a Python-based tool that generates realistic random email addresses and verifies their existence by checking MX records and attempting to connect to the SMTP server.

## Features
- Generates realistic random email addresses using common usernames and domains.
- Retrieves MX records for domains.
- Verifies email addresses by attempting to connect to their SMTP servers.

## Requirements
- Python 3.x
- smtplib
- dnspython

## Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/email-generator-verifier.git
    ```
2. Navigate to the project directory:
    ```sh
    cd email-generator-verifier
    ```
3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Usage
1. Update the script with the desired domain and number of emails to generate.
2. Run the script:
    ```sh
    python email_verifier.py
    ```
3. The script will generate random email addresses and verify them. Valid emails will be printed to the console.

## Code Structure
- `email_verifier.py`: The main script that generates and verifies email addresses.


## Acknowledgements
*This project uses the dnspython library for DNS record retrieval.


