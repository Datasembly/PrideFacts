from __future__ import print_function
import os.path
import random
from googleapiclient.discovery import build # Make sure this is installed.
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

# Constants for convenience.
# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
# The sheet we're pulling facts from. This is the id.
pridefacts_data = '1_9G6G8HdTzZkdBBZNolHH0j23c1qIrhhiiTSYvmsUpw'


# Set up with the assumption that facts will always b e in column A.
# Is set up so that we can categorize facts by sheets if wanted in the future
# Always return a random fact though.
def random_fact(service, facttype="Sheet1"):
    # facttype chooses which sheet to reference from
    facts = '{}!A:A'.format(facttype)
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=pridefacts_data,
                                range=facts).execute()
    values = result.get('values', [])
    return random.choice(values)[0]


# Abstraction to create a service connector to Google services
# This is just code from the quickstart code example
def make_service():
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
        # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    service = build('sheets', 'v4', credentials=creds)
    return service


# The main function actually creates the service and then uses it to find a random fact.
def main():
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    service = make_service()
    return random_fact(service)


# Easy debugs
if __name__ == '__main__':
    print(main())
