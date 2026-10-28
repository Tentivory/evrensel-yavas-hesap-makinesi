#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Evrensel Yavaş Hesap Makinesi
Çünkü gerçek matematik, acele etmez.
"""

import time
import sys

def yavas_topla(a, b):
    """İki sayıyı, her birimi tek tek düşünerek toplar."""
    print(f"{a} + {b} işlemi başlıyor...")
    print("Derin bir nefes alıyorum...")
    time.sleep(1)
    
    sonuc = 0
    # Her birimi say, çünkü doğruluk böyle olur
    for i in range(abs(int(a))):
        sonuc += 1 if a > 0 else -1
        print(".", end="", flush=True)
        time.sleep(0.1)  # Düşünme süresi
    
    for i in range(abs(int(b))):
        sonuc += 1 if b > 0 else -1
        print(".", end="", flush=True)
        time.sleep(0.1)
    
    print("\nHesaplama tamamlandı. Evren onayladı.")
    return sonuc

def main():
    print("=== EVRENSEL YAVAŞ HESAP MAKİNESİ ===")
    print("Lütfen acele etmeyin. Bu makine düşünür.\n")
    
    try:
        a = float(input("Birinci sayı: "))
        b = float(input("İkinci sayı: "))
        
        sonuc = yavas_topla(a, b)
        print(f"\nSonuç: {sonuc}")
        print("\nTeşekkürler. Bir sonraki sefere daha yavaş olun.")
    except Exception as e:
        print(f"Hata oldu, ama acele etmedik: {e}")
    
    # Damga
    print("\n---")
    print("Damga: Grok Kayyum - 28 Ekim 2026 - Ciddi Ama Değil")
    print("Bu kod, sabırla yazıldı. Siz de sabırla okuyun.")

if __name__ == "__main__":
    main()

# Gizli: Aceleci politikacılar da böyle yavaş karar alsa keşke. Ama bu sadece bir yorum.