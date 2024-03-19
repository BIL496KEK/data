import json

dosya_yolu = "genel.json"
cikis_dosyasi_yolu = "genel.jsonl"

def json_to_jsonl(dosya_yolu, cikis_dosyasi_yolu):
    # JSON dosyasını okuma, encoding'i 'utf-8' olarak ayarlama
    with open(dosya_yolu, 'r', encoding='utf-8') as dosya:
        veriler = json.load(dosya)  # Birden fazla kitap yorumunu içeren bir liste bekleniyor

    # .jsonl dosyası olarak kaydetme, encoding'i 'utf-8' olarak ayarlama
    with open(cikis_dosyasi_yolu, "w", encoding='utf-8') as dosya:
        for veri in veriler:
            # İkinci tip mesajları içeren tam formatı oluşturma
            tam_format = {
                "messages": [
                    {"role": "system", "content": "Genel kategorisindeki yorumu alınacak. Özelliklerine göre durum dönecek."},
                    {"role": "user", "content": veri["yorum"]},
                    {
                        "role": "assistant",
                        "content": ", ".join([f"{key}: {value}" for key, value in veri["özellikler"].items()])
                    }
                ]
            }

            # Tam formatı bir satır olarak yazma ve ensure_ascii=False kullanma
            dosya.write(json.dumps(tam_format, ensure_ascii=False) + '\n')

# Bu fonksiyonu çağırarak işlemi gerçekleştir
# Örnek kullanım: json_to_jsonl('girdi_dosyasi.json', 'cikis_dosyasi.jsonl')
json_to_jsonl(dosya_yolu, cikis_dosyasi_yolu)

