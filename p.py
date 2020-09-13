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
'''
#----------------------------------------------------------------------------------#
#-----------------------------Kontrol yapıları-------------------------------------#

    #if else yapıları
    x=2
    y=3

    if y>x:
        print('büyük sayı y')
    
    elif x>y:
        print('büyük sayı x')
        