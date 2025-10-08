Otonom Kargo Aracı

Bu proje, düşük maliyetli bir otonom kargo aracı geliştirmeyi hedefler. Araç, kendi sokaklarında şerit ve engel tespiti yaparak güvenli şekilde hareket edebilir.

Özellikler

Otonom sürüş: Kamera ve makine öğrenmesi kullanarak yol takip ve yön tahmini

Engel algılama: Önündeki engellere göre yön değiştirme

Motor kontrolü: 3 motor (2 arkada, 1 önde) ve L298M motor sürücüler ile Arduino Nano üzerinden kontrol

Geliştirme ortamı: Python ve PyCharm

Makine öğrenmesi modelleri:

Şerit tespiti: Ultra Fast Lane Detection (UFLD) veya benzeri

Yön tahmini: CNN tabanlı regresyon modeli

Sistem Mimarisi
[ Kamera ] --> [ Python ML Modeli (PyCharm) ] --> [ Uygulama / Komut İşleyici ] --> [ Arduino Nano ] --> [ Motorlar ]


Kamera ile alınan görüntü, Python tarafında işlenir.

Araç ve yol verileri analiz edilip karar alınır.

Komutlar Arduino’ya gönderilir ve motorlar yönlendirilir.

Kurulum

Python 3.x yüklü olduğundan emin olun.

Gerekli kütüphaneleri yükleyin:

pip install -r requirements.txt


Arduino Nano'yu uygun şekilde motor sürücülerine bağlayın.

Kamera ile görüntü alabilmek için gerekli izinleri sağlayın.

Kullanım

python main.py ile aracı çalıştırabilirsiniz.

Model ağırlıkları ve konfigürasyon dosyaları models/ klasöründe bulunur.

Araç, yol ve engel durumuna göre otomatik olarak hareket edecektir.

Katkıda Bulunanlar
