import random
import time


print("""
******************************************************************
                       Sayı Tahmin oyunu
      
                1 ile 40 arası sayı tahmini yapın
            *Programı sonlandırmak için 
******************************************************************
      """)
tus = 
rastgele_sayı = random.randint(1,20)
tahmin_hakkı = 4
while True:
    
    tahmin = (input("Tahmininiz :"))
    
    if(tahmin == tus):
            print("Program sonlandırılıyor...")
            break
    else:
        tahmin = int(tahmin)
        if(tahmin <= 20 and tahmin >= 1):
            if (tahmin == rastgele_sayı):
                print("Tahmin ettiğiniz '{}' sayısı doğru ".format(rastgele_sayı))
                break

            if (tahmin_hakkı == 0):
                print("Tahmin hakkınız bitti! Sayı '{}' olucaktı. => ".format(rastgele_sayı))    
                break
        
            elif (tahmin < rastgele_sayı):
                print("Bilgiler sorgulanıyor...")
                time.sleep(1.5)
        
                if(tahmin == 0):
                    break
                elif (tahmin != 0):
                    print("Daha yüksek bir sayı giriniz...")
                    tahmin_hakkı -= 1
                    time.sleep(0.5)
        
            elif (tahmin > rastgele_sayı):
                print("Bilgiler sorgulanıyor...")
                time.sleep(1.5)
        
                print("Daha düşük bir sayı giriniz...")
                tahmin_hakkı -= 1
                time.sleep(0.5)
        
            if (tahmin == rastgele_sayı):
                print("Bilgiler sorgulanıyor...")
                time.sleep(1.5)
                print("Doğru sayı bulundu : ",rastgele_sayı,"\nHoşçakalın...")
                break
        else:
            print("Lütfen 1 ile 40 arasında bir sayı giriniz")