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
'''
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