import json
import os

# Warna biar cakep
MERAH = "\033[91m"
HIJAU = "\033[92m"
KUNING = "\033[93m"
BIRU = "\033[94m"
UNGU = "\033[95m"
CYAN = "\033[96m"
RESET = "\033[0m"

FILE_NAME = "tugas.json"

def load_data():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    return {}

def save_data(data):
    with open(FILE_NAME, "w") as f:
        json.dump(data, f, indent=4)

def tampilkan_menu():
    print(f"""
{BIRU}╔════════════════════════════════╗
║ {CYAN}📚 Penyimpan Tugas Sayangku 📚{BIRU} ║
╚════════════════════════════════╝{RESET}
    """)
    print(f"{HIJAU}1.{RESET} Save tugas")
    print(f"{HIJAU}2.{RESET} Lihat tugas")
    print(f"{HIJAU}3.{RESET} Tandai tugas selesai")
    print(f"{HIJAU}4.{RESET} Keluar\n")

data_tugas = load_data()

while True:
    tampilkan_menu()
    pilihan = input(f"{KUNING}Pilih menu (1/2/3/4): {RESET}").strip()

    if pilihan == "1":
        nama_tugas = input(f"{CYAN}Masukkan nama tugas: {RESET}").strip()
        isi_tugas = input(f"{CYAN}Masukkan detail tugas: {RESET}").strip()
        data_tugas[nama_tugas] = isi_tugas
        save_data(data_tugas)
        print(f"{HIJAU}✅ Tugas '{nama_tugas}' berhasil disimpan!{RESET}\n")

    elif pilihan == "2":
        if not data_tugas:
            print(f"{MERAH}⚠ Belum ada tugas yang disimpan, sayang.{RESET}\n")
        else:
            print(f"\n{UNGU}📜 Daftar Tugas:{RESET}")
            for i, tugas in enumerate(data_tugas, start=1):
                print(f"{HIJAU}{i}.{RESET} {tugas}")
            cari = input(f"\n{KUNING}Masukkan nama tugas untuk melihat detail: {RESET}").strip()
            if cari in data_tugas:
                print(f"{BIRU}📌 Detail tugas '{cari}':{RESET} {data_tugas[cari]}\n")
            else:
                print(f"{MERAH}❌ Tugas '{cari}' tidak ditemukan.{RESET}\n")

    elif pilihan == "3":
        if not data_tugas:
            print(f"{MERAH}⚠ Belum ada tugas yang bisa ditandai selesai.{RESET}\n")
        else:
            print(f"\n{UNGU}✅ Tugas yang ada sekarang:{RESET}")
            for i, tugas in enumerate(data_tugas, start=1):
                print(f"{HIJAU}{i}.{RESET} {tugas}")
            selesai = input(f"\n{KUNING}Masukkan nama tugas yang sudah selesai: {RESET}").strip()
            if selesai in data_tugas:
                del data_tugas[selesai]
                save_data(data_tugas)
                print(f"{HIJAU}🎉 Tugas '{selesai}' sudah selesai dan dihapus. Bangga banget sama kamu, sayang! 💖{RESET}\n")
            else:
                print(f"{MERAH}❌ Tugas '{selesai}' tidak ditemukan.{RESET}\n")

    elif pilihan == "4":
        print(f"{CYAN}Bye bye sayangku, semangat terus kerjain tugasnya! 💕{RESET}")
        break

    else:
        print(f"{MERAH}⚠ Pilihan nggak dikenali, coba lagi ya sayang.{RESET}\n")
