import os
import base64
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import (Mail, Attachment, FileContent, FileName, FileType, Disposition)

change_url = f"https://github.com/{os.environ.get('GITHUB_REPOSITORY')}/commit/{os.environ.get('COMMIT_HASH')}"
message = Mail(
    from_email=os.environ.get('FROM_EMAIL'),
    to_emails=os.environ.get('TO_EMAIL'),
    subject='Weekly Box Office update',
    html_content=f"""
    Weekly BoxOffice is updated. Content attached, changes can be found at <a href="https://www.boxofficemojo.com/weekly/?ref_=bo_nb_ml_secondarytab">Box Office Mojo</a>
    """)

# https://www.twilio.com/blog/sending-email-attachments-with-twilio-sendgrid-python
with open('WeeklyBoxoffice.csv', 'rb') as f:
    data = f.read()
    f.close()

encoded_file = base64.b64encode(data).decode()

attachedFile = Attachment(
    FileContent(encoded_file),
    FileName('WeeklyBoxoffice.csv'),
    FileType('text/csv'),
    Disposition('attachment')
)
message.attachment = attachedFile

try:
    sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e.message)