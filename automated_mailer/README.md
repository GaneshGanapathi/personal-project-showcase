# Automated Bulk Email Sender

A simple Python script to send personalized bulk emails using Gmail and a CSV contact list.

## Prerequisites

1.  **Python 3.11**
2.  **Pandas Library:**
    ```bash
    pip install pandas email 
    ```

## Setup & Configuration

1.  **Prepare the Data:**  
    Create a file named `email.csv` in the same directory as the script. It must contain the headers `name` and `email`.
    
    *Example `email.csv`:*
    ```csv
    name,email
    John Doe,john@example.com
    Jane Smith,jane@test.com
    ```

2.  **Configure Credentials:**  
    Open the Python script and update the following variables:
    ```python
    frm_addr = "your_email@gmail.com"
    password = "your_app_password" 
    ```

    > **⚠️ Important for Gmail:** Do not use your standard login password. You must generate an **App Password** from your Google Account settings (Security > 2-Step Verification > App passwords) to allow this script to log in.

## Usage

Run the script from your terminal:

```bash
python main.py
