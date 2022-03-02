import pickle
import os.path
from apiclient import errors
import email
from email.mime.text import MIMEText
import html2text
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import base64
from base64 import urlsafe_b64encode
from mimetypes import guess_type as guess_mime_type
from bs4 import BeautifulSoup
  

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly','https://www.googleapis.com/auth/gmail.send']

def sent_mails(service,user_id):
    sent_ids = service.users().messages().list(userId='me', labelIds='SENT').execute()
    messages = sent_ids.get('messages', [])
    list_ids=[]
    if not messages:
        return list_ids
    else:
        for i in messages:
            list_ids.append(i['id'])
        return list_ids

def search_message(service, user_id, search_string):
    try:
        # initiate the list for returning
        list_ids = []

        # get the id of all messages that are in the search string
        search_ids = service.users().messages().list(userId='me', q=search_string).execute()
        
        
        # if there were no results, print warning and return empty string
        try:
            ids = search_ids['messages']

        except KeyError:
            print("WARNING: the search queried returned 0 results")
            print("returning an empty string")
            return ""

        if len(ids)>1:
            for msg_id in ids:
                list_ids.append(msg_id['id'])
            return(list_ids)

        else:
            list_ids.append(ids['id'])
            return list_ids
        
    except (errors.HttpError, error):
        print("An error occured: %s") % error


def get_message(service, user_id, msg_id):
    if(msg_id=='0'):
        return "No data"
    try:
        # grab the message instance
        message = service.users().messages().get(userId='me', id=msg_id,format='raw').execute()

        # decode the raw string, ASCII works pretty well here
        msg_str = base64.urlsafe_b64decode(message['raw'].encode('ASCII'))

        # grab the string from the byte object
        mime_msg = email.message_from_bytes(msg_str)

        # check if the content is multipart (it usually is)
        content_type = mime_msg.get_content_maintype()
        if content_type == 'multipart':
            # there will usually be 2 parts the first will be the body in text
            # the second will be the text in html
            parts = mime_msg.get_payload()

            # return the encoded text
            #temp=html2text.html2text(parts[1].get_payload())
            final_content2 = parts[0].get_payload()
            final_content = parts[1].get_payload()

            return final_content2

        elif content_type == 'text':
            return mime_msg.get_payload()

        else:
            return ""
            print("\nMessage is not text or multipart, returned an empty string")
    # unsure why the usual exception doesn't work in this case, but 
    # having a standard Exception seems to do the trick
    except Exception:
        print("An error occured: %s") % error

def get_message_details(service, user_id, msg_id):
    
    if(msg_id=='0'):
        returning={"subject":"", "from":"","to":""}
        return returning
    try:
        # grab the message instance
        message = service.users().messages().get(userId='me', id=msg_id,format='full').execute()
        payload = message['payload']
        headers = payload.get("headers")
        parts = payload.get("parts")
        returning={"subject":"No Subject", "from":"Unknown","to":"Unknown" }
        for i in headers:
            if(i['name']=='From' or i['name']=='from'):
                returning["from"]=i['value']
            if(i['name']=='Subject' or i['name']=='subject'):
                if(i['value']==""):
                    i['value']="No Subject"
                returning["subject"]=i['value']
            if(i['name']=='To' or i['name']=='to'):
                returning["to"]=i['value']


        return returning   
    except Exception:
        print("An error occured: %s") % error

def get_inbox(service):
    results = service.users().messages().list(userId='me').execute()
    messages = results.get('messages', [])
    list_ids=[]
    if not messages:
        print('No messages found.')
        return list_ids
    else:
        for i in messages:
            list_ids.append(i['id'])
        return list_ids

def exp(service, ID):
    if(ID=='0'):
        return "No data"
    msg = service.users().messages().get(userId='me', id=ID).execute()
    if msg.get("payload").get("body").get("data"):
        return base64.urlsafe_b64decode(msg.get("payload").get("body").get("data").encode("ASCII")).decode("utf-8")
    return msg.get("snippet")

def message_details(service, msg_id):
    if(msg_id=='0'):
        returning={"subject":"No data", "from":"No data", "date":"No data" }
        return returning
    try:
        # grab the message instance
        message = service.users().messages().get(userId='me', id=msg_id,format='full').execute()
        payload = message['payload']
        headers = payload.get("headers")
        returning={"subject":"No Subject", "from":"Unknown", "date":"Someday" }
        for i in headers:
            if(i['name']=='Date'):
                returning["date"]=i['value']
            if(i['name']=='From'):
                returning["from"]=i['value']
            if(i['name']=='Subject'):
                if(i['value']==""):
                    i['value']="No Subject"
                returning["subject"]=i['value']


        return returning   
    except Exception:
        print("An error occured: %s") % error 

def add_attachment(message, filename):
    content_type, encoding = guess_mime_type(filename)
    if content_type is None or encoding is not None:
        content_type = 'application/octet-stream'
    main_type, sub_type = content_type.split('/', 1)
    if main_type == 'text':
        fp = open(filename, 'rb')
        msg = MIMEText(fp.read().decode(), _subtype=sub_type)
        fp.close()
    elif main_type == 'image':
        fp = open(filename, 'rb')
        msg = MIMEImage(fp.read(), _subtype=sub_type)
        fp.close()
    elif main_type == 'audio':
        fp = open(filename, 'rb')
        msg = MIMEAudio(fp.read(), _subtype=sub_type)
        fp.close()
    else:
        fp = open(filename, 'rb')
        msg = MIMEBase(main_type, sub_type)
        msg.set_payload(fp.read())
        fp.close()
    filename = os.path.basename(filename)
    msg.add_header('Content-Disposition', 'attachment', filename=filename)
    message.attach(msg)

def build_message(destination, obj, body, attachments):
    if not attachments: # no attachments given
        message = MIMEText(body)
        message['to'] = destination
        message['from'] = 'me'
        message['subject'] = obj
    else:
        message = MIMEMultipart()
        message['to'] = destination
        message['from'] = 'me'
        message['subject'] = obj
        message.attach(MIMEText(body))
        for filename in attachments:
            add_attachment(message, filename)
    return {'raw': urlsafe_b64encode(message.as_bytes()).decode()}    

def send_message(service, destination, obj, body, attachments):
    return service.users().messages().send(
      userId="me",
      body=build_message(destination, obj, body, attachments)
    ).execute()

def read_message(service, user_id, msg_id):
    
    if(msg_id=='0'):
        return "No data"
    # Get value of 'payload' from dictionary 'txt'
    message = service.users().messages().get(userId='me', id=msg_id,format='full').execute()
    payload = message['payload']
    headers = payload['headers']

    # Look for Subject and Sender Email in the headers
    for d in headers:
        if d['name'] == 'Subject':
            subject = d['value']
        if d['name'] == 'From':
            sender = d['value']

    # The Body of the message is in Encrypted format. So, we have to decode it.
    # Get the data and decode it with base 64 decoder.
    parts = payload.get('parts')[0]
    data = parts['body']['data']
    data = data.replace("-","+").replace("_","/")
    decoded_data = base64.b64decode(data)

    # Now, the data obtained is in lxml. So, we will parse 
    # it with BeautifulSoup library
    soup = BeautifulSoup(decoded_data , "lxml")
    body = soup.body()

    # Printing the subject, sender's email and message
    return body
    

def main():
    
    creds = None

    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)

    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)

        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)


    service = build('gmail', 'v1', credentials=creds)
    return service