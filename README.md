# Security Log Analyzer

## Deskripsi Proyek
Security Log Analyzer adalah aplikasi berbasis Python
untuk membaca, memvalidasi, dan menganalisis data log
keamanan dari file CSV.

Program ini dibuat untuk memenuhi tugas Ujian Tengah
Semester (UTS) mata kuliah Pemrograman Dasar.

## Fitur Program
1. Menampilkan seluruh data log keamanan.
2. Mencari log berdasarkan alamat IP.
3. Menampilkan aktivitas login gagal.
4. Mendeteksi alamat IP mencurigakan.
5. Menampilkan statistik keamanan.
6. Menyimpan hasil analisis dalam format JSON.
7. Menangani kesalahan input dan file.

## Struktur Proyek

    UTS_Security_Log_Analyzer/
    ├── data/
    │   ├── input.csv
    │   └── output.json
    ├── pengolahan/
    │   ├── __init__.py
    │   ├── file_handler.py
    │   ├── processor.py
    │   └── validator.py
    ├── main.py
    └── README.md

## Teknologi yang Digunakan
- Python 3.14
- Visual Studio Code
- CSV
- JSON
- Modul datetime
- Modul ipaddress
- Modul pathlib

## Cara Menjalankan Program
1. Buka folder proyek menggunakan Visual Studio Code.
2. Pastikan Python sudah terinstal.
3. Buka terminal.
4. Jalankan perintah berikut:

       python main.py

5. Pilih menu sesuai kebutuhan.

## Hasil Analisis
- Total log: 10
- Alamat IP unik: 5
- Pengguna unik: 5
- Login berhasil: 3
- Login gagal: 5
- IP mencurigakan: 192.168.1.20
- Jumlah login gagal pada IP mencurigakan: 4

IP dikategorikan mencurigakan apabila memiliki
minimal 3 percobaan login gagal.

## Pengujian Program
Program telah diuji untuk seluruh menu, validasi
alamat IP, pilihan menu tidak valid, file tidak
ditemukan, data tidak valid, dan data kosong.

Seluruh 14 skenario pengujian berhasil dilakukan.

## Kesimpulan
Program mampu membaca dan mengolah data log keamanan,
mendeteksi aktivitas mencurigakan, serta menyimpan
hasil analisis dalam format JSON.