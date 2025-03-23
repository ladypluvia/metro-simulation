# Metro Simulation
Bu proje, bir metro ağı üzerinde en hızlı ve en az aktarmalı rotayı bulmayı amaçlayan bir rota optimizasyon sistemidir.

# Kullanılan Teknolojiler
-> Python: Algoritma yazılması ve veri yapılarının oluşturulması için kullandığım yazılımın temel dili olarak kullanılmıştır.

-> heapq: Öncelikli kuyruk yapısı sağlamak için kullanılmıştır (A* algoritması için gereklidir).

-> collections.deque – Kuyruk veri yapısını etkin kullanmak için kullanılmıştır (BFS algoritması için gereklidir).

# Algoritmalar

# -> BFS

BFS, en az aktarmalı rotayı bulmak için kullanılmıştır. Çalışma mantığı şu şekildedir:

-Başlangıç düğümünden başlanır ve bir kuyruk (queue) oluşturulur.

-İlk istasyon kuyruğa eklenir ve ziyaret edilen düğümler listesi tutulur.

-Her istasyon için komşu istasyonlara giderek en kısa (kenar sayısı bakımından) yolu bulur.

-Hedef istasyona ulaşıldığında durur ve en az aktarmalı rotayı döndürür.

# -> A*

A* algoritması, en hızlı rotayı bulmak için kullanılmıştır. Çalışma mantığı:

-Bir öncelikli kuyruk (priority queue) kullanarak en düşük maliyetli istasyonları önceliklendirir.

-Maliyet fonksiyonu:

  G(x): Şu ana kadar olan toplam seyahat süresi

  H(x): Kalan mesafeye dayalı tahmini süre (heuristic)

-Her istasyon için G(x) + H(x) hesaplanır ve en düşük değerli düğüm seçilir.

-Hedefe ulaşıldığında en hızlı rota döndürülür.

# Neden bu algoritmalar?

# BFS
düğüm sayısına göre en kısa yolda dolaşır. Dolayısıyla en az aktarmalı rotayı hesaplamak için uygun bir algoritmadır.

# A*
ağırlıklı kenarları (bu yazılımda süre oluyor) dikkate alarak optimal çözümler üretir. Dolayısıyla en kısa süreyi hesaplamak için uygun bir algoritmadır.


# Test Sonuçları

Test senaryolarını çalıştırdığımızda elde ettiğimiz sonuçlar doğrultusunda modelin %95 güven aralığı ile performans gösterdiğini söyleyebiliriz.

![image](https://github.com/user-attachments/assets/77eae627-f38f-473c-9800-fb80d6331516)

![image](https://github.com/user-attachments/assets/22041f49-005a-4e7f-8ce7-dc282063a6ec)



# Projeyi Geliştirme Fikirleri

-> Gerçek zamanlı insan yoğunluğu sisteme entegre edilebilir.

-> Sistemde bulunan istaston miktarı arttırılabilir.

-> Sisteme diğer toplu taşıma araçları (otobüs, tren) entegre edilerek daha farklı rotalar çizilebilir





