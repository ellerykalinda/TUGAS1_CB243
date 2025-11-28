# Tugas 1 – Pengembangan Sistem Backend (CB243)

Repositori ini berisi implementasi dua studi kasus OOP sesuai instruksi tugas:
- Studi Kasus 1: Person–Student–Professor–Address**
- Studi Kasus 2: LibraryItem–Book–Author–LibraryMember**

Seluruh kode ditulis menggunakan bahasa pemrograman **Python**, tanpa framework (FastAPI / Django), sesuai instruksi tugas.

---

## 📁 Struktur Direktori

TUGAS1-CB243/
│
├── studi_kasus_1/
│ ├── campus_classes.py
│ ├── main.py
│
└── studi_kasus_2/
├── library_classes.py
├── main.py


- Setiap studi kasus berada dalam folder berbeda.
- Masing-masing memiliki **satu entry point**, yaitu `main.py`.

---

## 🎯 Tujuan Tugas

1. Menerapkan konsep dasar OOP (class, inheritance, encapsulation, polymorphism).
2. Mengimplementasikan class diagram menjadi program Python.
3. Menggunakan relasi antar objek sesuai diagram (association, inheritance).
4. Menyusun struktur program yang modular, bersih, dan mudah dibaca.

---

# 🧩 **Studi Kasus 1 — Person, Student, Professor, Address**

## ✔ Class yang Diimplementasikan

### 1. **Address**
- Atribut: street, city, state, postalCode, country
- Method:
  - private `__validate()`
  - `output_as_label()`
  - `is_valid()`

### 2. **Person**
- Superclass dari Student & Professor
- Atribut: name, phoneNumber, emailAddress, address
- Method:
  - `purchase_parking_pass()`

### 3. **Student**
- Atribut: studentNumber, averageMark
- Method:
  - `is_eligible_to_enroll()`
  - `get_seminars_taken()`
- Relasi supervises dengan Professor

### 4. **Professor**
- Atribut: staffNumber, yearsOfService (private), numberOfClasses
- Property:
  - `salary` (derived attribute)
- Method:
  - `add_supervised_student()` (max 5 mahasiswa)

---

## ▶ Cara Menjalankan Studi Kasus 1
Buka terminal Folder TUGAS1_CB243
Masuk ke folder:
cd studi_kasus_1
python main.py

## ▶ Output studi_kasus_1
====== Demo Studi Kasus 1 ======

[1. Inisialisasi Address]
Alamat: Jln. Raya Puputan No.86, Denpasar Timur, Kota Denpasar 80234, Indonesia
Alamat Valid? True

[2. Inisialisasi Professor]
Professor: Dr. Rudy (Staff No: 1001), Classes: 3, Years of Service: 10, Current Salary: Rp 20,000,000
Dr. Rudy telah berhasil membeli kartu parkir kampus.

[3. Inisialisasi Student]
Student: Ellery (NIM: 240030341), Avg Mark: 85. Supervisors: 0

[4. Demonstrasi Student Methods]
Student Ellery Eligible to enroll in CB243.
Student Raditya Not eligible to enroll in CA233 (Mark: 65).
Ellery telah mengambil 5 seminar.

[5. Demonstrasi Relasi Supervises]
Professor: Dr. Rudy (Staff No: 1001), Classes: 3, Years of Service: 10, Current Salary: Rp 20,000,000
Student: Ellery (NIM: 240030341), Avg Mark: 85. Supervisors: 1
Student: Raditya (NIM: 240030054), Avg Mark: 65. Supervisors: 1




---

# 📚 **Studi Kasus 2 — LibraryItem, Book, Author, LibraryMember**

## ✔ Class yang Diimplementasikan

### 1. **Author**
- Atribut: name, birthYear
- Method: `get_age()`

### 2. **LibraryItem** (Superclass – Abstract Behavior)
- Atribut: itemId, title
- Method:
  - `display_info()`
  - `calculate_late_fee()`

### 3. **Book** (Subclass)
- Atribut: private `isbn`
- Override:
  - `display_info()`
  - `calculate_late_fee()`

### 4. **LibraryMember**
- Mewarisi Author
- Atribut: memberId, borrowedItems
- Method:
  - `borrow_item()`
  - `return_item()`
  - `list_borrowed_items()`

---

## ▶ Cara Menjalankan Studi Kasus 2
Buka terminal Folder TUGAS1_CB243
Masuk ke folder:
cd studi_kasus_2
python main.py

## ▶ Output studi_kasus_2
====== Demo Studi Kasus 2 ======

[1. Inisialisasi Author]
J.R.R. Tolkien lahir tahun 1892, umurnya sekarang: 133 tahun.

[2. Inisialisasi Book]
--- Library Item Info ---
ID: 101, Title: The Hobbit
Type: Book, ISBN: 978-0547928227
Author: J.R.R. Tolkien

[3. Inisialisasi Library Member]
Author(Name: Aragorn Elessar, Born: 1995)

[4. Peminjaman Item]
'Aragorn Elessar' berhasil meminjam item: 'The Hobbit'

--- Item yang Dipinjam oleh Aragorn Elessar (ID: 2001) ---
- [ID: 101] The Hobbit

[5. Menghitung Denda]
Jika buku 'The Hobbit' terlambat 7 hari, denda: Rp 7,000

[6. Pengembalian Item]
'Aragorn Elessar' berhasil mengembalikan item: 'The Hobbit'

--- Item yang Dipinjam oleh Aragorn Elessar (ID: 2001) ---
Tidak ada item yang sedang dipinjam.


---

# Penggunaan AI dalam Pengerjaan 

Saya menggunakan bantuan ChatGPT hanya untuk memperbaiki penjelasan, mengecek kesesuaian class diagram, dan merapikan README.md.
Seluruh implementasi kode, logika, dan struktur program dikembangkan secara mandiri.


## Dokumentasi Prompt–Response AI

Bagian ini dibuat untuk memenuhi standar integritas akademik sesuai rubrik tugas.  
Seluruh kode, struktur program, dan logika bisnis disusun secara mandiri.  
AI digunakan sebagai asisten pengecekan konsep, klarifikasi instruksi, dan penyusunan dokumentasi.

Dokumentasi berikut berisi rangkuman **prompt dan response** yang digunakan selama proses pengerjaan.

### Prompt 1
"Periksa apakah kode Studi Kasus sudah sesuai dengan class diagram dan instruksi PDF."

**Ringkasan Response:**  
ChatGPT membantu memvalidasi struktur class, relasi supervisi, inheritance, serta memberikan saran perbaikan kecil.

### Prompt 2
"Bantu susun README.md yang sesuai rubrik tugas."

**Ringkasan Response:**  
ChatGPT memberikan contoh pembuatan README, perbaikan struktur direktori, dan penjelasan yang lebih rapi.

### Prompt 3
"Bantu jelaskan apakah maksud instruksi 'program dijalankan melalui satu entry point' berarti kedua studi kasus harus memakai satu main.py atau masing-masing."

**Ringkasan Response:**  
ChatGPT menjelaskan bahwa setiap studi kasus harus berada di folder terpisah dan masing-masing memiliki satu `main.py` sebagai entry point, bukan digabungkan menjadi satu file.

### Prompt 4
"Tolong cek apakah class Person, Student, Professor, dan Address yang saya buat sudah sesuai dengan class diagram."

**Ringkasan Response:**  
ChatGPT membantu memverifikasi atribut (`name`, `phoneNumber`, `emailAddress`, relasi Address), method (`purchase_parking_pass()`), inheritance Student–Person, dan batasan supervisi pada Professor (maksimal 5 mahasiswa).  
Diberikan masukan kecil seperti penggunaan private attribute (`__years_of_service`) dan pemisahan file agar lebih modular.

### Prompt 5 
"Maksud ‘screenshot output program’ itu bagaimana? Apakah perlu gambar atau bisa dalam bentuk teks?"

**Ringkasan Response:**  
ChatGPT menjelaskan bahwa output **boleh ditulis dalam bentuk teks** langsung di README, tidak wajib screenshot gambar. Teks yang rapi sudah cukup dan lebih direkomendasikan untuk GitHub.

## Pernyataan Akhir Penggunaan AI
AI digunakan **secara terbatas** untuk:
- Klarifikasi instruksi dari soal  
- Pengecekan konsistensi class vs class diagram  
- Saran struktur folder  
- Penyusunan dan perapian README.md  
- Dokumentasi integritas penggunaan AI  

**Seluruh implementasi kode program dan logika ditulis sendiri.**