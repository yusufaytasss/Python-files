import time,random
print("""
             *SİSTEME HOŞGELDİNİZ*
""")
time.sleep(1)
print("""
        -YAPMAK İSTEDİĞİNİZ İŞLEMİ SEÇİNİZ-

        1.Sisteme Giriş
        2.Kayıt Olma
        3.Şifremi Unuttum
        4.Çıkış
""")
time.sleep(2)
işlem = int(input("Yapmak istediğiniz işlemi seçiniz : ")) #İşlem girişi
time.sleep(2)
while True:
    #ADMİN GİRİŞİ ve KULLANICI GİRİŞİ
    if(işlem == 1): #SİSTEME GİRİŞ bölümü işlemden alınan değer 1 e eşit ise koşulları döndürür
        print("Şifrenizi unuttuysanız şifre bölümüne 'şifremi unuttum' yazabilirsiniz.") #ikinci bir yedek olarak login bölümüne de şifremi unuttum kısmı koydum
        time.sleep(2)
        kullanıcı_adi = input("Kullanıcı adınızı girin \n : ") #İlk bakışta bir kullanıcı ve şifre tanımlı olmadığı için admin girişi şekilde önceden tanımlı bir admin girişi oluşturdum
        time.sleep(2)
        kullanıcı_şifre = input("Kullanıcı şifrenizi girin \n : ")
        #Kullanıcı girişi şifremi unuttum bölümü
        if(kullanıcı_şifre == "şifremi unuttum"): #Şifremi unuttum bölümündeki text'e 'şifremi unuttum' yazarsak bu if parametresine yönlendirliyoruz.
            print("ŞİFRE KURTARMAYA HOŞGELDİNİZ")
            time.sleep(1.5)
            print("Bilgiler alınıyor...")
            time.sleep(3)
            kurtarma = int(input("Lütfen kurtarma kodunu giriniz : ")) #kurtarma kodu ilk başta tanımı gelmiyor fakat kayıt(record) olduktan sonra random bi tanımlı kod bize sunuluyor
            #Kurtarma kodu aktif etme
            if(kurtarma == random_kod): #girilen kod ile oluşturulan random kodun birbirine eşit olup olmadığını kontrol ediyor. Eşit ise if döngüsüne giriş yapıyor.
                print("Sisteme giriş yapıldı, Şifrenizi yenilemek ister misiniz ? (E/H)") #Burda ekstra olarak şifresini yenilemek isteyip istemediğini sormak kullanıcı için büyük bir avantaj yaratacaktır.
                soru = input("Seçiminiz : ")
                if(soru == "E"):
                    print("Şifre yenileme işlemi gerçekleştiriliyor...")
                    time.sleep(5)
                    yeni_şifre = input("Yeni Şifrenizi Giriniz : ")
                    time.sleep(3)
                    print("Şifre değiştirme gerçekleştirildi. Programdan çıkılıyor...")
                    exit()
            else:
                print("Kurtarma kodu hatalı, sistemden çıkış yapılıyor!") #random kodun hatalı olması durumnda yapılacak işlemi denetliyor.
                exit()
        #Giriş
        if(kullanıcı_adi == "admin" and kullanıcı_şifre == "admin123" or kullanıcı_adi == yeni_kullanıcı_adı and kullanıcı_şifre == yeni_şifre): #Burada admin girişi ve kullanıcı girişini sağlıyoruz
            print("Sisteme başarılı bir şekilde giriş yaptınız !!!")
            break
        else:
            print("Bilgiler alınıyor...")
            time.sleep(3)
            print("Sisteme giriş yaparken bir hata oluştu !")
            time.sleep(1)
            print("Bilgilerinizi tekrardan kontrol ediniz...")
            time.sleep(3)
    #KAYIT OLMA
    if(işlem == 2): #kayıt olma durumu söz konusu
        print("Yeni kayıt oluştururken şifrenizi unutmamaya özen gösterin :) ") #Mini bi uyarı
        time.sleep(2)
        yeni_kullanıcı_adı = input("Kullanıcı adınızı girin : ") # Yeni kullanıcı adı parola gibi login yaparken gerekecek bilgiler isteniliyor.
        yeni_şifre = input("Şifrenizi girin : ") #Çoğu sistemde artık iki farklı kutucukta şifre istiyor. Nedeni de hatalı şifre oluşumunun büyül ölçüde önüne geçmek
        yeni_şifre2 = input("Şifrenizi tekrar girin : ")
        #Parola eşleştirme
        if(yeni_şifre != yeni_şifre2): #Burada iki tane şifrenin aynı olmadığı durumda çalışması gereken kod parçası var.
            hak = 3
            while(yeni_şifre != yeni_şifre2):
                hak -=1
                print("HATA !! Şifreler eşleştirilemiyor : ")
                time.sleep(2)
                print("Şifrenizi Yeniden Giriniz")
                time.sleep(2)
                yeni_şifre = input("Şifrenizi yeniden belirleyiniz : ")
                yeni_şifre2 = input("Şifrenizi yeniden yazınız : ")
                if(hak == 0):
                    print("SİSTEMDEN ATILDINIZ !")      #3 kere deneme yapıldığı için otomatikmen sistemden atılıyor...
                    exit()
            print("KAYIT BAŞARILI !")
        if(yeni_şifre == yeni_şifre2): #Girilen iki şifrenin de doğru olması durumu.
            print("Sisteme hoşgeldi̇ni̇z... Sizi görmek ne güzel")
            time.sleep(3)
            random_kod = random.randint(1,10000)
            print("Şifrenizi veya Kullanıcı adınızı unutursanız '{}' kodunu yazarak sisteme erişim sağlayabilirsiniz...".format(random_kod))
            time.sleep(1.5)
            işlem = int(input("Yapmak istediğiniz işlemi seçiniz : "))
    #ŞİFREMİ UNUTTUM
    if(işlem == 3): #Harici şifre kurtrma bölümümüz.. Kod yapısında değişen pek bir şey yok
        print("ŞİFRE KURTARMAYA HOŞGELDİNİZ")
        time.sleep(1.5)
        print("Bilgiler alınıyor...")
        time.sleep(3)
        kurtarma = int(input("Lütfen kurtarma kodunu giriniz : "))
        if(kurtarma == random_kod):
            print("Sisteme giriş yapıldı, Şifrenizi yenilemek ister misiniz ? (E/H)")
            soru = input("Seçiminiz : ")
        if(soru == "E"):
            print("Şifre yenileme işlemi gerçekleştiriliyor...")
            time.sleep(5)
            yeni_şifre = input("Yeni Şifrenizi Giriniz :")
            time.sleep(3)
            print("Şifre değiştirme gerçekleştirildi. Programdan çıkılıyor...")
            exit()
        elif(soru == "H"):
            print("İşleminiz gerçekleştirildi. Programdan çıkıldı!")
            time.sleep(3)
            exit()
    #ÇIKIŞ
    if(işlem == 4): # son olarak ise exit(çıkış) durumu
        print("Çıkış gerçekleştiriliyor...")
        time.sleep(2)
        print("Hoşçakal!")
        exit()