from gmail_reader import read_emails
from summarizer import summarize_email

emails = read_emails()

for index, email in enumerate(emails):

    print(f"\nEMAIL {index + 1}")
    print("-" * 50)

    summary = summarize_email(email)

    print(summary)
