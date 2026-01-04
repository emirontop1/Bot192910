from instagrapi import Client
import time

# --- BİLGİLERİNİ BURAYA YAZ ---
# Tırnak işaretlerini kaldırma!
KULLANICI_ADI = "denem_ebotu1282919172" 
SIFRE = "Kdşwöemelw2ğwğK;÷>2[+]82]10"

cl = Client()

def botu_baslat():
    try:
        print("Sisteme giriş yapılıyor...")
        cl.login(KULLANICI_ADI, SIFRE)
        print("Giriş başarılı! Mesajlar taranıyor...")

        while True:
            # Okunmamış mesajları al
            threads = cl.direct_threads()
            for thread in threads:
                if thread.unread_count > 0:
                    # En son gelen mesajı al
                    last_msg = thread.messages[0]
                    gelen_metin = last_msg.text.lower()
                    
                    print(f"Yeni mesaj geldi: {gelen_metin}")

                    # Eğer mesajda "merhaba" geçiyorsa cevap ver
                    if "merhaba" in gelen_metin:
                        cl.direct_answer(thread.id, f"Merhaba! Bana '{last_msg.text}' dedin, ben bir botum.")
                        print("Cevap gönderildi.")
            
            # Instagram'ın seni engellememesi için 30 saniye bekle
            time.sleep(30)
            
    except Exception as e:
        print(f"Bir hata oluştu: {e}")
        time.sleep(60)

if __name__ == "__main__":
    botu_baslat()
