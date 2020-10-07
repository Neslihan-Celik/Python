
#----------------------------Python Alıştırmaları----------------------------------#
#----------------------------------------------------------------------------------#
#basit işlemler

print("nes")

liste1=[1,2,3]
liste2=["a","b","c"]
print(liste1+liste2)
print("\n")
print(liste1)

x,y,z="altın ","kuvars ","elmas "
print(x)
print("\n",y)
print("\n",y+x+z,"\n")

#----------------------------------------------------------------------------------#
#String uzunluk bulan method
ad="Neslihan"
print("\n Merhaba benim adım",ad,"\n Adımın uzunluğu",1*len(ad),"\n harftir")

isim=input("isim giriniz")
print("\n Merhaba senin adın",isim,"\n Adının uzunluğu",1*len(isim),"\n harftir")

#----------------------------------------------------------------------------------#
#true false kullanımı
sayi=input("sayı giriniz")
print(sayi)
sayi=bool(0)
print("sayi son hal ",sayi)

#----------------------------------------------------------------------------------#
#----------------------Liste işlemleri---------------------------------------------#

#her hangi bir şeyin tüm karakterilerinin listesini çıkartan method
n=("AnkaraTürkiye'ninBaşkentidir!")
list(n)
print(list(n))
print("\n")

#küme fonksiyonu 
print("\n")
print(set(n))
print("\n")

#enumarete liste elemenının indis numarasıyla yazımı
print(list(enumerate("merhaba")))
print("\n")

#girdi kontrol true veya false çıktı verir
isinstance("hello",str)
print(isinstance("hello",str))
print("\n")

isinstance(123,int)
print("\n")

#en büyük bulma
a=[1,2,3,]
max(a)
print("\n")

#en küçük bulma
b=[9,8,7]
min(b)
print("\n")

#küme elemanlarını toplama
x=[1,2,3,4,5]
sum(x)
print("\n")

#----------------------------------------------------------------------------------#
#-----------------------------Kontrol yapıları-------------------------------------#

#if, elif ve else yapıları
x=2
y=3

if y>x:
    print('büyük sayı y')

elif x>y:
    print('büyük sayı x')

    
else:
    print('sayılar eşit')  
    

#----------------------------------------------------------------------------------#
#basit kontrol

yas = int(input("Yaş bilgisi giriniz :"))

if yas >= 18:
    print('Yaşınız 18\'den büyük\nYaşınız :',yas)

elif yas < 18:
    print('Yaşiniz 18 \'den küçük \Yaşınız :',yas)

else:
    print('Lütfen yaş bilgisi giriniz !')

#----------------------------------------------------------------------------------#
#En büyük sayı bulma

a = 1  # type: int
b = 2  # type: int
c = 3  # type: int 

if a > b and a > c:
    print('Büyük sayı a\'dır.')

elif b > a and b > c:
    print('Büyük sayı b\'dir.')

elif c > a and c > b:
    print('Büyük sayı c\'dir.')

#----------------------------------------------------------------------------------#
#Tek çift sayı bulma

sayi=int(input('Lütfen bir sayı giriniz :'))  # type: int
if sayi%2==0:
        print('Sayı çift sayıdır')

else:
        print('Sayı tek sayıdır ')


#----------------------------------------------------------------------------------#

#Vize final Ortalama hesaplama (ortalama =vize%50+ Final %50)
vize=int(input('Lütfen vizenizi giriniz :'))  # type: int
final=int(input('Lütfen finalinizi giriniz :'))  # type: int

ortalama=(vize+final)/2 # type: int
print('\nOrtalamanız :',ortalama)

harfNotu=''  # type: str
if  ortalama <40 and ortalama > 0:
    harfNotu='FF'
    print('\nHarf Notunuz : ', harfNotu, '\nMaalesef kaldınız =(')

elif  ortalama < 50 and ortalama > 39:
    harfNotu='DD'
    print('\nHarf Notunuz : ',harfNotu)

elif ortalama < 75 and ortalama > 49:
    harfNotu = 'CC'
    print('\nHarf Notunuz : ', harfNotu)

elif ortalama < 85 and ortalama > 74:
    harfNotu = 'BB'
    print('\nHarf Notunuz : ', harfNotu)

else:
    harfNotu = 'AA'
    print('\nHarf Notunuz : ', harfNotu,'\nTebrikler! \nBaşarılarınızın devamını dileriz.')


#----------------------------------------------------------------------------------#
#manav uygulaması lütfen artık fonksiyonlara geçelim =)

manavList = ['elma', 'armut', 'üzüm', 'muz']
print("\nManavda bulunan meyveler şunlardır :\n", manavList)
secim = input('\nHangi meyveyi istersiniz :')
if secim == 'elma':
    kilo = int(input('kaç kilo istiyorsunuz :'))
    fiyat = 4  # Type int

    if kilo == 1:
        print("\nSeçtiğiniz meyve :", secim, "\nİstediğiniz miktar :", kilo,"kilo", "\nÖdemeniz gereken tutar :", fiyat , "TL")

    elif kilo == 2:
        print("\nSeçtiğiniz meyve :", secim, "\nİstediğiniz miktar :", kilo,"kilo","\nÖdemeniz gereken tutar :", fiyat * 2,"TL")

    elif kilo ==3:
        print("\nSeçtiğiniz meyve :", secim, "\nİstediğiniz miktar :", kilo,"kilo", "\nÖdemeniz gereken tutar :", fiyat * 3, "TL")

    else:
        print("\nManavda istediğiniz miktarda meyve bulunmamaktadır!")


elif secim == 'armut':
    kilo = int(input('kaç kilo istiyorsunuz :'))
    fiyat = 5  # Type int

    if kilo == 1:
        print("\nSeçtiğiniz meyve :", secim, "\nİstediğiniz miktar :", kilo, "kilo","\nÖdemeniz gereken tutar :", fiyat , "TL")

    elif kilo == 2:
        print("\nSeçtiğiniz meyve :", secim, "\nİstediğiniz miktar :", kilo, "kilo","\nÖdemeniz gereken tutar :", fiyat * 2, "TL")

    elif kilo ==3:
        print("\nSeçtiğiniz meyve :", secim, "\nİstediğiniz miktar :" ,kilo,"kilo","\nÖdemeniz gereken tutar :", fiyat * 3, "TL")

    else:
        print("\nManavda istediğiniz miktarda meyve bulunmamaktadır!")


elif secim == 'üzüm':
    kilo = int(input('kaç kilo istiyorsunuz :'))
    fiyat = 7  # Type int

    if kilo == 1:
        print("\nSeçtiğiniz meyve :", secim, "\nİstediğiniz miktar :", kilo, "kilo","\nÖdemeniz gereken tutar :", fiyat , "TL")

    elif kilo == 2:
        print("\nSeçtiğiniz meyve :", secim, "\nİstediğiniz miktar :", kilo, "kilo","\nÖdemeniz gereken tutar :", fiyat * 2, "TL")

    elif kilo ==3:
        print("\nSeçtiğiniz meyve :", secim, "\nİstediğiniz miktar :" ,kilo,"kilo","\nÖdemeniz gereken tutar :", fiyat * 3, "TL")

    else:
        print("\nManavda istediğiniz miktarda meyve bulunmamaktadır!")


elif secim == 'muz':
    kilo = int(input('kaç kilo istiyorsunuz :'))
    fiyat = 11  # Type int

    if kilo == 1:
        print("\nSeçtiğiniz meyve :", secim, "\nİstediğiniz miktar :", kilo, "kilo","\nÖdemeniz gereken tutar :", fiyat , "TL")

    elif kilo == 2:
        print("\nSeçtiğiniz meyve :", secim, "\nİstediğiniz miktar :", kilo, "kilo","\nÖdemeniz gereken tutar :", fiyat * 2, "TL")

    elif kilo ==3:
        print("\nSeçtiğiniz meyve :", secim, "\nİstediğiniz miktar :" ,kilo,"kilo","\nÖdemeniz gereken tutar :", fiyat * 3, "TL")

    else:
        print("\nManavda istediğiniz miktarda meyve bulunmamaktadır!")


else:
    print("\nManavda bulunmayan bir şey girdiniz !\nLütfen tekrar deneyiniz...")
    print("\nLütfen artık fonksiyonlara geçelim =)")


#----------------------------------------------------------------------------------#
#--------------------------------Döngüler------------------------------------------#

#for döngüsü

for i in range(1,100):
    if i%2==0:
        print(i)

for i in range(1,100):
    if i%2==1:
        print(i)


sayilar='1234567890'
for sayi in sayilar:
    print(int(sayi))


sayilar='1234567890'
for sayi in sayilar:
    print(int(sayi*2))


sayilar='1234567890'
for sayi in sayilar:
    print(int(sayilar))

sayilar='1234567890'
for sayi in sayilar:
    if int(sayi)>3 and int(sayi)%2==0:
        print(sayi)


harfler=['a','b','c','d','e','f','g']
for sesli in harfler:
    if sesli=='a' or sesli=='e':
        print(sesli)

harfler=['a','b','c','d','e','f','g']
for sesli in harfler:
    print(sesli)
    if sesli=='d':
             break 


#----------------------------------------------------------------------------------#

#while döngüsü

#Python sonzuz döngü =)
a=1
while a<10:
    print(a)
    

a=1
while a<10:
    print(a)
       a+=1

#Daha komik bir sonsuz döngü
a=1
while a<10:
    print(5*'Python sen acayip bir dilsin ! ')



#Kontrol yapısı örneği
while True:
    TC=input("\nLütfen TC'nizi giriniz :")
    AsilTC='123456789011'

    if len(TC)!=12 or TC==str :
        print("\nLütfen TC'nizi doğru giriniz !\nTC'niz 11 rakam olmalı ve harf içermemelidir !")
        break
    elif int(TC)==int(AsilTC):
        print("TC'niz doğru Sisteme giriş yapabilirsiniz.")
        break
    else:
        print("TC'niz doğru değildir !\nSisteme giriş yapamazsınız!!!")
        break



while True: 
   metin=input('Lütfen girmek istediğiniz metni yazınız :')
   if metin==str:
       continue

   elif metin==int or metin=='İPTAL':
       break


#----------------------------------------------------------------------------------#

#range methodu ile işlemler
for i in range(1,10):
    print(i)

for i in range(1,100,2):
    print(i)

for i in range(100,1,5):
    print(i)

print(*range(1,10))

print(*range(1,10,2))

#----------------------------------------------------------------------------------#
#----------------------------------Alıştırmalar------------------------------------#

# asal sayı kontrol
sayac = 0
sayi = int(input("Lütfen sayı giriniz : "))
for i in range(2, int(sayi)):
    if (int(sayi % i == 0)):
        sayac += 1

    if (sayac != 0):
        print("Girdiğiniz ", sayi, "sayısı asal değildir")
        break
    else:
        print("Girdiğiniz ", sayi, " sayısı asal bir sayıdır")
        break


#----------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------#

#Hesap makinesi
islemler='''
(1)Toplama
(2)Çıkartma
(3)Çarpma
(4)Bölme
(5)Kare Alma
(6)Kök Bulma
(X)ÇIKIŞ YAP
'''
print(islemler)
while True:
    islem=input("\nHangi işlemi yapmak istiyorsunuz : ")
    if islem=='X' or islem=='x':
        print("Seçtiğiniz işlem : ÇIKIŞ YAP")
        print("Çıkış Yapıldı !")
        break

    elif islem=="1":
        sayi1 = int(input("Lütfen 1.sayıyı giriniz : "))
        sayi2 = int(input("Lütfen 2.sayıyı giriniz : "))
        print("Seçtiğiniz işlem : Toplama")
        print(sayi1," + ",sayi2," = ",sayi1+sayi2)

    elif islem=="2":
        sayi1 = int(input("Lütfen 1.sayıyı giriniz : "))
        sayi2 = int(input("Lütfen 2.sayıyı giriniz : "))
        print("Seçtiğiniz işlem : Çıkartma ")
        print(sayi1," - ",sayi2," = ",sayi1-sayi2)

    elif islem=="3":
        sayi1 = int(input("Lütfen 1.sayıyı giriniz : "))
        sayi2 = int(input("Lütfen 2.sayıyı giriniz : "))
        print("Seçtiğiniz işlem : Çarpma")
        print(sayi1," x ",sayi2," = ",sayi1*sayi2)

    elif islem=="4":
        sayi1 = int(input("Lütfen 1.sayıyı giriniz : "))
        sayi2 = int(input("Lütfen 2.sayıyı giriniz : "))
        print("Seçtiğiniz işlem : Bölme")
        print(sayi1," / ",sayi2," = ",sayi1/sayi2)

    elif islem=="5":
        sayi = int(input("Lütfen Karesini almak istediğiniz sayıyı giriniz : "))
        print("Seçtiğiniz işlem : Kare Alma ")
        print(sayi,"sayısının karesi "," = ",sayi**2)

    elif islem=="6":
        sayi = int(input("Lütfen Kökünü bulmak istediğiniz sayıyı giriniz : "))
        print("Seçtiğiniz işlem : Kök Bulma")
        print(sayi, "sayısının kökü ", " = ", sayi ** 3)

    else:
        print("----------------------------------------------------------------------------")
        print("Yanlış Karakter girdiniz !\nLütfen aşağıdaki işlemlerden birini seçiniz ...")
        print("----------------------------------------------------------------------------")


#----------------------------------------------------------------------------------#

#Random kullanımı

import random
aile=["nes","os","dil","mem","muc","tur","an","ba"]
print("Rastgele seçilen kişi : ",random.choice(aile))



#sayı tahmin oyunu

import random
gizliSayi=random.randint(1,50)
sayac=0

print("\nMerhaba sayı tahmin oyununa hoşgeldiniz !"
       "\ngizli sayı 1 ile 50 arasındadır"
      "\nYapmanız gereken en kısa sürede gizli sayıyı bulmak"
      "\nBaşarılar !!!"
      "\n(Çıkış yapmak için 0'ra basın)\n\n")

while True:
    sayac+=1
    tahmin=int(input("Lütfen tahmininizi giriniz : "))
    if tahmin==0:
        print("\nÇıkış yapıldı !")
        print("Doğru sayı {} idi !".format(gizliSayi),"\nSen {} tahminde bulundun .".format(sayac))
        break

    elif gizliSayi>tahmin:
        print("Yaklaştın ama daha yüksek bir sayı girmelisin !\n")
        continue

    elif gizliSayi < tahmin:
        print("Yaklaştın ama daha düşük bir sayı girmelisin !\n")
        continue

    else:
        print("\n----------------------------------------")
        print("Tabrikler tahminin doğru !\n"
              "Doğru sayı ",gizliSayi,""
              " sen {} denemede buldun . ".format(sayac))
        print("----------------------------------------")
        break



#----------------------------------------------------------------------------------#  

#Sisteme kullanıcı giriş kontrolü

print("\nHoşgeldiniz !\nLütfen kullanıcı adınızı ve şifrenizi giriniz !\n")
print("---------------------------")
kullaniciAdi=input("Kullanıcı Adınız : ")
sifre=input("Şifreniz : ")
print("---------------------------\n")

sayac=1
Admin="nes"
Password="1234"

while True:

    if sayac==5:
        print("\n{} hatalı giriş denemesi".format(sayac),"\nSistemden çıkartıldınız !")
        break


    elif kullaniciAdi==Admin and sifre==Password:
        print("Merhaba Admin \nSisteme başarılı bir şekilde giriş yaptınız !")
        break

    elif kullaniciAdi==Admin and sifre!=Password:
        print("Girdiğiniz şifre yanlış tekrar deneyin!")
        print("---------------------------")
        kullaniciAdi = input("Kullanıcı Adınız : ")
        sifre = input("Şifreniz : ")
        print("---------------------------\n")
        sayac+=1
        continue

    elif kullaniciAdi!=Admin and sifre==Password:
        print("Girdiğiniz kullanıcı adı yanlış tekrar deneyin!")
        print("---------------------------")
        kullaniciAdi = input("Kullanıcı Adınız : ")
        sifre = input("Şifreniz : ")
        print("---------------------------\n")
        sayac += 1
        continue

    elif kullaniciAdi!=Admin and sifre!=Password:
        print("Girdiğiniz kullanıcı adı  ve şifre yanlış tekrar deneyin!")
        print("---------------------------")
        kullaniciAdi = input("Kullanıcı Adınız : ")
        sifre = input("Şifreniz : ")
        print("---------------------------\n")
        sayac += 1
        continue


#----------------------------------------------------------------------------------#  
#----------------------------------Fonksiyonlar------------------------------------# 

#Fonksiyon örnekleri

def bilgiKutusu(ad,soyad,yas,cinsiyet,uyruk):
    print("-"*30)
    print("Ad :",ad)
    print("Soyad :",soyad)
    print("Yaş :",yas)
    print("Cinsiyet :",cinsiyet)
    print("Uyruk :",uyruk)
    print("-" * 30)

bilgiKutusu("xxx","xxxx","xxx","xxx","xxx")




def ulkeTanitim(ulke,baskent,nufus,ulkeKodu):
    ekranaBastir="Ülke :{}\nBaşkent :{}\nNüfus :{}\nÜlke Kodu :{}"
    print("-"*30)
    print(ekranaBastir.format(ulke,baskent,nufus,ulkeKodu))
    print("-" * 30,"\n")

ulkeTanitim("Türkiye","Ankara","83 Milyon","TR")
ulkeTanitim("Ukrayna","Kiev","41 Milyon","UA")




def adinNe():
    ad=input("Adın ne :")
    return ad

print("\nMerhaba {}.\nNasılsın ".format(adinNe()))




def kontrolYapisi(ifade):
    if ifade==0:
        print("Girdiğiniz sayı Sıfırdır !")

    elif ifade<0:
        print("Girdiğiniz sayı Negatiftir !")

    else:
        print("Girdiğiniz sayı Pozitiftir !")


ifade=int(input("Litfen bir sayı girin : "))
kontrolYapisi(ifade)




def kontrol(x):
    if x<0:
        return "Negatif bir değer giremezsiniz"
    else:
        return x

print(kontrol(-1))


list=["meyve","sebze"]

def liste():
    global list #Bu yapıyı bil ama kullanma !
    list.append("tahıl")
    return list
print("Liste öğeleri :\n",liste())



#lambda yapısı (küçük fonksiyon)

fonk=lambda sayi1,sayi2:sayi1+sayi2
print(fonk(2899,199))


#faktöriyel hesaplama

def faktoriel(x):
  if x==0:
      return 1
  else:
      return x*faktoriel(x-1)

x=int(input("Faktöriyelini hesaplamak istediğiniz sayıyı girin : "))
print(faktoriel(x))


#----------------------------------------------------------------------------------# 

#geometrik hesaplama örneği

def daire():
    print("-"*30,"\nSeçim : Daire \n")
    yaricap=input("\nÇevresini ve Alanını hesaplamak istediğiniz Dairenin Yarıçapını girin : ")
    cevre=(2*3.14*float(yaricap))
    alan=(3.14*float(yaricap)*float(yaricap))
    print("\n")
    print("-"*30)
    print("Dairenin Alanı : {}\nDairenin Çevresi : {}".format(alan,cevre))
    print("-" * 30)

def dikdortgen():
    print("-" * 30, "\nSeçim : Dikdörtgen \n")
    uzunKenar=int(input("Lütfen Dikdörgen\'in Uzun kenar uzunluğunu giriniz : "))
    kisaKenar = int(input("Lütfen Dikdörgen\'in Kısa kenar uzunluğunu giriniz : "))
    alan=uzunKenar*kisaKenar
    cevre=2*(uzunKenar+kisaKenar)
    print("\n")
    print("-" * 30)
    print("Dikdörtgen\'in  Alanı : {}\nDikdörtgen\'in Çevresi : {}".format(alan, cevre))
    print("-" * 30)

def ucgen():
    print("-" * 30, "\nSeçim : Üçgen (Çeşitkenar) \n")
    birinciKenar = int(input("Lütfen birinci kenar uzunluğunu giriniz : "))
    ikinciKenar = int(input("Lütfen ikinci  kenar uzunluğunu giriniz : "))
    ucuncuKenar = int(input("Lütfen üçüncü  kenar uzunluğunu giriniz : "))
    x=(birinciKenar+ikinciKenar+ucuncuKenar)/2
    alan=(x*(x-birinciKenar)*(x-ikinciKenar)*(x-ucuncuKenar))**(0.5)
    cevre=(birinciKenar+ikinciKenar+ucuncuKenar)
    print("\n")
    print("-" * 30)
    print("Üçgen\'in  Alanı : {}\nÜçgen\'in Çevresi : {}".format(alan, cevre))
    print("-" * 30)

def kup():
    print("-" * 30, "\nSeçim : Küp \n")
    kenarUzunluk = int(input("Lütfen Küp\'ün bir  kenar uzunluğunu giriniz : "))
    cevre=kenarUzunluk*12
    alan=6*kenarUzunluk**2
    hacim=kenarUzunluk**3
    print("\n")
    print("-" * 30)
    print("Küp\'ün  Alanı : {}\nKüp\'ün Çevresi : {}\nKüp\'ün Hacmi : {}".format(alan, cevre,hacim))
    print("-" * 30)

def kare():
    print("-" * 30, "\nSeçim : Kare \n")
    kenar = int(input("Lütfen Kare\'nin bir  kenar uzunluğunu giriniz : "))
    alan=kenar**2
    cevre=4*kenar
    print("\n")
    print("-" * 30)
    print("Kare\'nin  Alanı : {}\nKare\'nin Çevresi : {}".format(alan, cevre))
    print("-" * 30)

def silindir():
    print("-" * 30, "\nSeçim : Silindir \n")
    yukseklik = int(input("Lütfen Silindir\'in yüksekliğini giriniz : "))
    yaricap = int(input("Lütfen Silindir\'in yarıçapını giriniz : "))
    alan=(2*3.14*yaricap*(yaricap+yukseklik))
    hacim=(3.14*(yaricap**2)*yukseklik)
    print("\n")
    print("-" * 30)
    print("Silindir\'in Alanı : {}\nSilindir\'in Hacmi : {}".format(alan, hacim))
    print("-" * 30)

def cikis():
    print("Sistemde tanımsız bir karakter girdiğiniz için Çıkış yaptınız !!!")


sec=input("Daire = 1\nDikdörtgen = 2\nÜçgen = 3\nKüp = 4\nKare = 5\nSilindir = 6\nÇIKIŞ için herhangi bir karekter girin !\nHangisi için işlem yapacaksınız ? \n\nLütfen kodu girin : ")

while True:
    if sec == "1":
        daire()
        break
    elif sec=="2":
        dikdortgen()
        break
    elif sec=="3":
        ucgen()
        break
    elif sec=="4":
        kup()
        break
    elif sec == "5":
        kare()
        break
    elif sec == "6":
        silindir()
        break
    else:
        cikis()
        break




#----------------------------------------------------------------------------------# 

#ebob ekok  alıştırması

def ebob():
    print("\nSeçim = Ebob\n")
    sayi1 = int(input("1. Sayıyı girin : "))
    sayi2 = int(input("2. Sayıyı girin : "))
    kucukSayi=min(sayi1,sayi2)
    bolenler=[]
    for i in range(1,kucukSayi+1):
        if sayi1%i==0 and sayi2%i==0:
            bolenler.append(i)
    bolenler.sort(reverse=True)
    if len(bolenler)==0:
        return print("\nEbob({},{}) = {}".format(sayi1, sayi2,1))
    return print("\nEbob({},{}) = {}".format(sayi1, sayi2, bolenler[0]))

def ekok():
    print("\nSeçim = Ekok\n")
    sayi1 = int(input("1. Sayıyı girin : "))
    sayi2 = int(input("2. Sayıyı girin : "))
    carpim=sayi1*sayi2
    sayi1Katlari=set()
    sayi2Katlari=set()
    for i in range(1,carpim):
        if sayi1*1!=carpim:
            sayi1Katlari.add(sayi1*i)
        else:
            break

    for k in range(1,carpim):
        if sayi2*k!=carpim:
            sayi2Katlari.add(sayi2*k)
        else:
            break

    kesisim=sayi1Katlari.intersection(sayi2Katlari)
    liste=list(kesisim)
    if len(liste)==0:
        return print("\nEkok({},{}) = {}".format(sayi1,sayi2,carpim))
    else:
        return print("\nEkok({},{}) = {}".format(sayi1,sayi2,liste[0]))






secim=input("\nEkok=1\nEbob=2\nÇIKIŞ için herhangi bir karakter girin \n\nHangisi için işlem yapcaksınız : ")

while True:
    if secim=="1":
        ekok()
        break

    elif secim=="2":
        ebob()
        break

    else:
        print("\nYanlış karakter girdiniz !\nÇıkış yaptınız !!!")
        break




#----------------------------------------------------------------------------------# 
#-----------------------------------Methodlar--------------------------------------# 
#-----------------------------------Karakter Methodları----------------------------# 

#dir methodu

sayac=0
for i in dir(" "):
    if "_" not in i[0]:
        sayac+=1
        print(sayac,i)

print("\nToplam {} method  vardır .".format(sayac))



#enumerate methodu

a="TürkiyeCumhuriyetininNüfusu83Milyondur"
print(*enumerate(a))



#daha kullanışlı versiyon

for sira,method in enumerate(dir("")):
    print(sira+1,method)



#replace

x="Ağri dağinin eteğinde"
print(x.replace("ğ","g"))



#split

x="Bir yıl üçyüz atmış beş gündür."
print(x.split(" "))


i="Türkiye Büyük Millet Meclisi "
for k in i.split(" "):
    print(k)



#capitalize

i="TÜRKİYE'NİN BAŞKENTİ ÇOK GÜZELDİR."
print(i,"\n",i.capitalize())



#title

i="merhaba ben neslihan."
print(i.title())



#swapcase

i="yAZI yAZMAYI hEP çOK sEVDİM dER şAİR."
print(i.swapcase())



#strip ve split kullanımı

metin='''
<liste 
<birinci 
<ikinci
<üçüncü 
<...
<... '''

for i in metin.split():
    print(i.strip("<"))



#join

x="Elektrik Elektronik Mühendisliği"
bolum=x.split()
print(x)
print(bolum)
print(" ".join(bolum))


#count

metin='''abcdhjdhwıyueqwhuaaaagqwwhuowejemmfv
ççvçmnnhwueıuuqteqqğqünnnnqüplööasmdwdheaaeararar
fwferıhereereruferueyrbbbbuurwıurfeıuwrfwuıfer'''

print("Metin içerisindeki 'n' harfi sayısı : ",metin.count("n"))




sifrebelirle=input("Lütfen yeni bir şifre belirleyiniz : ")

kontrol=True
for i in sifrebelirle:
    if sifrebelirle.count(i)>1:
        kontrol=False

if kontrol:
    print("Yeni şifreniz onaylandı !")
else:
    print("Şifrenizde bir karakteri yanlız bir kere kullanabilirsiniz !!!")



#index

x="istanbul"
print(x.index("n"))



#center

x="istanbul"
print(x.center(50))


#Bu yapı çok kullanışlı !
x="BAŞLIK" 
print(x.center(100,"-"))



#rjust ve ljust
#En güzel özellik =)

x="İstanbul"
print(x.rjust(15,"."))

x="Sen"
print(x.ljust(15,"."))

x="Bir"
print(x.rjust(15,"."))

x="Şiirsin"
print(x.ljust(15,"."))



for i in "elma","armut","muz","karpuz","kavun","......":
    print(i.ljust(10,"."))



#maketrans ve translate
#vazgeçtim en yararlı methodlar bunlar 

kaynak="çşğıöüŞÇĞÜÖİ"
hedef="csgiouSCGUOI"
ceviri=str.maketrans(kaynak,hedef)
metin="Şanlıurfa ve Ağrı Türkiye'de bulunan şehirlerdir. şğöçİ "
print(metin.translate(ceviri))



#isalpha

a="evimEvimGüzelEvim"
print(a.isalpha())

a="evim Evim Güzel Evim"
print(a.isalpha())



#isdigit

a="1234567890"
print(a.isdigit())

a="1234567890sayi"
print(a.isdigit())


#isalnum

a="1234567890sayi"
print(a.isalnum())



#----------------------------------------------------------------------------------# 
#-----------------------------------Liste Methodları-------------------------------# 


#liste methodları

for i in dir(list):
    if not "_"in i:
        print(i)


#append

liste=["ayı","kuş","tilki","timsah","inek","leylek"]
liste.append("devekuşu")
print(liste)


#append sadece bir parametre alıyor çoklu alım için döngü kullan !
sayiList=[1,2,3,4]
for i in[5,6,7,8,9,0]:
    sayiList.append(i)

print(sayiList)


#extend

liste1=[0,9,8,7,6]
liste2=[5,4,3,2,1]
liste1.extend(liste2)
print(liste1)


#insert

a=[1,2,3,4]
a.insert(0,0)
print(a)


#remove

list=[1,2,3,4,5,7,6,7,8,9,0]
list.remove(7)
print(list)


#reverse

x=["dünya","ay","venüs","uranüs","jüpiter","neptün"]
y=["n","a","h","i","l","s","e","N"]
x.reverse()
y.reverse()
print(x)
print(y)


#sort

sayilar=[3,5,9,-8,-6,-20,1,11,45,0]
sayilar.sort()
print(sayilar)


#sort ve reverse birlikte 
sayiList=[1,10,100,1000,10000]
sayiList.sort(reverse=True)
print(sayiList)


#index

list=["a","b","c","d","e"]
print(list.index("c")+1)



#----------------------------------------------------------------------------------# 
#----------------------------------Sözlük methodları-------------------------------#

#keys-values-items

sozluk={"a":0,"b":1,"c":2,"d":3,"e":4}
print(sozluk.keys())

sozluk={"a":0,"b":1,"c":2,"d":3,"e":4}
print(sozluk.values())

sozluk={"a":0,"b":1,"c":2,"d":3,"e":4}
print(sozluk.items())



ingSozluk={"dil":"language","insan":"human","bilgisayar":"computer","masa":"table"}

sorgu=input("Çevirmek istediğiniz kelimeyi girin : ")

if sorgu not in ingSozluk:
    print("\nAradığınız kelimenin sözlüğümüzde bir karşılığı yoktur !")
else:
    print("\nAradığınız kelimenin ingilizce karşılığı : ",ingSozluk[sorgu])


#get

ingSozluk={"dil":"language","insan":"human","bilgisayar":"computer","masa":"table"}
sorgu=input("Çevirmek istediğiniz kelimeyi girin : ")

print(ingSozluk.get(sorgu,"\nAradığınız kelimenin sözlükte karşılığı yok !"))


#fromkeys

kisiler="Ayça AY","Ahmet GÜN","Selim YIL","Feyza YÜZYIL"
adresler=dict.fromkeys(kisiler,"İstanbul")

print(adresler)


#setdefault

sepet={"meyve":{"muz","elma","kiraz"},"sebze":{"domates","salatalık","patlıcan"}}
sepet.setdefault("tahıl",{"mercimek","nohut","buğday"})
print(sepet)


#update

stokListe={"kola":15,"gazoz":20,"su":30,"meyve suyu":20}
yeniStok={"kola":9,"gazoz":12,"su":19,"meyve suyu":16}
stokListe.update(yeniStok)
print(stokListe)



#----------------------------------------------------------------------------------# 
#-----------------------------------Küme methodları--------------------------------#

for i in dir(set):
    if "__"not in i:
        print(i)



#add

küme=set(["kedi","kuş","köpek","yılan"])
küme.add("koyun")
print(küme)


#difference

liste1=set([0,1,2,3,4,5])
liste2=set([4,5,6,7,8,9])

print("liste1\'de olup liste2\'de olmayan elemenalar : ",liste1.difference(liste2))
print("liste2\'de olup liste1\'de olmayan elemenalar : ",liste2.difference(liste1))
#farklı  ve pratik kullanım
print(liste1-liste2)
print(liste2-liste1)



#difference_update

list1=set(["a","b","c"])
list2=set(["c","d","b","e"])
list1.difference_update(list2)
print("iki liste farkı :",list1)


#discard

gezegenler=set(["Dünya","Plüton","Neptün","Venüs","Jüpiter"])
gezegenler.discard("Plüton")  #Plüton gezegen değilsin artık üzgünüm =)
print(gezegenler)



#intersection

sayiList1=set([1,2,3,4,5,6,7])
sayiList2=set([6,7,8,9,0])

print("iki listenin ortak elemanları : ",sayiList1.intersection(sayiList2))
#daha kullanışlı yapı
print("iki listenin ortak elemanları : ",sayiList1&sayiList2)


#union

a=set([1,2,3,4,5])
b=set([6,7,8,9,0])
print("iki kümenin birleşimi :",a.union(b))
#pratik kullanım
print("iki kümenin birleşimi :",a|b)



#symmetric_difference

a=set([0,1,2,3,4,5])
b=set([3,4,5,6,7,8,9])
print("iki kümenin ortak elemanları : ",a.intersection(b))
print("İki kümenin ortak olmayan elemanları : ",a.symmetric_difference(b))


#----------------------------------------------------------------------------------# 
#-----------------------------------sayı methodları--------------------------------#


#bin-len

print("-"*25)
print("sayı\tbinary\t bit")
print("-"*25)
for i in range(11):
    print(i,bin(i)[2:], len(bin(i)[2:]),sep=" \t  ")
print("-"*25)



#bit_lenght

sayi=10
print("Girilen sayı ikilik sistemde {} bit yer kaplar .".format(sayi.bit_length()))


#Binary dönüştürücü

sayi=int(input("Binary karşılığını görmek istediğiniz sayıyı yazın :"))
if True:
    print("\nGirdiğiniz sayının bit uzunluğu :",(sayi).bit_length(),"\nİkili sistemdeki karşılığı : ",bin(sayi)[2:])
else:
    print("Hata!")


    
#----------------------------------------------------------------------------------# 
#-----------------------------------Modüller---------------------------------------#


#random

import random
print(dir(random))



import random
liste=[random.randint(0,100) for i in range(10)]
print(liste)



import random
sayi=int(input("Kaç adet rastgele sayı üretmek istiyorsunuz :"))
aralik=int(input("Sayı sınırınız nedir :"))
sayiList=[random.randint(0,aralik) for i in range(sayi)]
print("Sayı listeniz:",sayiList)



import random
print("Dosya\n{} \nadresinde  bulunuyor .".format(random.__file__))


#modul1 modülü
sozluk={"kitap":"book","elma":"apple","bilgisayar":"computer"}

def ceviri(kelime):
    hata="{} kelimesinin sözlükte karşılığı bulunmuyor !"
    return sozluk.get(kelime,hata.format(kelime))


import modul1
print("Aranan kelimenin karşılığı :",modul1.ceviri("ayak"))
print("Aranan kelimenin karşılığı :",modul1.ceviri("elma"))


#ikiliKontrol modülü
sayi=int(input("Binary karşılığını görmek istediğiniz sayıyı yazın :"))
if True:
    print("\nGirdiğiniz sayının bit uzunluğu :",(sayi).bit_length(),"\nİkili sistemdeki karşılığı : ",bin(sayi)[2:])
else:
    print("Hata!")
    
    
import ikiliKontrol
print(ikiliKontrol)



#----------------------------------------------------------------------------------# 
#--------------------------------Hata ayıklama-------------------------------------# 


#try-except

print("\nKarekök hesaplayıcısına hoşgeldiniz.\n")
sayi1=input("Sayı giriniz : ")


try:
    ilkSayi=int(sayi1)
    karekok=(ilkSayi)**0.5
    print("Sonuç : ",karekok)
except ValueError:
    print("Lütfen bir tam sayı giriniz !")



ilkSayi=input("1.sayıyı giriniz : ")
ikinciSayi=input("2.sayıyı giriniz : ")
try:
    sayi1=int(ilkSayi)
    sayi2=int(ikinciSayi)
    print("\nSonuç :\n{} / {} = {}".format(sayi1,sayi2,sayi1/sayi2))
except ValueError:
    print("\n")
    print("-"*35)
    print("\nLütfen tam sayı girin !\n")
    print("-" * 35)
except ZeroDivisionError:
    print("\n")
    print("-" * 35)
    print("\nHerhangi bir sayı sıfıra bölünemez !\n")
    print("-" * 35)
finally:
    print("\nProgram çalıştırılıp kapatıldı !")



#----------------------------------------------------------------------------------# 
#--------------------------------Dosya işlemleri-----------------------------------# 

#open-close-write-read

dosya=open("c:/ders/deneme.txt","w")
dosya.close()


dosya=open("c:/ders/dosya.txt","w")
dosya.write("Dosyaya yazı yazıldı !")
dosya.close()



dosya=open("c:/ders/borcluListesi.txt","w")
dosya.write("Ela : 100\n")
dosya.write("Ahmet : 500\n")
dosya.write("Veli : 700\n")
dosya.write("Sena : 250\n")
dosya.write("Cemal : 1000\n")
dosya.close()

bocluListesi=open("c:/ders/borcluListesi.txt")
print(bocluListesi.read())
bocluListesi.close()

bocluListesi=open("c:/ders/borcluListesi.txt","a")
bocluListesi.write("Suat : 950")
bocluListesi.close()


#readlines-readline

dosya=open("c:/ders/alisverisListesi.txt","w")
dosya.write("Pirinc\n")
dosya.write("Yag\n")
dosya.write("Zeytin\n")
dosya.write("Ekmek\n")
dosya.write("Tavuk\n")
dosya.write("Sut\n")
dosya.close()

liste=open("c:/ders/alisverisListesi.txt")
alisverisListesi=liste.readlines()
print("Birinci eleman :",alisverisListesi[0])
print(alisverisListesi[3])
liste.close()



dosya=open("c:/ders/alisverisListesi.txt","w")
dosya.write("Pirinc\n")
dosya.write("Yag\n")
dosya.write("Zeytin\n")
dosya.write("Ekmek\n")
dosya.write("Tavuk\n")
dosya.close()

liste=open("c:/ders/alisverisListesi.txt")
print(liste.readline())
print(liste.readline())
print(liste.readline())
liste.close()


#----------------------------------------------------------------------------------# 
#---------------------------Nesne tabanlı programlama------------------------------# 


# class yapısı

class insan:
    yas=0
    boy=0
    kilo=0
    isim=""
    soyisim=""
    dogumTarihi=0
    bugununTarihi=0
    def yasHesapla(self):
        yas=self.bugununTarihi-self.dogumTarihi
        return yas
    def tanit(self):
        print("\nMerhaba ben {} {} {} yaşındayım.\n"
              " Boyum {}, kilom ise {}. "
              "\nSizinle tanıştığıma memnun oldum."
              "".format(self.isim,self.soyisim,self.yasHesapla(),self.boy,self.kilo))
nes=insan()
nes.dogumTarihi=1996
nes.bugununTarihi=2020
nes.kilo=55
nes.boy=175
nes.isim="Neslin"
nes.soyisim="Neslin"

nes.tanit()

#OOP you are my dıl =)



class ogrenci:
    universite=""
    bolum=""
    numara=0
    isimSoyisim=""
    cinsiyet=None
    notOrtalamasi=0
    birinciSinifNot=0
    ikinciciSinifNot = 0
    ucuncuSinifNot = 0
    dorduncuSinifNot = 0

    def ortalamHesapla(self):
        self.birinciSinifNot=float(input("1.Sınıf Not Ortalamsı : "))
        self.ikinciciSinifNot = float(input("2.Sınıf Not Ortalamsı : "))
        self.ucuncuSinifNot = float(input("3.Sınıf Not Ortalamsı : "))
        self.dorduncuSinifNot = float(input("4.Sınıf Not Ortalamsı :"))

        self.notOrtalamasi=(self.birinciSinifNot+self.ikinciciSinifNot+self.ucuncuSinifNot+self.dorduncuSinifNot)/4
        return self.notOrtalamasi

    def tanit(self):
        return "\n\n------------ÖĞRENCİ BİLGİLERİ------------\n"\
                "isim Soyisim :{}\n" \
               "Cinsiyet : {}\n" \
               "Üniversite : {}\n" \
               "Bölüm :{} \n" \
               "Öğrenci Numarası :{}\n" \
               "Not ortalaması : {}\n" \
               "------------------------------------------\n" \
               "".format(self.isimSoyisim,self.cinsiyet,self.universite,self.bolum,self.numara,self.notOrtalamasi)

    def veriGiris(self):
            print("\nÖğrenci Veri giriş ekranı \n")
            self.isimSoyisim=input("İsim Soyisim : ")
            self.cinsiyet=input("Cinsiyet : ")
            self.universite=input("Üniversite : ")
            self.bolum=input("Bölüm :")
            self.numara=input("Öğrenci Numarası : ")
            self.notOrtalamasi=self.ortalamHesapla()
            return self.dosyayaAktar()
    def dosyayaAktar(self):
        dosya = open("c:/ders/ogrenciBilgi.txt", "a")
        dosya.write(self.tanit())
        dosya.close()


nes=ogrenci()
nes.veriGiris()
ahmet=ogrenci()
ahmet.veriGiris()




#İnit (yapılandırıcı)


class insan():
    def __init__(self,ad,soyad,yas,cins):#init Javadaki yapılandırıcı 
        self.ad=ad
        self.soyad=soyad
        self.yas=yas
        self.cins=cins
        
i=insan("nes","celik",24,"kadin")
print(i.ad)



#python private çalışma


class bankaHesap(object):
    def __init__(self,ad,soyad,para):
        self.ad=ad
        self.soyad=soyad
        self.__para=para #private hale getirdim erişim enegelli iç methodla erişim yapılabilir
        
    def adDegis(self,ad): #SetAd da denilebilir 
        self.ad=ad
        return self.ad
    def adSoyle(self): #setAd da denilebilir cem hoca taktiği doğru mu yanlış mı bilmiyorum zaman gösterecek
        return self.ad
    def soyadDegis(self,soyad):
        self.soyad=soyad
        return self.soyad
    
    def soyadSoyle(self):
        return self.soyad
    
    def paraMiktarDegis(self,miktar):
        self.__para=miktar
        
    def paraMiktarKac(self): #getParaMiktar
        return self.__para
    
    def tanit(self):
        print("\nMerhaba \nSayın {} {} hesap bakiyeniz : {} TL'dir\nİyi günler dileriz. "
              .format(self.adSoyle(),self.soyadSoyle(),self.paraMiktarKac()))
i=bankaHesap("nes","celik",2000)
i.tanit()
i.paraMiktarDegis(5000)
i.tanit()




