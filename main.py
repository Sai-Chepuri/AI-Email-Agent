from gmail_reader import read_emails
from summarizer import summarize_email

emails = read_emails()

print("\n")
print("=" * 80)
print("Email Summarization Results")
print("=" * 80)

for index, email in enumerate(emails):

    print("\n")
    print("-" * 80)

    print(f"EMAIL - {index + 1}")

    print("-" * 80)

    print(f"\nSUBJECT:")
    print(email['subject'])

    print("\nSUMMARY:\n")

    summary = summarize_email(email['body'])

    print(summary)

    print("\n")
