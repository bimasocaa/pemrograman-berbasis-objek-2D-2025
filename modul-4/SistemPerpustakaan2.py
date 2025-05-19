class Buku:
    def __init__(self, judul, penulis, jumlah_halaman):
        self.__judul = judul
        self.__penulis = penulis
        self.__jumlah_halaman = jumlah_halaman

  
    def get_judul(self):
        return self.__judul

    def get_penulis(self):
        return self.__penulis

    def get_jumlah_halaman(self):
        return self.__jumlah_halaman


    def set_judul(self, judul_baru):
        self.__judul = judul_baru

    def set_penulis(self, penulis_baru):
        self.__penulis = penulis_baru

    def set_jumlah_halaman(self, jumlah_baru):
        self.__jumlah_halaman = jumlah_baru


class Perpustakaan:
    def __init__(self):
        self.daftar_buku = []

    def tambah_buku(self, buku):
        self.daftar_buku.append(buku)
        print("✅ Buku berhasil ditambahkan ke perpustakaan.")

    def tampilkan_buku(self):
        if self.daftar_buku:
            print("\n📚 Daftar Buku di Perpustakaan:")
            for i, buku in enumerate(self.daftar_buku, start=1):
                print(f"{i}. Judul: {buku.get_judul()}, Penulis: {buku.get_penulis()}, Halaman: {buku.get_jumlah_halaman()}")
        else:
            print("❌ Tidak ada buku di perpustakaan.")

    def edit_buku(self, index):
        if 0 <= index < len(self.daftar_buku):
            buku = self.daftar_buku[index]
            print("\n--- Edit Buku ---")
            print("1. Judul")
            print("2. Penulis")
            print("3. Jumlah Halaman")
            pilihan = input("Pilih data yang ingin diubah (1/2/3): ")

            if pilihan == '1':
                judul_baru = input("Masukkan Judul Baru: ")
                buku.set_judul(judul_baru)
                print("✅ Judul berhasil diperbarui.")

            elif pilihan == '2':
                penulis_baru = input("Masukkan Penulis Baru: ")
                buku.set_penulis(penulis_baru)
                print("✅ Penulis berhasil diperbarui.")

            elif pilihan == '3':
                try:
                    halaman_baru = int(input("Masukkan Jumlah Halaman Baru: "))
                    buku.set_jumlah_halaman(halaman_baru)
                    print("✅ Jumlah halaman berhasil diperbarui.")
                except ValueError:
                    print("❌ Jumlah halaman harus berupa angka.")

            else:
                print("❌ Pilihan tidak valid.")
        else:
            print("❌ Nomor buku tidak ditemukan.")



def main():
    perpustakaan = Perpustakaan()

    while True:
        print("\n=== MENU PERPUSTAKAAN ===")
        print("1. Tambah Buku")
        print("2. Tampilkan Daftar Buku")
        print("3. Edit Buku")
        print("4. Keluar")

        pilihan = input("Pilih menu (1-4): ")

        if pilihan == '1':
            judul = input("Masukkan Judul Buku: ")
            penulis = input("Masukkan Nama Penulis: ")
            try:
                halaman = int(input("Masukkan Jumlah Halaman: "))
                buku_baru = Buku(judul, penulis, halaman)
                perpustakaan.tambah_buku(buku_baru)
            except ValueError:
                print("❌ Jumlah halaman harus berupa angka!")

        elif pilihan == '2':
            perpustakaan.tampilkan_buku()

        elif pilihan == '3':
            perpustakaan.tampilkan_buku()
            if not perpustakaan.daftar_buku:
                continue
            try:
                nomor = int(input("Masukkan nomor buku yang ingin diedit: ")) - 1
                perpustakaan.edit_buku(nomor)
            except ValueError:
                print("❌ Masukkan angka yang valid.")

        elif pilihan == '4':
            print("👋 Terima kasih telah menggunakan sistem perpustakaan.")
            break

        else:
            print("❌ Pilihan tidak valid. Coba lagi.")


if __name__ == "__main__":
    main()
