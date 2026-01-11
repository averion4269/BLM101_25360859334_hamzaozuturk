# Proje Teslim Raporu

## 1. Öğrenci Bilgileri
Ad Soyad: hamza ozuturk
Öğrenci Numarası:25360859334


---

## 2. Proje Konusu
Python ile Otomatik HTML Sayfası Oluşturucu
---

## 3. YouTube Sunum Linki
Projemin çalışma mantığını ve ekran çıktısını anlattığım videoya aşağıdaki bağlantıdan ulaşabilirsiniz:

https://youtu.be/DQKnQEX6ULk

*(Not: Linkin üzerine tıklayarak videoya gidebilirsiniz.)*

---

## 4. Proje Açıklaması ve Dokümantasyon

### A. Kod Ne Yapar?
Bu program, HTML veya CSS bilgisi olmayan bir kullanıcının, sadece terminal üzerinden soruları cevaplayarak kendine ait şık bir **"Kişisel Portföy Web Sitesi"** oluşturmasını sağlar.
Program çalıştırıldığında kullanıcıya adını, biyografisini ve aldığı dersleri sorar. Bu verileri arka planda işleyerek renkli ve düzenli bir `index.html` dosyası üretir ve işlem bittiğinde sayfayı otomatik olarak tarayıcıda açar.

### B. Nasıl Çalıştırılır? (Kurulum)
Bu proje Python'un kendi standart kütüphanelerini kullanır, bu yüzden **harici bir kütüphane kurulumuna (pip install vb.) gerek yoktur.**

1.  Bilgisayarınızda Python'un yüklü olması yeterlidir.
2.  `main.py` (veya dosya adınız neyse) dosyasının olduğu klasörde terminali açın.
3.  Aşağıdaki komutu yazın:
    ```bash
    python main.py
    ```
4.  Konsoldaki soruları cevaplayın ve `Enter` tuşuna basın.

### C. Kodun Çalışma Mantığı (Algoritma)

Kod, temel olarak **Girdi (Input) -> İşleme (Process) -> Çıktı (Output)** mantığıyla 3 ana aşamada çalışır:

#### 1. Veri Girişi (Input)
* Python'un `input()` fonksiyonu kullanılarak kullanıcı ile etkileşime geçilir.
* Kullanıcıdan "Dersler" bilgisi tek bir satırda, virgülle ayrılmış şekilde (Örn: "Matematik, Fizik, Kodlama") istenir.

#### 2. Veri İşleme (String Manipulation)
* **Listeye Çevirme:** Kullanıcının girdiği dersler string'i, `split(',')` metodu ile parçalanarak bir Python listesine dönüştürülür.
* **Temizleme:** `strip()` metodu ile her bir dersin başındaki ve sonundaki gereksiz boşluklar temizlenir.
* **HTML Döngüsü:** Bir `for` döngüsü ile listedeki her eleman, HTML'in `<li>` (Liste elemanı) etiketleri arasına yerleştirilir.
* **F-String:** Python'un `f-string` yapısı kullanılarak, hazırlanan bu dinamik veriler (Ad, Biyografi, Liste), önceden CSS ile stillendirilmiş HTML şablonunun içine gömülür.

#### 3. Dosya Çıktısı (File I/O)
* **Encoding:** Türkçe karakterlerin (ğ, ş, ı vb.) tarayıcıda bozuk görünmemesi için dosya açma işleminde `encoding='utf-8'` parametresi özellikle kullanılmıştır.
* **Dosya Yazma:** `open()` fonksiyonu `w` (write) modunda açılarak `index.html` dosyası oluşturulur.
* **Otomasyon:** İşlem hatasız tamamlanırsa, `webbrowser` modülü devreye girer ve oluşturulan sayfa kullanıcının varsayılan internet tarayıcısında otomatik olarak açılır
