import os
import webbrowser  # Sayfayı otomatik açmak için

def web_sayfasi_olustur():
    print("--- HTML Web Sayfası Oluşturucu ---\n")

    # 1. KULLANICIDAN BİLGİLERİ AL
    ad_soyad = input("Adınız ve Soyadınız: ")
    biyografi = input("Kısa Biyografiniz: ")
    dersler_input = input("Aldığınız dersleri virgül ile ayırarak yazın: ")

    # Dersleri listeye çevir ve HTML listesi hazırla
    ders_listesi = dersler_input.split(',')
    dersler_html_kodu = ""
    
    for ders in ders_listesi:
        # .strip() komutu ders adının başındaki/sonundaki boşlukları temizler
        dersler_html_kodu += f"        <li>{ders.strip()}</li>\n"

    # 2. HTML ŞABLONU (CSS Dahil)
    # Türkçe karakterler için <meta charset="UTF-8"> eklendi.
    # CSS'deki süslü parantezlerin karışmaması için {{ }} kullanıldı.
    
    html_icerigi = f"""
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{ad_soyad} - Kişisel Sayfa</title>
    <style>
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: #f4f6f7;
            color: #333;
            max-width: 800px;
            margin: 40px auto;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }}
        h1 {{
            color: #2c3e50;
            text-align: center;
            border-bottom: 2px solid #3498db;
            padding-bottom: 15px;
        }}
        .bio-box {{
            background-color: #ffffff;
            padding: 20px;
            border-left: 5px solid #e67e22;
            margin-bottom: 20px;
            font-size: 1.1em;
        }}
        h3 {{ color: #2980b9; }}
        ul {{
            background-color: #fff;
            padding: 20px 40px;
            border-radius: 5px;
        }}
        li {{ margin-bottom: 8px; }}
    </style>
</head>
<body>

    <h1>{ad_soyad}</h1>
    
    <h3>Hakkımda</h3>
    <div class="bio-box">
        {biyografi}
    </div>
    
    <h3>Aldığım Dersler</h3>
    <ul>
{dersler_html_kodu}
    </ul>
</body>
</html>
    """

    # 3. DOSYAYI KAYDETME (encoding="utf-8" ÖNEMLİ!)
    dosya_adi = "index.html"
    
    try:
        # Türkçe karakterler bozulmasın diye encoding="utf-8" ekledik
        with open(dosya_adi, "w", encoding="utf-8") as dosya:
            dosya.write(html_icerigi)
        
        # Dosyanın tam yolunu bul
        tam_yol = os.path.abspath(dosya_adi)
        print(f"\nBaşarılı! Dosya oluşturuldu: {tam_yol}")
        
        # 4. OTOMATİK OLARAK TARAYICIDA AÇ
        print("Sayfa tarayıcınızda açılıyor...")
        webbrowser.open(f"file://{tam_yol}")

    except Exception as hata:
        print(f"Bir hata oluştu: {hata}")

# Programı Başlat
if __name__ == "__main__":
    web_sayfasi_olustur()