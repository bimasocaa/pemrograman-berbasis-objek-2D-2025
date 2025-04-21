class Mahasiswa:  
    total_mahasiswa = 0

    def __init__(self, nama, nim, prodi):
        self.nama = nama
        self.nim = nim
        self.prodi = prodi
        self.daftar_matkul = []
        
        if not self.validasi_nim(nim): 
            print(f"! NIM {nim} tidak valid (harus 10 digit dan diawali '23')")
            print("-" * 60)

        Mahasiswa.total_mahasiswa += 1 
    
    def tampilkan_info(self): 
        print("\n" + "=" * 60)
        print(f"NAMA\t: {self.nama.upper()}")
        print(f"NIM\t: {self.nim}")
        print(f"PRODI\t: {self.prodi.upper()}")
        print("\nMATA KULIAH YANG DIAMBIL:")
        for i, matkul in enumerate(self.daftar_matkul, 1):
            status = ""
            if not matkul.validasi_sks(matkul.sks):
                status = " (SKS TIDAK VALID)"
            print(f"{i}. {matkul.nama} - {matkul.sks} SKS{status}")
        print("-" * 60)

    def tambah_matkul(self, matkul):
        if len(self.daftar_matkul) >= 8:
            print(f"! {self.nama} sudah mencapai maksimal 8 matkul")
            return False
            
        self.daftar_matkul.append(matkul)

    @classmethod
    def jumlah_mahasiswa(cls):
        print(f"\nTOTAL MAHASISWA: {cls.total_mahasiswa}")

    @staticmethod
    def validasi_nim(nim):
        nim_str = str(nim)
        return len(nim_str) == 10 and nim_str.startswith('23') 

class MataKuliah:  
    def __init__(self, kode, nama, sks):
        self.kode = kode
        self.nama = nama
        self.sks = sks  

    @staticmethod
    def validasi_sks(sks):
        return sks in {2, 3}

class Kampus:
    def __init__(self, nama, alamat):
        self.nama = nama
        self.alamat = alamat
        if not self.validasi_nama(nama):
            print(f"Nama kampus '{nama}' tidak valid")

    def tampilkan_info(self):
        print("\n" + "="*50)
        print("                 INFORMASI KAMPUS")
        print("="*50)
        print(f"Nama\t: {self.nama}")
        print(f"Alamat\t: {self.alamat}")
        status = "VALID" if self.validasi_nama(self.nama) else "TIDAK VALID"
        print(f"Status\t: {status}")
        print("="*50)

    @staticmethod
    def validasi_nama(nama):
        """Static method validasi menggunakan isalpha() dan isspace()"""
        for char in nama:
            if not (char.isalpha() or char.isspace()):
                return False
        return True


matkuls = [
    MataKuliah("MK001", "Pemrograman Berbasis Objek", 3),
    MataKuliah("MK002", "Struktur Data", 3),
    MataKuliah("MK003", "Algoritma", 3),
    MataKuliah("MK004", "Basis Data", 4),  
    MataKuliah("MK005", "Jaringan Komputer", 3),
    MataKuliah("MK006", "Sistem Operasi", 3),
    MataKuliah("MK007", "Kalkulus", 2),
    MataKuliah("MK008", "Logika Matematika", 5) 
]


mahasiswas = [
    Mahasiswa("Andi Wijaya", "2312345678", "Teknik Informatika"), 
    Mahasiswa("Budi Santoso", "2311111111", "Sistem Informasi"),
    Mahasiswa("Cindy Lestari", "2322222222", "Teknik Komputer"),
    Mahasiswa("Dedi Pratama", "2333333333", "Sistem Informasi"),
    Mahasiswa("Eva Nurlela", "2344444444", "Teknik Informatika"),
    Mahasiswa("Fani Anggraeni", "2355555555", "Teknik Komputer")
]


kampus = Kampus("Universitas Indonesia ", "Depok")  # Nama tidak valid


for i, mhs in enumerate(mahasiswas):
    # Setiap mahasiswa mengambil 4-5 matkul acak
    matkul_diambil = [matkuls[(i+j) % len(matkuls)] for j in range(4 if i % 2 == 0 else 5)]
    for matkul in matkul_diambil:
        mhs.tambah_matkul(matkul)

# Menampilkan informasi
print("\n" + "=" * 60)
print("LAPORAN DATA MAHASISWA".center(60))
print("=" * 60)
for mhs in mahasiswas:
    mhs.tampilkan_info()

# Menampilkan info kampus
kampus.tampilkan_info()

Mahasiswa.jumlah_mahasiswa()
