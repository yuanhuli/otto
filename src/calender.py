import datetime as dt
import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ["https://www.googleapis.com/auth/calendar"]

def main():
    creds = None
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json")
    
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)
        with open("token.json", "w") as token:
            token.write(creds.to_json())
    
    try:
        service = build("calendar", "v3", credentials=creds)
        
        event = {
           "summary": "My python event",
           "location": "Somewhere Online",
           "description": "Some more details",
           "colorId": 6,
           "start":{
               "dateTime": "2024-03-18T09:00:00",
               "timeZone": "America/New_York"
           },
           "end":{
               "dateTime": "2024-03-18T17:00:00",
               "timeZone": "America/New_York"
           },
           "recurrence": [
               "RRULE:FREQ=DAILY;COUNT=3"
           ],
        }
        
        event = service.events().insert(calendarId="primary", body=event).execute()
        print(f"Event created: {event.get('htmlLink')}")
            
    except HttpError as error:
        print("An error occurred:", error)

if __name__ == "__main__":
    main()
