'''
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
        print("\nSeçtiğiniz meyve :", secim, "\nİstediğiniz miktar :", kilo,"kilo", "\nÖdemeniz greken tutar :", fiyat , "TL")

    elif kilo == 2:
        print("\nSeçtiğiniz meyve :", secim, "\nİstediğiniz miktar :", kilo,"kilo","\nÖdemeniz greken tutar :", fiyat * 2,"TL")

    elif kilo ==3:
        print("\nSeçtiğiniz meyve :", secim, "\nİstediğiniz miktar :", kilo,"kilo", "\nÖdemeniz greken tutar :", fiyat * 3, "TL")

    else:
        print("\nManavda istediğiniz miktarda meyve bulunmamaktadır!")


elif secim == 'armut':
    kilo = int(input('kaç kilo istiyorsunuz :'))
    fiyat = 5  # Type int

    if kilo == 1:
        print("\nSeçtiğiniz meyve :", secim, "\nİstediğiniz miktar :", kilo, "kilo","\nÖdemeniz greken tutar :", fiyat , "TL")

    elif kilo == 2:
        print("\nSeçtiğiniz meyve :", secim, "\nİstediğiniz miktar :", kilo, "kilo","\nÖdemeniz greken tutar :", fiyat * 2, "TL")

    elif kilo ==3:
        print("\nSeçtiğiniz meyve :", secim, "\nİstediğiniz miktar :" ,kilo,"kilo","\nÖdemeniz greken tutar :", fiyat * 3, "TL")

    else:
        print("\nManavda istediğiniz miktarda meyve bulunmamaktadır!")


elif secim == 'üzüm':
    kilo = int(input('kaç kilo istiyorsunuz :'))
    fiyat = 7  # Type int

    if kilo == 1:
        print("\nSeçtiğiniz meyve :", secim, "\nİstediğiniz miktar :", kilo, "kilo","\nÖdemeniz greken tutar :", fiyat , "TL")

    elif kilo == 2:
        print("\nSeçtiğiniz meyve :", secim, "\nİstediğiniz miktar :", kilo, "kilo","\nÖdemeniz greken tutar :", fiyat * 2, "TL")

    elif kilo ==3:
        print("\nSeçtiğiniz meyve :", secim, "\nİstediğiniz miktar :" ,kilo,"kilo","\nÖdemeniz greken tutar :", fiyat * 3, "TL")

    else:
        print("\nManavda istediğiniz miktarda meyve bulunmamaktadır!")


elif secim == 'muz':
    kilo = int(input('kaç kilo istiyorsunuz :'))
    fiyat = 11  # Type int

    if kilo == 1:
        print("\nSeçtiğiniz meyve :", secim, "\nİstediğiniz miktar :", kilo, "kilo","\nÖdemeniz greken tutar :", fiyat , "TL")

    elif kilo == 2:
        print("\nSeçtiğiniz meyve :", secim, "\nİstediğiniz miktar :", kilo, "kilo","\nÖdemeniz greken tutar :", fiyat * 2, "TL")

    elif kilo ==3:
        print("\nSeçtiğiniz meyve :", secim, "\nİstediğiniz miktar :" ,kilo,"kilo","\nÖdemeniz greken tutar :", fiyat * 3, "TL")

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

# Girilen iki sayı arasındaki asal ve asal olmayan sayıları bulma
asalSayi=[]
asalOlmayan=[]
sayi1 = int(input("Lütfen 1.sayıyı giriniz : "))
sayi2 = int(input("Lütfen 2.sayıyı giriniz : "))

print(sayi1," ile ",sayi2," arasındaki asal sayılar şunlardır : \n")
for i in range(sayi1, sayi2+1):
    if i>1:
        for k in range(2,i):
            if (i%k)==0 :
                asalOlmayan.append(i)
                break

        else:
            asalSayi.append(i)
print(asalSayi)
print("Girilen sayılar arasında ",len(asalSayi)," tane asal sayı vardır \n\n")
print(asalOlmayan)
print("Girilen sayılar arasında ",len(asalOlmayan)," asal olmayan sayı vardır ")


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



'''