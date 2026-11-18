from pathlib import Path
from ipaddress import ip_address

from pengolahan import (
    read_csv,
    save_json,
    search_by_ip,
    filter_failed,
    detect_suspicious,
    get_statistics
)

BASE_DIR = Path(__file__).resolve().parent
INPUT_FILE = BASE_DIR / "data" / "input.csv"
OUTPUT_FILE = BASE_DIR / "data" / "output.json"


def show_logs(logs):
    """Menampilkan daftar log keamanan."""
    if not logs:
        print("Tidak ada data yang ditemukan.")
        return 0

    for log in logs:
        print(
            f'{log["timestamp"]} | '
            f'{log["ip_address"]} | '
            f'{log["username"]} | '
            f'{log["event"]} | '
            f'{log["status"]}'
        )

    return len(logs)


def main():
    """Menjalankan aplikasi Security Log Analyzer."""

    logs = read_csv(INPUT_FILE)

    if not logs:
        print("Tidak ada data valid untuk dianalisis.")
        return 1

    while True:
        print("\n================================")
        print("     SECURITY LOG ANALYZER")
        print("================================")
        print("1. Tampilkan semua log")
        print("2. Cari berdasarkan IP Address")
        print("3. Tampilkan login gagal")
        print("4. Deteksi IP mencurigakan")
        print("5. Tampilkan statistik keamanan")
        print("6. Simpan hasil analisis")
        print("0. Keluar")
        print("================================")

        pilihan = input("Masukkan pilihan: ").strip()

        if pilihan == "1":
            show_logs(logs)

        elif pilihan == "2":
            ip = input("Masukkan alamat IP: ").strip()

            try:
                ip_address(ip)
                show_logs(search_by_ip(logs, ip))
            except ValueError:
                print("Error: Alamat IP tidak valid.")

        elif pilihan == "3":
            show_logs(filter_failed(logs))

        elif pilihan == "4":
            suspicious = detect_suspicious(logs)

            if not suspicious:
                print("Tidak ada IP mencurigakan.")
            else:
                for ip, count in suspicious.items():
                    print(f"{ip}: {count} login gagal")

        elif pilihan == "5":
            stats = get_statistics(logs)

            for key, value in stats.items():
                print(f"{key}: {value}")

        elif pilihan == "6":
            result = get_statistics(logs)

            if save_json(OUTPUT_FILE, result):
                print("Hasil analisis berhasil disimpan.")
                print(f"Lokasi: {OUTPUT_FILE}")

        elif pilihan == "0":
            print("Terima kasih!")
            return 0

        else:
            print("Pilihan tidak valid.")


if __name__ == "__main__":
    raise SystemExit(main())