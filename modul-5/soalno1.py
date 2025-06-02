class Manusia:
    def berbicara(self):
        print("Manusia berbicara...")

    def bekerja(self):
        print("Manusia bekerja...")

    def makan(self):
        print("Manusia makan...")


class Bima(Manusia):
    def berbicara(self):
        print("Bima berbicara dengan logat Jawa yang halus.")

    def bekerja(self):
        print("Bima bekerja sebagai petani di sawah.")

    def makan(self):
        print("Bima makan dengan tangan tanpa sendok.")


class Beni(Manusia):
    def berbicara(self):
        print("Beni suka bercerita dengan suara lantang.")

    def bekerja(self):
        print("Beni bekerja sebagai mekanik bengkel.")

    def makan(self):
        print("Beni makan sambil menonton TV.")


class Fani(Manusia):
    def berbicara(self):
        print("Fani berbicara dengan sopan dan lembut.")

    def bekerja(self):
        print("Fani bekerja sebagai desainer grafis.")

    def makan(self):
        print("Fani makan makanan sehat dan bergizi.")


class Jani(Manusia):
    def berbicara(self):
        print("Jani sering berbicara sambil tertawa.")

    def bekerja(self):
        print("Jani bekerja sebagai musisi jalanan.")

    def makan(self):
        print("Jani makan sambil bermain gitar.")


def pilih_karakter(nama):
    karakter_dict = {
        "Bima": Bima(),
        "Beni": Beni(),
        "Fani": Fani(),
        "Jani": Jani()
    }
    return karakter_dict.get(nama)


def main():
    print("=== PROGRAM PERILAKU MANUSIA ===")
    while True:
        print("\nPilih karakter yang ingin ditampilkan:")
        print("1. Bima\n2. Beni\n3. Fani\n4. Jani\n5. Keluar")
        pilihan = input("Masukkan nama sesuai menu atau angka pilihan: ").strip()

        if pilihan.lower() in ['5', 'keluar', 'exit']:
            print("Terima kasih! Program selesai.")
            break

        nama_map = {
            '1': 'Bima',
            '2': 'Beni',
            '3': 'Fani',
            '4': 'Jani'
        }

 
        karakter_nama = nama_map.get(pilihan, pilihan)
        karakter = pilih_karakter(karakter_nama)

 
        if pilihan in ['bima', 'beni', 'fani', 'jani']:
            print(" Penulisan nama harus sesuai dengan menu (awali huruf besar, contoh: 'Bima').")

        elif karakter:
            print(f"\n=== Perilaku {karakter_nama} ===")
            karakter.berbicara()
            karakter.bekerja()
            karakter.makan()
        else:
            print("❌ Karakter tidak dikenali. Silakan coba lagi.")

if __name__ == "__main__":
    main()
