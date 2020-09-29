def topla(a,b):
    return a+b
def cikar(a,b):
    return a-b
def carp(a,b):
    return a*b
def bol(a,b):
    return a/b
def kontrol():
    deger=None
    secim=input("\nÇIKIŞ için X 'basın !\n Devam etmek için herhangi bir tuşa basın !  ")
    if secim=="x" or secim=="X":
        print("\nÇıkış yapıldı !")
        deger=True
    else:
        deger=False
        return deger
while True:
    try:
        secim=int(input("\n\n1-Toplama\n2-Çıkarma\n3-Çarpma\n4-Bölme\n\nLütfen bir seçim yapınız : "))


        if secim==1:
            sayi1 = float(input("1. sayı : "))
            sayi2 = float(input("2. sayı : "))
            sonuc=topla(sayi1,sayi2)
        elif secim == 2:
            sayi1 = float(input("1. sayı : "))
            sayi2 = float(input("2. sayı : "))
            sonuc=cikar(sayi1, sayi2)
        elif secim == 3:
            sayi1 = float(input("1. sayı : "))
            sayi2 = float(input("2. sayı : "))
            sonuc=carp(sayi1, sayi2)
        elif secim == 4:
            sayi1 = float(input("1. sayı : "))
            sonuc=sayi2 = float(input("2. sayı : "))
            sonuc=bol(sayi1, sayi2)
        elif secim<1 or secim>4:
            print("\nHatalı karakter girdiniz \nÇıkış Yaptınız !")


        print("Sonuc = {}".format(sonuc))
        if kontrol():
            break

    except ValueError:
        print("\nHatalı karakter girdiniz !\n")
        break


