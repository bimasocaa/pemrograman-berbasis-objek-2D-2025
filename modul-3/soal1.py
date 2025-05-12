
class Karyawan:
    def __init__(self, nama, gaji, departemen):
        self.nama = nama
        self.gaji = gaji
        self.departemen = departemen

    def info(self):
        print(f"Nama       : {self.nama}")
        print(f"Gaji       : {self.gaji}")
        print(f"Departemen : {self.departemen}")


class KaryawanTetap(Karyawan):
    def __init__(self, nama, gaji, departemen, tunjangan):
        super().__init__(nama, gaji, departemen)
        self.tunjangan = tunjangan

    def info(self):
        super().info()
        print(f"Tunjangan  : {self.tunjangan}")
        print(f"Status     : Karyawan Tetap")
        print("-" * 30)


class KaryawanHarian(Karyawan):
    def __init__(self, nama, gaji, departemen, jam_kerja):
        super().__init__(nama, gaji, departemen)
        self.jam_kerja = jam_kerja

    def info(self):
        super().info()
        print(f"Jam Kerja  : {self.jam_kerja} jam/hari")
        print(f"Status     : Karyawan Harian")
        print("-" * 30)

class ManajemenKaryawan:
    def __init__(self):
        self.daftar_karyawan = []

    def tambah_karyawan(self, karyawan):
        self.daftar_karyawan.append(karyawan)

    def tampilkan_semua_karyawan(self):
        print("Daftar Seluruh Karyawan:\n" + "=" * 30)
        for karyawan in self.daftar_karyawan:
            karyawan.info()


manajemen = ManajemenKaryawan()

k1 = KaryawanTetap("Bimaa", 5000000, "IT", 1000000)
k2 = KaryawanHarian("Firdaa", 100000, "Produksi", 8)
k3 = KaryawanTetap("Metaa", 7000000, "HRD", 1500000)
k4 = KaryawanHarian("Apan", 120000, "Gudang", 7)
k5 = KaryawanHarian("Arzhaa", 220000, "Qc", 7)

manajemen.tambah_karyawan(k1)
manajemen.tambah_karyawan(k2)
manajemen.tambah_karyawan(k3)
manajemen.tambah_karyawan(k4)
manajemen.tambah_karyawan(k5)

manajemen.tampilkan_semua_karyawan()
