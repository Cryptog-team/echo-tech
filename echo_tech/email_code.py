import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders





def send_email(filename):
    sender="echotech2022@gmail.com"  #sender gmail address
    reciever = input("Enter reciver gmail address")  #reciver gmail address
    msg=MIMEMultipart()
    msg['From']=sender
    msg['To']=reciever
    msg['Subject']="Warning This Is Echo-Tech"
    body="sent from Echo-Team"
    msg.attach(MIMEText(body,'plain'))
    attachment_file = input('Enter the attachment_file path : ')
    attachment=open(attachment_file,"rb") #attachment folder
    p=MIMEBase('application','octet-stream')
    p.set_payload((attachment).read())
    encoders.encode_base64(p)
    p.add_header('Content-Disposition',"attachment; filename=%s"%filename)
    msg.attach(p)
    s=smtplib.SMTP('smtp.gmail.com',587)
    s.starttls()
    s.login(sender,"Echoteam2020") #enter sender gmail password here
    text=msg.as_string()
    s.sendmail(sender,reciever,text)
    s.quit()