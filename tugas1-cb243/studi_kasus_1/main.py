# main.py
from campus_classes import Address, Student, Professor

def main():
    """
    Fungsi utama untuk mendemonstrasikan implementasi Studi Kasus 1.
    """
    print("====== Demo Studi Kasus 1 ======")
    

    # 1. Inisialisasi Address
    print("\n[1. Inisialisasi Address]")
    addr_kampus = Address("Jln. Raya Puputan No.86", "Denpasar Timur", "Kota Denpasar", 80234, "Indonesia")
    print(f"Alamat: {addr_kampus.output_as_label()}")
    print(f"Alamat Valid? {addr_kampus.is_valid()}")

    # 2. Inisialisasi Professor
    print("\n[2. Inisialisasi Professor]")
    prof_dosen = Professor(
        name="Dr. Rudy",
        phone_number="081999359001",
        email_address="rudy.@stikombali.ac.id",
        address=addr_kampus,
        staff_number=1001,
        years_of_service=10,
        number_of_classes=3
    )
    print(prof_dosen)
    prof_dosen.purchase_parking_pass() # Method dari Person

    # 3. Inisialisasi Student
    print("\n[3. Inisialisasi Student]")
    mhs_a = Student(
        name="Ellery",
        phone_number="0895394025773",
        email_address="240030341@stikombali.ac.id",
        address=addr_kampus,
        student_number=240030341,
        average_mark=85
    )
    mhs_b = Student(
        name="Raditya",
        phone_number="0851234568",
        email_address="240030054@stikombali.ac.id",
        address=addr_kampus,
        student_number=240030054,
        average_mark=65
    )
    print(mhs_a)
    print(mhs_b)

    # 4. Demonstrasi Method Student
    print("\n[4. Demonstrasi Student Methods]")
    mhs_a.is_eligible_to_enroll("CB243")
    mhs_b.is_eligible_to_enroll("CA233")
    print(f"Ellery telah mengambil {mhs_a.get_seminars_taken()} seminar.")
   

    # 5. Demonstrasi Relasi Supervises
    print("\n[5. Demonstrasi Relasi Supervises]")
    prof_dosen.add_supervised_student(mhs_a)
    prof_dosen.add_supervised_student(mhs_b)
    
    print(prof_dosen)
    print(mhs_a)
    print(mhs_b)


if __name__ == "__main__":
    import datetime
    main()