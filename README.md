# Parçacık Kalbi · Particle Heart

Siyah zeminde pembe çizgilerden kalem gibi tek tek çizilen, sonra atmaya başlayan bir kalp animasyonu.
Tek bir HTML dosyası; kurulum ve internet gerektirmez.

*A pink particle heart drawn stroke by stroke like Python turtle, then beating. One offline HTML file.*

## Açma
- **Bilgisayarda:** `index.html` dosyasına çift tıkla.
- **Telefonda:** Bilgisayar ve telefon aynı Wi-Fi'dayken `TELEFONDA-AC.bat` dosyasını çalıştır ve ekranda yazan `http://` adresini telefonun tarayıcısında aç. Node.js gerekir.
- **Python sürümü:** `python parcacik_kalbi.py` (Python 3 ve Tk gerekir).

## Özellikler
- Kalp formülü `x = 16 sin³t`, `y = 13 cos t − 5 cos 2t − 2 cos 3t − cos 4t` ile çizilen 1000 + 3500 çizgi
- Turtle tarzı çizim: her çizgi uzayarak belirir, ucunda parlak bir kalem noktası
- Çizim bitince iki vuruşlu kalp atışı, nefes alan pembe ışıma, kıvılcımlar ve yükselen toz
- **Dokun:** kalp dağılır ve yeniden toplanır · **Sürükle:** parçacıklar kenara kaçar · **Çift dokun:** baştan çizer

Ayrıntılar için `OKU-BENI.txt` dosyasına bak.
