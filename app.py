import random
import os
import time

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def menu():
    clear()
    print("- Oyunlar -\n")
    print("1.Taş Kağıt Makas Oyunu")
    print("2.Zar Atma Oyunu")
    print("3.Hikaye Oyunu")
    print("4.Çıkış Yapınız")

    secim = input("Seçiminizi Yapınız: ")

    if secim == "1":
        clear()
        tkm()
    elif secim == "2":
        clear()
        zar()
    elif secim == "3":
        clear()
        hikaye()
    elif secim == "4":
        clear()
        print("Çıkış Yapılıyor...\n")
        clear()
        print("3 Saniye İçinde Kapanacaktır")
        time.sleep(1)
        print("2 Saniye İçinde Kapanacaktır")
        time.sleep(1)
        print("1 Saniye İçinde Kapanacaktır")
        time.sleep(1)
        clear()
        exit()
    else:
        clear()
        print("Yanlış Seçim! Tekrar Menüye Gitmek İçin Lütfen 3 Saniye Bekleyiniz...")
        time.sleep(1)
        clear()
        print("Yanlış Seçim! Tekrar Menüye Gitmek İçin Lütfen 2 Saniye Bekleyiniz...")
        time.sleep(1)
        clear()
        print("Yanlış Seçim! Tekrar Menüye Gitmek İçin Lütfen 1 Saniye Bekleyiniz...")
        time.sleep(1)
        clear()
        print("Yanlış Seçim! Tekrar Menüye Gitmek İçin Lütfen 0 Saniye Bekleyiniz...")
        clear()
        menu()
    
def tkm():

    print("Taş Kağıt Makas Oyununa Hoş Geldin...")
    secenekler = ["taş","kağıt","makas"]
    k_secim = input("Seçiminizi Yapınız: ")
    pc_secim = random.choice(secenekler)

    clear()
    print("Sonuç Açıklanıyor! 2 Saniye Bekleyiniz")
    time.sleep(1)
    clear()
    print("Sonuç Açıklanıyor! 1 Saniye Bekleyiniz")
    time.sleep(1)
    clear
    print(f"Senin Seçimin: {k_secim}")
    print(f"Bilgisayar Seçimi: {pc_secim}")

    if k_secim == pc_secim:
        print("Berabere!")
    elif k_secim == "kağıt" and pc_secim == "taş":
        print("Sen Kazandın!")
    elif k_secim == "taş" and pc_secim == "makas":
        print("Sen Kazandın!")
    elif k_secim == "makas" and pc_secim == "kağıt":
        print("Sen Kazandın")
    else:
        print("Bilgisayar Kazandı!")

    tekrar = input("Devam Etmek İster Misiniz y/n: ")
    if tekrar == "y":
        clear()
        tkm()
    else:
        menu_secim = input("Menüye Gitmek İster Misin y/n: ")
        if menu_secim == "y":
            clear()
            menu()
        else:
            clear()
            print("Çıkış Yapılıyor...\n")
            clear()
            print("3 Saniye İçinde Kapanacaktır")
            time.sleep(1)
            print("2 Saniye İçinde Kapanacaktır")
            time.sleep(1)
            print("1 Saniye İçinde Kapanacaktır")
            time.sleep(1)
            clear()
            exit()

def zar():
    clear()
    zar_at = input("Zar Atmak İçin 'y' Tuşuna Basınız: ")
    
    if zar_at == "y":
        clear()
        print("Zar Atılıyor! 2 Saniye Bekleyiniz")
        time.sleep(1)
        clear()
        print("Zar Atılıyor! 1 Saniye Bekleyiniz")
        time.sleep(1)
        clear()

        zar_sonuc = random.randint(1,6)
        print(f"Zar Sonuç: {zar_sonuc}")
        
        tekrar = input("Devam Etmek İster Misiniz y/n: ")
        if tekrar == "y":
            clear()
            zar()
        else:
            menu_secim = input("Menüye Gitmek İster Misin y/:n ")
            if menu_secim == "y":
                clear()
                menu()
            else:
                print("Çıkış Yapılıyor...\n")
                clear()
                print("3 Saniye İçinde Kapanacaktır")
                time.sleep(1)
                print("2 Saniye İçinde Kapanacaktır")
                time.sleep(1)
                print("1 Saniye İçinde Kapanacaktır")
                time.sleep(1)
                clear()
                exit()

def hikaye():

    print("- Hikaye Oyununa Hoş Geldiniz -\n\n")

    user = input("Kendi Adınızı Giriniz: ")
    print(f"\nKendi Adınız {user} Olarak Belirlendi")
    enemy = input("\nRakip Kişinin Adını Giriniz: ")
    print(f"\nRakip Kişinin Adı {enemy} Olarak Belirlendi\n")
    user_power = input("Gücünüzü Giriniz: ")
    print(f"\n{user} Gücünü {user_power} olarak tanımladı")
    enemy_power = input("Rakip Gücünü Giriniz: ")
    print(f"{enemy} Gücünü {enemy_power} Olarak Tanımladı")


    story = f"""Sisli bir gecede {user} yolda ilerliyordu. Evinin sokağına döndükten birkaç adım sonra, yanında şapkalı birini fark etti. Bu kişi, azılı suçlu {enemy}’den başkası değildi.
{user}, onun nasıl biri olduğunu çok iyi biliyordu. Bu yüzden sessizce arkasından yaklaşarak {user_power} gücünü kullanmaya karar verdi.
Ancak {enemy}, hafife alınacak biri değildi. {user} ne kadar uğraşsa da, {enemy} bir şekilde kaçmayı başarıyordu.
Fakat sonunda {user}, yanındaki rampayı fırsat bilerek hız aldı. Görkemli sesiyle haykırarak, bütün gücünü topladı ve {user_power}’ı doğrudan {enemy}’nin kafasına uyguladı.
{enemy} ayağa kalkmaya çalıştı ama nafileydi… {user}, onu nihayet alt etmişti!"""    

    print(f"\nHikaye Tasarlanıyor 5 Saniye Lütfen Bekleyiniz. \nKendi Adınız: {user}\nDüşman Adı: {enemy}\n")
    time.sleep(1)
    clear()
    print(f"\nHikaye Tasarlanıyor 4 Saniye Lütfen Bekleyiniz. \nKendi Adınız: {user}\nDüşman Adı: {enemy}\n")
    time.sleep(1)
    clear()
    print(f"\nHikaye Tasarlanıyor 3 Saniye Lütfen Bekleyiniz. \nKendi Adınız: {user}\nDüşman Adı: {enemy}\n")
    time.sleep(1)
    clear()
    print(f"\nHikaye Tasarlanıyor 2 Saniye Lütfen Bekleyiniz. \nKendi Adınız: {user}\nDüşman Adı: {enemy}\n")
    time.sleep(1)
    clear()
    print(f"\nHikaye Tasarlanıyor 1 Saniye Lütfen Bekleyiniz. \nKendi Adınız: {user}\nDüşman Adı: {enemy}\n")
    time.sleep(1)
    clear()
    print(f"\n Hikaye Yüklendi!")
    time.sleep(1)
    clear()

    print(story)    

    tekrar = input("Devam Etmek İster Misiniz y/n: ")
    if tekrar == "y":
        clear()
        tkm()
    else:
        menu_secim = input("Menüye Gitmek İster Misin y/n: ")
        if menu_secim == "y":
            clear()
            menu()
        else:
            clear()
            print("Çıkış Yapılıyor...\n")
            clear()
            print("3 Saniye İçinde Kapanacaktır")
            time.sleep(1)
            print("2 Saniye İçinde Kapanacaktır")
            time.sleep(1)
            print("1 Saniye İçinde Kapanacaktır")
            time.sleep(1)
            clear()
            exit()

menu()