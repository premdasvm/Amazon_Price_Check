import requests
from bs4 import BeautifulSoup
import smtplib
import time

# URL Of the product on amazon, Only amazon is supported

URL = 'PRODUCT_URL'

# Change the User-Agent to your computer's

headers = {"User-Agent": 'YOUR_USER-AGENT}


# User Defined variables
# To Authenticate Email access you may have to enable 2-Factor Authenctiv=cation on your Gmail account
# Then Generate Google App Password for the Mail app, And Use the Password here.

Email = 'YOUR_EMAIL_ADDRESS'
password = 'YOUR_PASSWORD'
ToEmail = 'TO_EMAIL_ADDRESS'
Checking_Interval = 60 # In Seconds

# Email Subject & Body

Subject = 'YOUR_MESSAGE_SUBJECT'
Body = 'YOUR_MESSAGE_BODY'


def check_Price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    converted_Price = float(price[2:7].replace(',', ''))
    
    if(converted_Price < 2000.00):
        send_mail()

    print(converted_Price)
    print(title.strip())

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(Email, password)

    msg = 'Subject: %s\n\n%s'%(Subject, Body)

    server.sendmail(Email, ToEmail, msg)

    print('HEY MAIL HAS BEEN SENT')

    server.quit()

while(True):
    check_Price()
    time.sleep(Checking_Interval)

