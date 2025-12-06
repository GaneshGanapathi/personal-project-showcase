import pandas as pd
import smtplib 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

frm_addr = "enter your email"
password = "enter your email password"

data=pd.read_csv("email.csv")
emails = data["email"].tolist()
names = data["name"].tolist()

mail = smtplib.SMTP('smtp.gmail.com', 587)
mail.starttls()
mail.login(frm_addr, password)


for i in range(len(emails)):
    try: 
        msg = MIMEMultipart()
        msg["From"] = frm_addr
        msg["To"] = emails[i]
        msg["Subject"] = 'Holiday Wishes'

        body = f'HI {names[i]}, Wishing you a Merry Christmas and Happy New Year!'
        msg.attach(MIMEText(body,'plain'))

        
        mail.sendmail(frm_addr, emails[i],msg.as_string())
        print(f'Sent to {emails[i]}')
    
    except Exception as e:
        print(f'Failed for {emails[i]} -> {e}')


mail.quit()
print("Sent")
