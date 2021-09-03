from gtts import gTTS
import os


try:
    dosya=open("yazi.txt","r").read()
    ##dosya="Bu dosya python ile oluşturulmuş bir ses dosyasıdır verilen metin dosyaları bu program sayesinde ses dosyasına dönüştürülür."
    konusma=gTTS(text=dosya, lang="tr",slow=False)
    konusma.save("ses.mp3")
    os.system("ses.mp3")
except IOError:
    print("bir hata oluştu!")
finally:
    dosya.close()
