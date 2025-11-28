## Class Address
class Address:
    """
    Merepresentasikan alamat tempat tinggal.

    Atribut:
        street (str): Nama jalan. (+street: str)
        city (str): Kota. (+city: str)
        state (str): Negara bagian/Provinsi. (+state: str)
        postal_code (int): Kode pos. (+postalCode: int)
        country (str): Negara. (+country: str)
        _is_valid (bool): Status validasi alamat (digunakan untuk atribut private).
    """
    def __init__(self, street: str, city: str, state: str, postal_code: int, country: str):
        self.street = street
        self.city = city
        self.state = state
        self.postal_code = postal_code
        self.country = country
        self.__is_valid = self.__validate() # -validate() dipanggil di init

    def __validate(self) -> bool:
        """
        Method private untuk memvalidasi alamat.
        Asumsi: Alamat dianggap valid jika semua field string tidak kosong.
        (-validate(): bool)
        """
        # Dalam implementasi nyata, ini akan lebih kompleks (misalnya, cek format postal code)
        if all([self.street, self.city, self.state, self.country]) and self.postal_code > 0:
            return True
        return False

    def output_as_label(self) -> str:
        """
        Mengembalikan alamat dalam format label pengiriman yang rapi.
        (+outputAsLabel(): str)
        """
        return (f"{self.street}, {self.city}, {self.state} "
                f"{self.postal_code}, {self.country}")

    def is_valid(self) -> bool:
        """Getter untuk atribut private __is_valid."""
        return self.__is_valid

    def __str__(self):
        return self.output_as_label()


## Class Person (Superclass/Kelas Induk)
class Person:
    """
    Merepresentasikan orang secara umum (kelas induk untuk Student dan Professor).

    Atribut:
        name (str): Nama orang. (+name: str)
        phone_number (str): Nomor telepon. (+phoneNumber: str)
        email_address (str): Alamat email. (+emailAddress: str)
        address (Address | None): Objek alamat (Relasi 0..1 lives at 1).
    """
    def __init__(self, name: str, phone_number: str, email_address: str, address: Address = None):
        self.name = name
        self.phone_number = phone_number
        self.email_address = email_address
        self.address = address

    def purchase_parking_pass(self) -> None:
        """
        Simulasi pembelian kartu parkir.
        (+purchaseParkingPass())
        """
        print(f"{self.name} telah berhasil membeli kartu parkir kampus.")
    
    def __str__(self):
        addr_info = f"Lives at: {self.address.output_as_label()}" if self.address else "Address: Not provided"
        return f"Person: {self.name}, Email: {self.email_address}. {addr_info}"


## Class Student (Subclass dari Person)
class Student(Person):
    """
    Merepresentasikan Mahasiswa, merupakan jenis dari Person.

    Atribut:
        student_number (int): Nomor mahasiswa. (+studentNumber: int)
        average_mark (int): Rata-rata nilai (0-100). (+averageMark: int)
        _professor_supervisors (list): Daftar Profesor yang mengawasi (untuk relasi supervises).
    """
    def __init__(self, name: str, phone_number: str, email_address: str, address: Address, student_number: int, average_mark: int):
        # Memanggil constructor kelas induk (Person)
        super().__init__(name, phone_number, email_address, address)

        # Atribut spesifik Student
        self.student_number = student_number
        self.average_mark = average_mark
        # Digunakan untuk relasi: 0..* supervises Professor
        self._professor_supervisors = [] 

    def is_eligible_to_enroll(self, required_course: str) -> bool:
        """
        Memeriksa apakah mahasiswa layak untuk mendaftar pada mata kuliah tertentu.
        Asumsi: Dianggap eligible jika average_mark > 70.
        (+isEligibleToEnroll(str): bool)
        """
        if self.average_mark > 70:
            print(f"Student {self.name} Eligible to enroll in {required_course}.")
            return True
        print(f"Student {self.name} Not eligible to enroll in {required_course} (Mark: {self.average_mark}).")
        return False

    def get_seminars_taken(self) -> int:
        """
        Mengembalikan jumlah seminar yang telah diambil.
        Asumsi: Mengembalikan nilai statis 5 untuk contoh.
        (+getSeminarsTaken(): int)
        """
        return 5 # Nilai placeholder untuk demonstrasi

    def add_supervisor(self, professor_obj):
        """Menambahkan Professor sebagai supervisor (untuk relasi supervises)."""
        if professor_obj not in self._professor_supervisors:
            self._professor_supervisors.append(professor_obj)

    def __str__(self):
        return (f"Student: {self.name} (NIM: {self.student_number}), "
                f"Avg Mark: {self.average_mark}. "
                f"Supervisors: {len(self._professor_supervisors)}")


## Class Professor (Subclass dari Person)
class Professor(Person):
    """
    Merepresentasikan Dosen, merupakan jenis dari Person.

    Atribut:
        _salary (int): Gaji (Derived property /salary: int).
        _staff_number (int): Nomor staf. (Protected #staffNumber: int)
        __years_of_service (int): Lama tahun mengabdi. (Private -yearsOfService: int)
        number_of_classes (int): Jumlah kelas yang diampu. (+numberOfClasses: int)
        _supervised_students (list): Daftar Mahasiswa yang diawasi (untuk relasi supervises).
    """
    def __init__(self, name: str, phone_number: str, email_address: str, address: Address, staff_number: int, years_of_service: int, number_of_classes: int):
        # Memanggil constructor kelas induk (Person)
        super().__init__(name, phone_number, email_address, address)

        # Atribut spesifik Professor, menggunakan konvensi Python
        self._staff_number = staff_number # Protected (single underscore)
        self.__years_of_service = years_of_service # Private (double underscore)
        self.number_of_classes = number_of_classes
        self._supervised_students = [] # Digunakan untuk relasi: Professor (1..5) supervises Student (0..*)

    @property
    def salary(self) -> int:
        """
        Properti derived (/salary: int). Gaji dihitung berdasarkan masa kerja.
        """
        base_salary = 10_000_000
        # Asumsi: Gaji bertambah 1 juta per tahun service
        return base_salary + (self.__years_of_service * 1_000_000)

    # Getter untuk years_of_service (karena private)
    def get_years_of_service(self) -> int:
        """Mengembalikan nilai lama pengabdian (atribut private)."""
        return self.__years_of_service

    def add_supervised_student(self, student_obj: Student) -> bool:
        """
        Menambahkan Student yang diawasi, memastikan batas 5 mahasiswa terpenuhi.
        """
        if 1 <= len(self._supervised_students) < 5:
             if student_obj not in self._supervised_students:
                self._supervised_students.append(student_obj)
                student_obj.add_supervisor(self) # Memastikan relasi dua arah
                return True
        
        elif len(self._supervised_students) == 0:
            self._supervised_students.append(student_obj)
            student_obj.add_supervisor(self)
            return True
            
        print(f"Warning: Professor {self.name} sudah mengawasi 5 mahasiswa (batas maksimum).")
        return False

    def __str__(self):
        return (f"Professor: {self.name} (Staff No: {self._staff_number}), "
                f"Classes: {self.number_of_classes}, "
                f"Years of Service: {self.get_years_of_service()}, "
                f"Current Salary: Rp {self.salary:,.0f}")