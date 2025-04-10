class Mahasiswa:
    def __init__(self, nama, nim, jurusan, alamat):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
        self.alamat = alamat

    def tampilkan_info(self):
        print("\nData Mahasiswa:")
        print(f"Nama     : {self.nama}")
        print(f"NIM      : {self.nim}")
        print(f"Jurusan  : {self.jurusan}")
        print(f"Alamat   : {self.alamat}")

print("\nMasukkan data mahasiswa 1:")
nama1 = input("Nama: ")
nim1 = input("NIM: ")
jurusan1 = input("Jurusan/Prodi: ")
alamat1 = input("Alamat: ")
mahasiswa1 = Mahasiswa(nama1, nim1, jurusan1, alamat1)

print("\nMasukkan data mahasiswa 2:")
nama2 = input("Nama: ")
nim2 = input("NIM: ")
jurusan2 = input("Jurusan/Prodi: ")
alamat2 = input("Alamat: ")
mahasiswa2 = Mahasiswa(nama2, nim2, jurusan2, alamat2)

print("\nMasukkan data mahasiswa 3:")
nama3 = input("Nama: ")
nim3 = input("NIM: ")
jurusan3 = input("Jurusan/Prodi: ")
alamat3 = input("Alamat: ")
mahasiswa3 = Mahasiswa(nama3, nim3, jurusan3, alamat3)

mahasiswa1.tampilkan_info()
mahasiswa2.tampilkan_info()
mahasiswa3.tampilkan_info()