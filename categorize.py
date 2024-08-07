import os
import shutil

# İndirilenler klasörünün yolu
indirilenler_dosyasi = os.path.expanduser('~/Downloads')

# Kategorilere göre klasörler
klasorler = {
    'Resimler': ['.jpg', '.jpeg', '.png', '.gif', '.bmp',".webp",".HEIC"],
    'Belgeler': ['.pdf', '.doc', '.docx', '.txt', '.xls', '.xlsx',".csv",".ppt",".pptx"],
    'Müzik': ['.mp3', '.wav', '.flac'],
    'Videolar': ['.mp4', '.avi', '.mkv', '.mov'],
    'Arşivler': ['.zip', '.rar', '.tar', '.gz',".7z"],
    'Diğer': []
}

# Kategorilere göre dosyaları taşı
for dosya_adi in os.listdir(indirilenler_dosyasi):
    dosya_yolu = os.path.join(indirilenler_dosyasi, dosya_adi)
    if os.path.isfile(dosya_yolu):
        # Dosya uzantısını al
        _, uzanti = os.path.splitext(dosya_adi)
        # Dosya uzantısına göre ilgili klasörü bul
        hedef_klasor = None
        for klasor, uzantilar in klasorler.items():
            if uzanti.lower() in uzantilar:
                hedef_klasor = klasor
                break
        if hedef_klasor is None:
            hedef_klasor = 'Diğer'
        
        # Hedef klasörün tam yolunu oluştur
        hedef_klasor_yolu = os.path.join(indirilenler_dosyasi, hedef_klasor)
        if not os.path.exists(hedef_klasor_yolu):
            os.makedirs(hedef_klasor_yolu)
        
        # Dosyayı hedef klasöre taşı
        yeni_dosya_yolu = os.path.join(hedef_klasor_yolu, dosya_adi)
        shutil.move(dosya_yolu, yeni_dosya_yolu)

print("Dosyalar kategorize edilerek taşındı.")
