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


def read_emails():
    service = get_gmail_service()

    results = service.users().messages().list(
        userId='me',
        q='category:primary is:unread',
        maxResults=10
    ).execute()

    messages = results.get('messages', [])

    for message in messages:
        msg = service.users().messages().get(
            userId='me',
            id=message['id']
        ).execute()

        emails = []
        emails.append(msg['snippet'])
        return emails
