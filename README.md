Bobobox Assessment

Repository ini berisi kumpulan challenge teknikal yang mencakup data analysis, database design, python coding, dan SQL query.
Tujuan dari assessment ini adalah untuk menguji kemampuan analisis data, transformasi, serta desain dan implementasi query database.

=======================================================================================================================================

'''
Struktur Direktori

bobobox-assessment/
│
├── Data Analysis Challenge/
│   ├── Anomali Detection/
│   │   ├── Explanation.txt
│   │   ├── Output.txt
│   │   └── transaction_anomaly.py
│   │
│   └── Data Insight/
│       ├── Explanation.txt
│       ├── Output.txt
│       ├── transaction_summary.py
│       └── transactions.csv
│
├── Database Design/
│   └── Relational Database Design for ...
│       ├── create_tables.sql
│       └── .gitkeep
│
├── Python Code Challenge/
│   └── Data Transformation/
│       ├── Explanation.txt
│       ├── Result.txt
│       └── data_transformation.py
│
└── SQL Query Challenge/
    ├── Aggregation Query/
    │   ├── Explanation.txt
    │   ├── Contoh Output.txt
    │   └── aggregation.sql
    │
    └── Multi-Table Join Query/
        ├── Explanation.txt
        ├── Contoh Output.txt
        └── multi-table-join-query.sql
'''

==============================================================================================================================================================

1. Data Analysis Challenge
   
a. Anomaly Detection

Folder: Anomali Detection
Deskripsi:
Menjalankan analisis untuk mendeteksi transaksi yang menyimpang dari pola umum (anomali), misalnya transaksi dengan jumlah tidak wajar atau frekuensi tinggi.
File Utama:
- transaction_anomaly.py – Script utama untuk mendeteksi anomali.
- Explanation.txt – Penjelasan metode deteksi yang digunakan.
- Output.txt – Hasil deteksi transaksi anomali.

b. Data Insight

Folder: Data Insight
Deskripsi:
Analisis deskriptif dan eksploratif terhadap dataset transaksi untuk menemukan pola, tren, dan insight bisnis yang relevan.
File Utama:
- transactions.csv – Dataset sumber.
- transaction_summary.py – Script analisis data.
- Explanation.txt – Penjelasan logika analisis.
- Output.txt – Hasil insight yang dihasilkan.

2. Database Design

Folder: Database Design/Relational Database Design for ...
Deskripsi:
Perancangan model database relasional yang terstruktur untuk menyimpan data transaksi, pengguna, dan entitas terkait.
File Utama:
- create_tables.sql – Script SQL untuk membuat tabel dan relasi antar entitas.

3. Python Code Challenge – Data Transformation

Folder: Python Code Challenge/Data Transformation
Deskripsi:
Transformasi data mentah menjadi format yang siap digunakan untuk analisis, termasuk pembersihan, penggabungan, dan perhitungan metrik.
File Utama:
- data_transformation.py – Script utama transformasi data.
- Explanation.txt – Penjelasan proses transformasi.
- Result.txt – Hasil akhir transformasi.

4. SQL Query Challenge

Folder: SQL Query Challenge
Deskripsi:
Berisi tantangan SQL yang berfokus pada manipulasi dan analisis data dalam basis data relasional.

a. Aggregation Query
Melakukan agregasi data untuk menghasilkan ringkasan statistik seperti total, rata-rata, atau jumlah transaksi per kategori.
File:
- aggregation.sql – Query utama agregasi.
- Explanation.txt – Penjelasan logika query.
- Contoh Output.txt – Contoh hasil eksekusi query.

b. Multi-Table Join Query
Melakukan penggabungan beberapa tabel untuk menghasilkan laporan terintegrasi yang mencakup berbagai entitas.
File:
- multi-table-join-query.sql – Query utama join.
- Explanation.txt – Penjelasan logika join.
- Contoh Output.txt – Contoh hasil eksekusi query.

=======================================================================================================================================

Cara Menjalankan

Menjalankan Script Python
1. Pastikan Python 3.10+ telah terpasang.
2. Jalankan script sesuai folder:
    cd "Data Analysis Challenge/Anomali Detection"
    python transaction_anomaly.py

Menjalankan SQL Script
Gunakan PostgreSQL, MySQL, atau SQLite.
Eksekusi melalui command line atau DBMS GUI:
    psql -U <user> -d <database> -f create_tables.sql

=======================================================================================================================================

Tools dan Library

Python:
- pandas
- numpy
- matplotlib (opsional)
- seaborn (opsional)

Database:
- PostgreSQL
- SQLite (untuk pengujian lokal)

========================================================================================================================================

Author
Nama: Alfi Safrian
Tujuan: Latihan dan pengembangan keterampilan analisis data, SQL, serta desain database.
