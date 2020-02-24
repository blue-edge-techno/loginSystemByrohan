import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def send_mail(toaddr,message,sub):
    try:
        msg = MIMEMultipart()

        fromaddr = "gooogleincoporation@gmail.com"

        msg['From']=fromaddr
        msg['To']= toaddr
        msg['Subject']=sub

        msg.attach(MIMEText(message, 'plain'))

        s = smtplib.SMTP('smtp.gmail.com', 587)

        s.starttls()

        s.login(fromaddr, "maths1729")

        text = msg.as_string()

        s.sendmail(fromaddr, toaddr, text)
        s.quit()
        return True

    except:
        return False

if __name__ == '__main__':
    print(send_mail("rohangupta1176@gmail.com","This thing works","RESET YOUR PASSWORD"))
