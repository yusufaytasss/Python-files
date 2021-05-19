import random
import time

print("""
******************************************************************
                       Sayı Tahmin oyunu
      
                1 ile 40 arası sayı tahmini yapın
******************************************************************
      """)
rastgele_sayı = random.randint(1,40)
tahmin_hakkı = 7
while True:
    
    tahmin = int(input("Tahmininiz :"))
    
    if(tahmin <= 40 and tahmin >= 1):
        if (tahmin < rastgele_sayı):
            print("Bilgiler sorgulanıyor...")
            time.sleep(1.5)
        
            print("Daha yüksek bir sayı giriniz...")
            tahmin_hakkı -= 1
    
        elif (tahmin > rastgele_sayı):
            print("Bilgiler sorgulanıyor...")
            time.sleep(1.5)
        
            print("Daha düşük bir sayı giriniz...")
            tahmin_hakkı -= 1
        
        else:
            print("Bilgiler sorgulanıyor...")
            time.sleep(1.5)
            print("Doğru sayı bulundu : ",rastgele_sayı)
            break
        if (tahmin_hakkı == 0):
            print("Tahmin hakkınız bitti !",rastgele_sayı,"\n Hoşçakalın...")    
            break
    else:
        print("Lütfen 1 ile 40 arasında bir sayı giriniz")

    