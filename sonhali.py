import random,time

print("""
******************************************************************
                       Sayı Tahmin oyunu

                1 ile 40 arası sayı tahmini yapın
            *Programı sonlandırmak 'stop' yazmanız yeterli
******************************************************************
      """)

durdur = "stop"
random_number = random.randint(1,35)
tahmin_hakkı = 6
while True:
    tahmin = (input("Tahmininiz :"))
    if (tahmin == durdur):
        print("Program sonlandırılıyor...")
        break
    else:
        tahmin = int(tahmin)
        if (tahmin <= 35 and tahmin >=1):
            if (tahmin == random_number):
                print("Tahmin ettiğiniz '{}' sayısı doğru ".format(random_number))
                break
            if (tahmin_hakkı == 0):
                print("Tahmin hakkınız bitti! Sayı '{}' olucaktı.  ".format(random_number))
                break
            elif (tahmin < random_number):
                print("Bilgiler sorgulanıyor...")
                time.sleep(1.5)
                if(tahmin == 0):
                    break
                elif (tahmin != 0):
                    print("Daha yüksek bir sayı giriniz...")
                    tahmin_hakkı -= 1
                    time.sleep(0.5)
            elif (tahmin > random_number):
                print("Bilgiler sorgulanıyor...")
                time.sleep(1.5)
                print("Daha düşük bir sayı giriniz...")
                tahmin_hakkı -=1
                time.sleep(0.5)
            elif (tahmin_hakkı == random_number):
                print("Bilgiler sorgulanıyor...")
                time.sleep(1.5)
                print("Doğru sayı bulundu : '{}'",format(random_number))
                break
        else:
            print("Lütfen 1 ile 35 arasında bir sayı giriniz")
#Geliştirmeye devam