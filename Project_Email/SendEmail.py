#This code is to send email in Python
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import getpass

emailadd = 'spokhriyal@plannet21.ie'
password = getpass.getpass()
s = smtplib.SMTP(host='p21-exch-2013.plannet21.ie', port=587)

s.starttls()
s.login(emailadd, password)

toemail = 'siddharth_hunt@yahoo.com'
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
