from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import base64

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']


def get_gmail_service():
    flow = InstalledAppFlow.from_client_secrets_file(
        'credentials.json',
        SCOPES
    )

    creds = flow.run_local_server(port=0)

    service = build('gmail', 'v1', credentials=creds)

    return service


def extract_email_body(payload):

    if 'parts' in payload:
        for part in payload['parts']:
            mime_type = part.get('mimeType')
            data = part.get('body', {}).get('data')

            if mime_type == 'text/plain' and data:
                text = base64.urlsafe_b64decode(
                    data
                ).decode('utf-8', errors='ignore')
                return text

    data = payload.get('body', {}).get('data')

    if data:
        text = base64.urlsafe_b64decode(
            data
        ).decode('utf-8', errors='ignore')
        return text

    return ""


def read_emails():
    service = get_gmail_service()

    results = service.users().messages().list(
        userId='me',
        q='category:primary is:unread',
        maxResults=5
    ).execute()

    messages = results.get('messages', [])
    emails = []

    for message in messages:
        msg = service.users().messages().get(
            userId='me',
            id=message['id']
        ).execute()

        payload = msg.get('payload', {})
        headers = payload.get('headers', [])

        subject = ""
        sender = ""

        for header in headers:

            if header['name'] == 'Subject':
                subject = header['value']

            if header['name'] == 'From':
                sender = header['value']

        body = extract_email_body(payload)

        emails.append({
            "sender": sender,
            "subject": subject,
            "body": body
        })

    return emails
