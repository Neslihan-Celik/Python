import qrcode

qr=qrcode.QRCode(version=1,
    error_correction =qrcode.constants.ERROR_CORRECT_L,
    box_size=20,
    border=5)


giden_veri="Merhaba Ben NES bu qr kodu gorup kaynak koduna ulasmak isterseniz eger su linke tiklayabilirsiniz -> https://github.com/Neslihan-Celik/Python/tree/master/qr_kod_olusturucu"
qr.add_data(giden_veri)
qr.make(fit=True)

resim=qr.make_image(fill_color="black",back_color="white")
resim.save("qr_code.png")