from collections import defaultdict, deque
import heapq
from typing import Dict, List, Tuple, Optional

class Istasyon:
    def __init__(self, idx: str, ad: str, hat: str):
        self.idx = idx
        self.ad = ad
        self.hat = hat
        self.komsular: List[Tuple['Istasyon', int]] = []  # (istasyon, süre) tuple'ları

    def komsu_ekle(self, istasyon: 'Istasyon', sure: int):
        self.komsular.append((istasyon, sure))

class MetroAgi:
    def __init__(self):
        self.istasyonlar: Dict[str, Istasyon] = {}
        self.hatlar: Dict[str, List[Istasyon]] = defaultdict(list)

    def istasyon_ekle(self, idx: str, ad: str, hat: str) -> None:
        if idx not in self.istasyonlar:  # İstasyonun varlığı kontrol edildi
            istasyon = Istasyon(idx, ad, hat)
            self.istasyonlar[idx] = istasyon
            self.hatlar[hat].append(istasyon)

    def baglanti_ekle(self, istasyon1_id: str, istasyon2_id: str, sure: int) -> None:
        if istasyon1_id in self.istasyonlar and istasyon2_id in self.istasyonlar:
            istasyon1 = self.istasyonlar[istasyon1_id]
            istasyon2 = self.istasyonlar[istasyon2_id]
            istasyon1.komsu_ekle(istasyon2, sure)
            istasyon2.komsu_ekle(istasyon1, sure)

    def en_az_aktarma_bul(self, baslangic_id: str, hedef_id: str) -> Optional[List[Istasyon]]:
        if baslangic_id not in self.istasyonlar or hedef_id not in self.istasyonlar:
            return None

        baslangic = self.istasyonlar[baslangic_id]
        hedef = self.istasyonlar[hedef_id]
        kuyruk = deque([(baslangic, [baslangic])])
        ziyaret_edildi = set()

        while kuyruk:
            mevcut, yol = kuyruk.popleft()
            if mevcut == hedef:
                return yol
            
            for komsu, _ in mevcut.komsular:
                if komsu not in ziyaret_edildi:
                    ziyaret_edildi.add(komsu)
                    kuyruk.append((komsu, yol + [komsu]))
        
        return None

    def en_hizli_rota_bul(self, baslangic_id: str, hedef_id: str) -> Optional[Tuple[List[Istasyon], int]]:
        if baslangic_id not in self.istasyonlar or hedef_id not in self.istasyonlar:
            return None

        baslangic = self.istasyonlar[baslangic_id]
        hedef = self.istasyonlar[hedef_id]
        pq = [(0, id(baslangic), baslangic, [baslangic])]
        ziyaret_edildi = {}

        while pq:
            sure, _, mevcut, yol = heapq.heappop(pq)
            if mevcut == hedef:
                return yol, sure

            if mevcut in ziyaret_edildi and ziyaret_edildi[mevcut] <= sure:
                continue

            ziyaret_edildi[mevcut] = sure
            
            for komsu, ek_sure in mevcut.komsular:
                heapq.heappush(pq, (sure + ek_sure, id(komsu), komsu, yol + [komsu]))
        
        return None


        pass
        if baslangic_id not in self.istasyonlar or hedef_id not in self.istasyonlar:
            return None

        baslangic = self.istasyonlar[baslangic_id]
        hedef = self.istasyonlar[hedef_id]
        ziyaret_edildi = set()

print("Test senaryosu tamamlandı!")

# Örnek Kullanım
if __name__ == "__main__":
    metro = MetroAgi()
    
    # İstasyonlar ekleme
    # Kırmızı Hat
    metro.istasyon_ekle("K1", "Batıkent", "Kırmızı Hat")
    metro.istasyon_ekle("K2", "Atatürk Kültür Merkezi", "Kırmızı Hat") #Aktarma noktası
    metro.istasyon_ekle("K3", "Kızılay", "Kırmızı Hat") #Aktarma noktası
    metro.istasyon_ekle("K4", "ODTÜ", "Kırmızı Hat")
    
    
    # Mavi Hat
    metro.istasyon_ekle("M1", "AŞTİ", "Mavi Hat")
    metro.istasyon_ekle("M2", "Emek", "Mavi Hat")
    metro.istasyon_ekle("M3", "Maltepe", "Mavi Hat") #Aktarma noktası
    metro.istasyon_ekle("M4", "Kızılay", "Mavi Hat")  # Aktarma noktası
    
    # Turuncu Hat
    metro.istasyon_ekle("T1", "Adliye", "Turuncu Hat") 
    metro.istasyon_ekle("T2", "Atatürk Kültür Merkezi", "Turuncu Hat")  # Aktarma noktası
    metro.istasyon_ekle("T3", "Gar", "Turuncu Hat") #Aktarma noktası
    metro.istasyon_ekle("T4", "Meteoroloji", "Turuncu Hat")
    metro.istasyon_ekle("T5", "Dutluk", "Turuncu Hat")
    
    # Bağlantılar ekleme
    # Kırmızı Hat bağlantıları
    metro.baglanti_ekle("K1", "K2", 18)  # Batıkent -> AKM
    metro.baglanti_ekle("K2", "K3", 6)   # AKM -> Kızılay
    metro.baglanti_ekle("K3", "K4", 12)  # Kızılay -> Odtü
    
    # Mavi Hat bağlantıları
    metro.baglanti_ekle("M1", "M2", 2)  # AŞTİ -> Emek
    metro.baglanti_ekle("M2", "M3", 6)  # Emek -> Maltepe
    metro.baglanti_ekle("M3", "M4", 2)  # Maltepe -> Kızılay
    
    # Turuncu Hat bağlantıları
    metro.baglanti_ekle("T1", "T2", 4)  # Adliye -> AKM
    metro.baglanti_ekle("T2", "T3", 2)  # AKM -> Gar
    metro.baglanti_ekle("T3", "T4", 7)  # Gar -> Meteoroloji
    metro.baglanti_ekle("T4", "T5", 8)  # Meteoroloji -> Dutluk
    
    # Hat aktarma bağlantıları (aynı istasyon farklı hatlar)
    metro.baglanti_ekle("K3", "M4", 2)  # Kızılay aktarma
    metro.baglanti_ekle("K2", "T2", 3)  # AKM aktarma
    metro.baglanti_ekle("M3", "T3", 4)  # Gar-Maltepe aktarma
    
    # Test senaryoları
    print("\n=== Test Senaryoları ===")
    
    # Senaryo 1: AŞTİ'den OSB'ye
    print("\n1. AŞTİ'den ODTÜ'ye:")
    rota = metro.en_az_aktarma_bul("M1", "K4")
    if rota:
        print("En az aktarmalı rota:", " -> ".join(i.ad for i in rota))
    
    sonuc = metro.en_hizli_rota_bul("M1", "K4")
    if sonuc:
        rota, sure = sonuc
        print(f"En hızlı rota ({sure} dakika):", " -> ".join(i.ad for i in rota))
    
    # Senaryo 2: Batıkent'ten Keçiören'e
    print("\n2. Emek'ten Meteorolojiye'e:")
    rota = metro.en_az_aktarma_bul("M2", "T4")
    if rota:
        print("En az aktarmalı rota:", " -> ".join(i.ad for i in rota))
    
    sonuc = metro.en_hizli_rota_bul("M2", "T4")
    if sonuc:
        rota, sure = sonuc
        print(f"En hızlı rota ({sure} dakika):", " -> ".join(i.ad for i in rota))
    
    # Senaryo 3: Keçiören'den AŞTİ'ye
    print("\n3. Batıkent'den Gar'a:")
    rota = metro.en_az_aktarma_bul("K1", "T3")
    if rota:
        print("En az aktarmalı rota:", " -> ".join(i.ad for i in rota))
    
    sonuc = metro.en_hizli_rota_bul("K1", "T3")
    if sonuc:
        rota, sure = sonuc
        print(f"En hızlı rota ({sure} dakika):", " -> ".join(i.ad for i in rota))
