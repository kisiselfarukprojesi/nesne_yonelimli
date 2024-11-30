import random
import time

class kumanda():
    def __init__(self, tv_durum='kapali', ses=0, kanallar=['trt'], kanal='trt'):
        self.tv_durum= tv_durum
        self.ses= ses
        self.kanallar= kanallar
        self.kanal= kanal


    def tv_ac(self):
        if(self.tv_durum=='acik'):
           print("zaten açık")
        else: 
            print("açılıyor...") 
            self.tv_durum='acik'


    def tv_kapat(self):
        if(self.tv_durum=='kapali'):
           print("kapali")
        else: 
            print("kapanıyor...") 
            self.tv_durum='kapali'
    def ses_ayarı(self):
        while True:
            cevap= input("sesi azalt '<'\n sesi arttır '>'\n çıkış:'c' ")
            if cevap=='<':
                if(self.ses != 0):
                    self.ses -=1
                    print(f"ses: {self.ses}")
            elif cevap =='>':
                if(self.ses !=30):
                    self.ses +=1
                    print(f"ses: {self.ses}")
            else:
                print(f"ses güncellendi..{self.ses}")
                break
    

    def kanal_ekle(self,kanal_ismi):
        print("kanal ekleniyor...")
        time.sleep(1)
        self.kanallar.append(kanal_ismi)
        print("kanal eklendi!!")



    def rastgele_kanal(self):
        rastgele= random.randint(0,len(self.kanallar)-1)
        self.kanal=self.kanallar[rastgele]
        print(f"şuanki kanal: {self.kanal}")

    def __len__(self):
        return len(self.kanallar)
    
    def __str__(self)->str:
        return f"tv durumu:{self.tv_durum}\nkanal listesi: {self.kanallar}\n şuanki kanal:{self.kanal}"


kumanda = kumanda()
""""
Televizyon Uygulaması


1. Tv Aç

2. Tv Kapat

3. Ses Ayarları

4. Kanal Ekle

5. Kanal Sayısını Öğrenme

6. Rastgele Kanala Geçme

7. Televizyon Bilgileri

Çıkmak için 'q' ya basın.
"""


while True:

    işlem = input("İşlemi Seçiniz:")

    if (işlem == "q"):
        print("Program Sonlandırılıyor...")
        break

    elif (işlem == "1"):
        kumanda.tv_ac()
    elif (işlem == "2"):
        kumanda.tv_kapat()

    elif (işlem == "3"):
        kumanda.ses_ayarı()

    elif (işlem == "4"):
        kanallar = input("Kanal isimlerini ',' ile ayırarak girin:")

        kanallar = kanallar.split(",")

        for eklenecekler in kanallar:
            kumanda.kanal_ekle(eklenecekler)
    elif (işlem == "5"):

        print("Kanal Sayısı:",len(kumanda))

    elif (işlem == "6"):
        kumanda.rastgele_kanal()
    elif (işlem == "7"):
        print(kumanda)

    else:
        print("Geçersiz İşlem......")

        