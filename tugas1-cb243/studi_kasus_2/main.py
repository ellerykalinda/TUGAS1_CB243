# main.py
import datetime
from library_classes import Author, Book, LibraryMember

def main():
    """
    Fungsi utama untuk mendemonstrasikan implementasi Studi Kasus 2.
    """

    print("====== Demo Studi Kasus 2 ======")

    # 1. Membuat objek Author
    print("\n[1. Inisialisasi Author]")
    penulis_a = Author("Andrea Hirata", 1967)
    tahun_sekarang = datetime.date.today().year
    print(f"{penulis_a.name} lahir tahun {penulis_a.birth_year}, umurnya sekarang: {penulis_a.get_age(tahun_sekarang)} tahun.")
    
    # 2. Membuat objek Book
    print("\n[2. Inisialisasi Book]")
    buku_1 = Book(
        item_id=101, 
        title="Laskar Pelangi", 
        isbn="978-0547928227", 
        author=penulis_a
    )
    buku_1.display_info()
    
    # 3. Membuat objek LibraryMember
    # Perhatikan LibraryMember mewarisi dari Author
    print("\n[3. Inisialisasi Library Member]")
    anggota_1 = LibraryMember(
        name="Budi Santosa", 
        birth_year=1998, 
        member_id=2001
    )
    print(anggota_1) # Menggunakan __str__ dari Author
    
    # 4. Melakukan peminjaman
    print("\n[4. Peminjaman Item]")
    anggota_1.borrow_item(buku_1) # +borrow_item [cite: 69]
    anggota_1.list_borrowed_items()
    
    # 5. Menghitung denda
    print("\n[5. Menghitung Denda]")
    hari_terlambat = 7
    denda = buku_1.calculate_late_fee(hari_terlambat) # Polymorphism, method Book dipanggil [cite: 54]
    print(f"Jika buku '{buku_1.title}' terlambat {hari_terlambat} hari, denda: Rp {denda:,.0f}")
    
    # 6. Melakukan pengembalian
    print("\n[6. Pengembalian Item]")
    anggota_1.return_item(buku_1) # +return_item
    anggota_1.list_borrowed_items()
    
if __name__ == "__main__":

    main()

