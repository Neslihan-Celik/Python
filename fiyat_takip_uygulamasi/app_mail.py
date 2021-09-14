import requests
from bs4 import BeautifulSoup
import smtplib
import time
url='https://www.bkmkitap.com/bilim-kadinlari-dunyayi-degistiren-50-korkusuz-bilimci?waw_keyword=bilim%20kad%C4%B1nlar%C4%B1'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'}

def mail_gonder(kitap):
     sender='pythonilemailgonderme@gmail.com'
     receiver='nesli.celik.966@gmail.com'
     try:

        server=smtplib.SMTP('smpt.gmail.com',587)
        server.ehlo()
        server.starttls()
        server.login(sender,'deneme123')
        subject=kitap+' Hakkında'
        body= ' Bu mail python ile internet üzerinden veri çekip mail atmak için oluşturuldu.¨\n Hazır veriler çekildi bana şu kitabı alsanız fena olmaz dua ederim bol bol =) link -> '+url
        mailContent=f"TO:{receiver}\nFrom:{sender}\nSubject:{subject}\n\n{body}"
        print('Mail gönderildi')

     except smtplib.SMTPException as e:
        print(e)
     finally:
        server.quit()


def bilgi_cek():

    page=requests.get(url,headers=headers)
    soup = BeautifulSoup(page.content,"html.parser")
    kitap = soup.find(id='productName').getText().strip()
   
   
    yazar= soup.find(id='productModelText').getText().strip()
    yayinevi= soup.find(id='productName').getText()
    print(kitap,yazar)
   
    mail_gonder(kitap)

while(1):
    bilgi_cek()
    time.sleep(60*60)
