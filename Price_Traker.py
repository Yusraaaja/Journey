import time
import json

# Simulasi database harga dari hasil riset manual kamu
# Ini bagus untuk portofolio: menunjukkan kamu bisa handle data JSON
market_data = [
    {"toko": "Tokopedia", "produk": "ThinkPad T480 i5 Gen 8", "harga": "Rp 3.200.000"},
    {"toko": "eBay", "produk": "ThinkPad T480 (Used)", "harga": "$210 (Rp 3.300.000)"},
    {"toko": "Lokal Lab", "produk": "ThinkPad T480 RAM 16GB", "harga": "Rp 3.550.000"}
]

def buat_laporan_investasi():
    nama_file = "laporan_t480.txt"
    print(f"[{time.strftime('%H:%M:%S')}] Mengolah data untuk target laptop...")
    
    with open(nama_file, "w") as f:
        f.write(f"=== LAPORAN HARGA T480 - {time.strftime('%d %B 2026')} ===\n")
        f.write(f"Target: Persiapan Maret 2026\n\n")
        
        for item in market_data:
            line = f"- {item['toko']}: {item['produk']} -> {item['harga']}\n"
            f.write(line)
            print(f"Berhasil mencatat data dari {item['toko']}")
            time.sleep(1) # Simulasi proses

    print(f"\n[SUKSES] File '{nama_file}' telah dibuat di folder Pydroid kamu!")
    print("Cek file tersebut di folder yang sama dengan skrip ini.")

if __name__ == "__main__":
    buat_laporan_investasi()
