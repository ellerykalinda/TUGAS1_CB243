import datetime

## Class Author
class Author:
    """
    Merepresentasikan seorang penulis atau pencipta item perpustakaan.

    Atribut:
        name (str): Nama penulis. (Public '+') [cite: 62]
        birth_year (int): Tahun lahir penulis. (Public '+') [cite: 63]
    """
    def __init__(self, name: str, birth_year: int):
        self.name = name  # +name: str [cite: 62]
        self.birth_year = birth_year  # +birth_year: int [cite: 63]

    def get_age(self, current_year: int) -> int:
        """
        Menghitung umur penulis berdasarkan tahun saat ini.

        Args:
            current_year (int): Tahun saat ini.

        Returns:
            int: Umur penulis. (+get_age(current_year: int) -> int) [cite: 64]
        """
        return current_year - self.birth_year
    
    def __str__(self):
        return f"Author(Name: {self.name}, Born: {self.birth_year})"


## Class LibraryItem (Superclass/Kelas Induk)
class LibraryItem:
    """
    Merepresentasikan item umum dalam perpustakaan (abstrak/parent class).

    Atribut:
        item_id (int): ID unik item. (Public '+') [cite: 56]
        title (str): Judul item. (Public '+') [cite: 57]
    """
    def __init__(self, item_id: int, title: str):
        self.item_id = item_id  # +item_id: int [cite: 56]
        self.title = title  # +title: str [cite: 57]

    def display_info(self) -> None:
        """
        Menampilkan informasi dasar tentang item perpustakaan.
        Ini adalah implementasi dasar yang harus di-override oleh subclass.
        (+display_info() -> None) [cite: 58]
        """
        print(f"--- Library Item Info ---")
        print(f"ID: {self.item_id}, Title: {self.title}")

    def calculate_late_fee(self, days_late: int) -> float:
        """
        Menghitung denda keterlambatan (late fee) umum.
        Asumsi: denda dasar 500 IDR per hari.
        (+calculate_late_fee(days_late: int) -> float) [cite: 60]

        Args:
            days_late (int): Jumlah hari keterlambatan.

        Returns:
            float: Total denda.
        """
        base_fee_per_day = 500
        return float(days_late * base_fee_per_day)

    def __str__(self):
        return f"LibraryItem(ID: {self.item_id}, Title: {self.title})"


## Class Book (Subclass dari LibraryItem)
class Book(LibraryItem):
    """
    Merepresentasikan item Buku, yang merupakan jenis dari LibraryItem.
    
    Atribut:
        _isbn (str): Nomor ISBN buku. (Private '-') [cite: 48]
        title (str): Judul buku. (Public '+', diwarisi dari LibraryItem, tapi disebutkan lagi di diagram) [cite: 49]
        author (Author): Objek penulis buku. (Public '+') [cite: 51]
    """
    def __init__(self, item_id: int, title: str, isbn: str, author: Author):
        # Memanggil constructor kelas induk (LibraryItem)
        super().__init__(item_id, title)

        # Atribut spesifik Book
        self.__isbn = isbn  # -isbn: str (menggunakan double underscore untuk konvensi private) [cite: 48]
        self.author = author  # +author: Author [cite: 51]

    # Getter untuk ISBN (karena private)
    def get_isbn(self) -> str:
        """Mengembalikan nilai ISBN (atribut private)."""
        return self.__isbn

    def display_info(self) -> None:
        """
        Meng-override method display_info untuk menampilkan detail buku.
        (+display_info() -> None) [cite: 52]
        """
        super().display_info()
        print(f"Type: Book, ISBN: {self.get_isbn()}")
        print(f"Author: {self.author.name}")

    def calculate_late_fee(self, days_late: int) -> float:
        """
        Menghitung denda keterlambatan spesifik untuk buku.
        Asumsi: denda buku 1000 IDR per hari.
        (+calculate_late_fee(days_late: int) -> float) [cite: 54]

        Args:
            days_late (int): Jumlah hari keterlambatan.

        Returns:
            float: Total denda.
        """
        book_fee_per_day = 1000
        return float(days_late * book_fee_per_day)


## Class LibraryMember (Subclass dari Author)
class LibraryMember(Author):
    """
    Merepresentasikan anggota perpustakaan. Mewarisi dari Author.
    
    Atribut:
        member_id (int): ID anggota. (Public '+') [cite: 66]
        borrowed_items (list): Daftar item yang dipinjam (objek LibraryItem). (Public '+') [cite: 68]
    """
    def __init__(self, name: str, birth_year: int, member_id: int):
        # Memanggil constructor kelas induk (Author)
        super().__init__(name, birth_year)

        # Atribut spesifik LibraryMember
        self.member_id = member_id  # +member_id: int [cite: 66]
        self.borrowed_items = []  # +borrowed_items: LibraryItem[] [cite: 68]

    def borrow_item(self, item: LibraryItem) -> None:
        """
        Menambahkan item ke daftar pinjaman anggota.
        (+borrow_item(item: LibraryItem) -> None) [cite: 69]

        Args:
            item (LibraryItem): Objek item yang dipinjam.
        """
        self.borrowed_items.append(item)
        print(f"'{self.name}' berhasil meminjam item: '{item.title}'")

    def return_item(self, item: LibraryItem) -> None:
        """
        Menghapus item dari daftar pinjaman anggota.
        (+return_item(item: LibraryItem) -> None)

        Args:
            item (LibraryItem): Objek item yang dikembalikan.
        """
        if item in self.borrowed_items:
            self.borrowed_items.remove(item)
            print(f"'{self.name}' berhasil mengembalikan item: '{item.title}'")
        else:
            print(f"Error: Item '{item.title}' tidak ditemukan dalam pinjaman '{self.name}'.")

    def list_borrowed_items(self) -> None:
        """Menampilkan daftar item yang sedang dipinjam."""
        print(f"\n--- Item yang Dipinjam oleh {self.name} (ID: {self.member_id}) ---")
        if not self.borrowed_items:
            print("Tidak ada item yang sedang dipinjam.")
            return

        for item in self.borrowed_items:
            print(f"- [ID: {item.item_id}] {item.title}")