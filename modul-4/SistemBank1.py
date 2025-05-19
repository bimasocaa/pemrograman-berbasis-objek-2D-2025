class RekeningBank:
    def __init__(self, no_rek, nama_pemilik, saldo):
        self.__no_rek = no_rek
        self.__nama_pemilik = nama_pemilik
        self.__saldo = saldo

    def get_no_rek(self):
        return self.__no_rek

    def get_nama_pemilik(self):
        return self.__nama_pemilik

    def get_saldo(self):
        return self.__saldo

    def set_no_rek(self, no_rek_baru):
        self.__no_rek = no_rek_baru

    def set_nama_pemilik(self, nama_baru):
        self.__nama_pemilik = nama_baru

    def set_saldo(self, saldo_baru):
        if saldo_baru >= 0:
            self.__saldo = saldo_baru
        else:
            print("❌ Saldo tidak boleh negatif.")

    def setor_tunai(self, jumlah):
        if jumlah > 0:
            self.__saldo += jumlah
            print(f"✅ Setor tunai sebesar {jumlah} berhasil. Saldo sekarang: {self.__saldo}")
        else:
            print("❌ Jumlah setor tunai tidak valid.")

    def tarik_tunai(self, jumlah):
        if 0 < jumlah <= self.__saldo:
            self.__saldo -= jumlah
            print(f"✅ Tarik tunai sebesar {jumlah} berhasil. Saldo sekarang: {self.__saldo}")
        else:
            print("❌ Jumlah tarik tunai tidak valid atau saldo tidak cukup.")


class Bank:
    def __init__(self):
        self.rekening_list = []

    def tambah_rekening(self, rekening):
        self.rekening_list.append(rekening)
        print("✅ Rekening berhasil ditambahkan.")

    def cari_rekening(self, no_rek):
        for rekening in self.rekening_list:
            if rekening.get_no_rek() == no_rek:
                return rekening
        return None

    def tampilkan_rekening(self):
        if self.rekening_list:
            print("\n📋 Daftar Rekening Bank:")
            for rekening in self.rekening_list:
                print(f"- No Rek: {rekening.get_no_rek()}, Nama: {rekening.get_nama_pemilik()}, Saldo: {rekening.get_saldo()}")
        else:
            print("❌ Belum ada rekening yang tersedia.")


def main():
    bank = Bank()

    while True:
        print("\n=== MENU BANK ===")
        print("1. Tambah Rekening")
        print("2. Setor Tunai")
        print("3. Tarik Tunai")
        print("4. Tampilkan Semua Rekening")
        print("5. Keluar")
        print("6. Edit Data Rekening")

        pilihan = input("Pilih menu (1-6): ")

        if pilihan == '1':
            no_rek = input("Masukkan No Rekening: ")
            if not no_rek.isdigit():
                print("❌ Nomor rekening harus berupa angka.")
                continue

            nama = input("Masukkan Nama Pemilik: ")
            try:
                saldo_awal = float(input("Masukkan Saldo Awal: "))
                rekening_baru = RekeningBank(no_rek, nama, saldo_awal)
                bank.tambah_rekening(rekening_baru)
            except ValueError:
                print("❌ Saldo awal harus berupa angka.")

        elif pilihan == '2':
            no_rek = input("Masukkan No Rekening: ")
            rekening = bank.cari_rekening(no_rek)
            if rekening:
                try:
                    jumlah = float(input("Masukkan jumlah setor: "))
                    rekening.setor_tunai(jumlah)
                except ValueError:
                    print("❌ Jumlah setor harus berupa angka.")
            else:
                print("❌ Rekening tidak ditemukan.")

        elif pilihan == '3':
            no_rek = input("Masukkan No Rekening: ")
            rekening = bank.cari_rekening(no_rek)
            if rekening:
                try:
                    jumlah = float(input("Masukkan jumlah tarik: "))
                    rekening.tarik_tunai(jumlah)
                except ValueError:
                    print("❌ Jumlah tarik harus berupa angka.")
            else:
                print("❌ Rekening tidak ditemukan.")

        elif pilihan == '4':
            bank.tampilkan_rekening()

        elif pilihan == '5':
            print("👋 Terima kasih telah menggunakan layanan bank.")
            break

        elif pilihan == '6':
            no_rek = input("Masukkan No Rekening yang ingin diedit: ")
            rekening = bank.cari_rekening(no_rek)
            if rekening:
                print("\n--- Edit Data ---")
                print("1. Edit Nomor Rekening")
                print("2. Edit Nama Pemilik")
                pilihan_edit = input("Pilih data yang ingin diedit (1/2): ")

                if pilihan_edit == '1':
                    no_baru = input("Masukkan Nomor Rekening Baru: ")
                    if not no_baru.isdigit():
                        print("❌ Nomor rekening harus berupa angka.")
                    else:
                        rekening.set_no_rek(no_baru)
                        print("✅ Nomor rekening berhasil diubah.")

                elif pilihan_edit == '2':
                    nama_baru = input("Masukkan Nama Pemilik Baru: ")
                    rekening.set_nama_pemilik(nama_baru)
                    print("✅ Nama pemilik berhasil diubah.")

                else:
                    print("❌ Pilihan tidak valid.")
            else:
                print("❌ Rekening tidak ditemukan.")

        else:
            print("❌ Pilihan tidak valid. Silakan coba lagi.")


main()
