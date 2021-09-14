import requests
import pandas as pd
from bs4 import BeautifulSoup

url='https://www.bkmkitap.com/bilim-tarihi-kitaplari?sort=6'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'}

def fiyat_cek():
    response=requests.get(url)
    html_icerigi = response.content
    soup = BeautifulSoup(html_icerigi,"html.parser")
    fiyat = soup.find_all("div",{"class":"col col-12 currentPrice"})
    isim =soup.find_all("a",{"class":"fl col-12 text-description detailLink"})
    yazar = soup.find_all("a",{"class":"fl col-12 text-title"})
    yayın = soup.find_all("a",{"class":"col col-12 text-title mt"})
   # print(isim,yazar,yayın)
    liste = list()

    for i in range(len(isim)):
        isim[i] = (isim[i].text).strip("\n").strip()
        yazar[i] = (yazar[i].text).strip("\n").strip()
        yayın[i] = (yayın[i].text).strip("\n").strip()
        fiyat[i] = (fiyat[i].text).strip("\n").replace("\nTL"," TL").strip()
        liste.append([isim[i],yazar[i],yayın[i],fiyat[i]])

    df = pd.DataFrame(liste,columns = ["Kitap İsmi","Yazar","Yayın Evi","Fiyat"])
    print(df)

fiyat_cek()
