# Soal pratikum 1 bima
class Manusia:
    def __init__(self, nama, umur, alamat):
        self.nama = nama
        self.umur = umur
        self.alamat = alamat
    
    def berjalan(self):
        return f"{self.nama} (umur {self.umur}, alamat {self.alamat}) sedang berjalan."
    
    def berlari(self):
        return f"{self.nama} (umur {self.umur}, alamat {self.alamat}) sedang berlari."

# Membuat objek dari class Manusia
manusia1 = Manusia("farhan", 25, "Lamongan")
manusia2 = Manusia("bima", 30, "Bangkalan")
manusia3 = Manusia("arza", 22, "Surabaya")
manusia4 = Manusia("bima", 28, "Sampang")
manusia5 = Manusia("irsyad", 35, "Pamekasan")

# Contoh penggunaan method berjalan dan berlari
print(manusia1.berjalan())
print(manusia2.berlari())
print(manusia3.berjalan())
print(manusia4.berlari())
print(manusia5.berjalan())