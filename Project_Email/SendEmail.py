#This code is to send email in Python
#This is working code
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import getpass

emailadd = 'spokhriyal@plannet21.ie'
password = getpass.getpass()
s = smtplib.SMTP(host='xxxxxx', port=587) # xxx is your exchange server


s.starttls()
s.login(emailadd, password)

toemail = 'yyyyy'  # Enter recepient email here
msg = MIMEMultipart()
message = 'Good job Sid'
# setup the parameters of the message
msg['From']=emailadd
msg['To']=toemail
msg['Subject']="This is TEST"
# add in the message body
msg.attach(MIMEText(message, 'plain'))

s.send_message(msg)
s.quit()
