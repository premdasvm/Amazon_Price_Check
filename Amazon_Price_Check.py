import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = 'https://www.amazon.in/Behringer-HC-200-Professional-Headphones/dp/B07V4RL8PF/ref=pd_sbs_267_4/257-2757016-4716359?_encoding=UTF8&pd_rd_i=B07V4RL8PF&pd_rd_r=e70d074a-6043-483d-a1a9-097679b5e058&pd_rd_w=yKyOD&pd_rd_wg=86dvt&pf_rd_p=00b53f5d-d1f8-4708-89df-2987ccce05ce&pf_rd_r=N367GYJ7G88Q8X95C8F2&psc=1&refRID=N367GYJ7G88Q8X95C8F2'

headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:79.0) Gecko/20100101 Firefox/79.0'}


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
    server.login('thorinlotr4@gmail.com', 'jktanoduhkkgkamc')

    Subject = 'Hey The Price Dropped'
    body = 'Price Dropped For The Headphone, https://www.amazon.in/Behringer-HC-200-Professional-Headphones/dp/B07V4RL8PF/ref=pd_sbs_267_4/257-2757016-4716359?_encoding=UTF8&pd_rd_i=B07V4RL8PF&pd_rd_r=e70d074a-6043-483d-a1a9-097679b5e058&pd_rd_w=yKyOD&pd_rd_wg=86dvt&pf_rd_p=00b53f5d-d1f8-4708-89df-2987ccce05ce&pf_rd_r=N367GYJ7G88Q8X95C8F2&psc=1&refRID=N367GYJ7G88Q8X95C8F2'

    # msg = f"""Subject: {Subject}\n\n{body}"""
    msg = 'Subject: %s\n\n%s'%(Subject, body)

    server.sendmail('thorinlotr4@gmail.com', 'premdasvm8@gmail.com', msg)

    print('HEY MAIL HAS BEEN SENT')

    server.quit()

while(True):
    check_Price()
    time.sleep(10)
