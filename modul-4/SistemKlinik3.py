class Pasien:
    def __init__(self, nama, umur, keluhan):
        self.__nama = nama
        self.__umur = umur
        self.__keluhan = keluhan

    def get_nama(self):
        return self.__nama

    def get_umur(self):
        return self.__umur

    def get_keluhan(self):
        return self.__keluhan

    def set_nama(self, nama_baru):
        self.__nama = nama_baru

    def set_umur(self, umur_baru):
        self.__umur = umur_baru

    def set_keluhan(self, keluhan_baru):
        self.__keluhan = keluhan_baru

    def get_data(self):
        return {
            "Nama": self.__nama,
            "Umur": self.__umur,
            "Keluhan": self.__keluhan
        }


class Klinik:
    def __init__(self):
        self.__daftar_pasien = []

    def tambah_pasien(self, pasien):
        self.__daftar_pasien.append(pasien)
        print("✅ Pasien berhasil ditambahkan.")

    def tampilkan_daftar_pasien(self):
        if not self.__daftar_pasien:
            print("❌ Belum ada pasien.")
        else:
            print("\n📋 Daftar Pasien:")
            for i, pasien in enumerate(self.__daftar_pasien, start=1):
                data = pasien.get_data()
                print(f"{i}. Nama: {data['Nama']}, Umur: {data['Umur']}, Keluhan: {data['Keluhan']}")

    def edit_data_pasien(self, index):
        if 0 <= index < len(self.__daftar_pasien):
            pasien = self.__daftar_pasien[index]
            print("\n--- Edit Data ---")
            print("1. Nama")
            print("2. Umur")
            print("3. Keluhan")
            pilihan = input("Pilih data yang ingin diubah (1/2/3): ")

            if pilihan == "1":
                nama_baru = input("Masukkan Nama Baru: ")
                pasien.set_nama(nama_baru)
                print("✅ Nama berhasil diperbarui.")

            elif pilihan == "2":
                umur_baru = input("Masukkan Umur Baru: ")
                if not umur_baru.isdigit():
                    print("❌ Umur harus berupa angka.")
                else:
                    pasien.set_umur(int(umur_baru))
                    print("✅ Umur berhasil diperbarui.")

            elif pilihan == "3":
                keluhan_baru = input("Masukkan Keluhan Baru: ")
                pasien.set_keluhan(keluhan_baru)
                print("✅ Keluhan berhasil diperbarui.")

            else:
                print("❌ Pilihan tidak valid.")
        else:
            print("❌ Nomor pasien tidak ditemukan.")


def main():
    klinik = Klinik()
    while True:
        print("\n=== MENU KLINIK ===")
        print("1. Tambah Pasien")
        print("2. Tampilkan Daftar Pasien")
        print("3. Keluar")
        print("4. Edit Data Pasien")

        pilihan = input("Pilih menu (1-4): ")

        if pilihan == "1":
            nama = input("Masukkan Nama: ").strip()
            umur = input("Masukkan Umur: ")
            if not umur.isdigit():
                print("❌ Umur harus berupa angka.")
                continue
            keluhan = input("Masukkan Keluhan: ")
            pasien = Pasien(nama, int(umur), keluhan)
            klinik.tambah_pasien(pasien)

        elif pilihan == "2":
            klinik.tampilkan_daftar_pasien()

        elif pilihan == "3":
            print("👋 Terima kasih. Program selesai.")
            break

        elif pilihan == "4":
            klinik.tampilkan_daftar_pasien()
            nomor = input("Masukkan nomor pasien yang ingin diedit: ")
            if not nomor.isdigit():
                print("❌ Input harus berupa angka.")
                continue
            index = int(nomor) - 1
            klinik.edit_data_pasien(index)

        else:
            print("❌ Pilihan tidak valid. Silakan coba lagi.")


if __name__ == "__main__":
    main()
