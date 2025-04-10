class Kucing:
    def __init__(self, nama, warna):
        self.nama = nama
        self.warna = warna
    
    def bersuara(self):
        return f"{self.nama} si kucing {self.warna} berkata: Meong!"

class Anjing:
    def __init__(self, nama, ras):
        self.nama = nama
        self.ras = ras
    
    def bersuara(self):
        return f"{self.nama} si anjing {self.ras} berkata: Guk! Guk!"

class Burung:
    def __init__(self, nama, jenis):
        self.nama = nama
        self.jenis = jenis
    
    def bersuara(self):
        return f"{self.nama} si burung {self.jenis} berkata: Cuit! Cuit!"

# Membuat objek menggunakan looping
daftar_hewan = [
    ("Kucing", "Momo", "Putih"),
    ("Anjing", "Buddy", "Golden Retriever"),
    ("Burung", "Kiki", "Kenari")
]

objek_hewan = []

for jenis, nama, atribut in daftar_hewan:
    if jenis == "Kucing":
        objek_hewan.append(Kucing(nama, atribut))
    elif jenis == "Anjing":
        objek_hewan.append(Anjing(nama, atribut))
    elif jenis == "Burung":
        objek_hewan.append(Burung(nama, atribut))


for hewan in objek_hewan:
    print(hewan.bersuara())
    print()