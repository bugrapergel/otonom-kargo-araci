🚚 Otonom Kargo Aracı
Bu proje, düşük maliyetli donanım ve gelişmiş makine öğrenmesi algoritmalarını bir araya getirerek, belirli bir ortamda (kendi sokaklarında) otonom olarak hareket edebilen bir kargo aracı geliştirmeyi hedefler. Sistem, bir kamera aracılığıyla şerit ve engel tespiti yaparak güvenli ve akıllı bir şekilde yol alabilir.

✨ Temel Özellikler
Otonom Sürüş: Gelişmiş bir CNN modeli (UFLD veya benzeri) kullanarak şeritleri ve yol çizgilerini gerçek zamanlı olarak takip etme.

Dinamik Engel Algılama: Önündeki engelleri algılayıp, çarpmayı önlemek için otomatik olarak yön değiştirme.

Verimli Motor Kontrolü: Arduino Nano, L298M motor sürücüler ve 3 motor (2 arka, 1 ön) ile aracın hareketini hassas bir şekilde yönetme.

Modüler Yazılım Mimarisi: Python ve PyCharm üzerinde geliştirilen kodun, donanım kontrolü ile ayrıştırılmış, düzenli bir yapıya sahip olması.

GIF Önerisi: Projenin küçük, döngüsel bir videosunu (örneğin, aracın bir şeridi takip etmesi veya bir engelden kaçması) çekerek buraya ekleyebilirsiniz. Bu, projenizin ne işe yaradığını anında gösterir.

⚙️ Sistem Mimarisi
Sistem, görevleri farklı katmanlara ayırarak daha anlaşılır ve yönetilebilir bir yapı sunar.

Görüntü İşleme Katmanı: Kamera ile alınan video akışı, şerit ve engel tespiti için Python tabanlı makine öğrenmesi modellerine gönderilir.

Karar Katmanı: İşlenen veriler doğrultusunda, aracın ne yöne gitmesi gerektiği veya durması gerekip gerekmediği gibi kararlar alınır.

Donanım Kontrol Katmanı: Alınan kararlar, Arduino Nano'ya seri port üzerinden komut olarak gönderilir.

Fiziksel Hareket Katmanı: Arduino, gelen komutlara göre motor sürücülerini ve motorları kontrol ederek aracı hareket ettirir.

Kod snippet'i

graph TD
    A[Kamera Görüntüsü] --> B(Python İşleme ve ML Modeli);
    B --> C{Karar Mantığı};
    C --> D[Arduino Nano];
    D --> E[Motor Sürücüleri & Motorlar];
🛠️ Kurulum
1. Donanım Bağlantısı
Arduino Nano, 3 motor ve L298M motor sürücüleri arasındaki bağlantıları şemaya uygun şekilde yapın.

2. Yazılım Kurulumu
Python 3.x'in bilgisayarınızda yüklü olduğundan emin olun.

Proje deposunu klonlayın:

Bash

git clone https://github.com/KULLANICIADINIZ/PROJEADINIZ.git
cd PROJEADINIZ
Gerekli tüm Python kütüphanelerini tek bir komutla yükleyin:

Bash

pip install -r requirements.txt
3. Model Ağırlıkları
Makine öğrenmesi modeli için gerekli ağırlıkları models/ klasörüne indirin.

▶️ Kullanım
Projenin ana betiğini çalıştırmak için şu komutu kullanın:

Bash

python main.py
Bu komut, kamerayı başlatacak ve aracı otonom olarak hareket ettirecektir.

🤝 Katkıda Bulunma
Bu projeye katkılarınızı memnuniyetle bekliyoruz! Hata düzeltmeleri, yeni özellikler veya performans iyileştirmeleri için lütfen bir pull request gönderin veya bir issue açın.
