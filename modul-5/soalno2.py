from abc import ABC, abstractmethod

class PerangkatElektronik(ABC):
    def __init__(self):
        self.energi_tersisa = 100
        self.total_jam_digunakan = 0

    @abstractmethod
    def nyalakan(self):
        pass

    @abstractmethod
    def matikan(self):
        pass

    @abstractmethod
    def gunakan(self, jam: int):
        pass

    def status(self):
        print("\n=== STATUS PERANGKAT ===")
        print(f"Tipe Perangkat     : {self.__class__.__name__}")
        print(f"Energi Tersisa     : {self.energi_tersisa}%")
        print(f"Total Digunakan    : {self.total_jam_digunakan} jam")
        print("=" * 30 + "\n")

class Laptop(PerangkatElektronik):
    def nyalakan(self):
        print("🔌 Laptop dinyalakan.")

    def matikan(self):
        print("🛑 Laptop dimatikan.")

    def gunakan(self, jam: int):
        if self.energi_tersisa == 0:
            print("❌ Energi habis. Laptop tidak bisa digunakan!")
            return

        print(f"💻 Menggunakan Laptop selama {jam} jam...")
        self.energi_tersisa -= 10 * jam
        self.total_jam_digunakan += jam
        if self.energi_tersisa <= 0:
            self.energi_tersisa = 0
            print("⚠️  Baterai habis!")

class Kulkas(PerangkatElektronik):
    def nyalakan(self):
        print("🔌 Kulkas dinyalakan.")

    def matikan(self):
        print("🛑 Kulkas dimatikan.")

    def gunakan(self, jam: int):
        if self.energi_tersisa == 0:
            print("❌ Energi habis. Kulkas tidak bisa digunakan!")
            return

        print(f"🧊 Kulkas beroperasi selama {jam} jam...")
        self.energi_tersisa -= 5 * jam
        self.total_jam_digunakan += jam
        if self.energi_tersisa <= 0:
            self.energi_tersisa = 0
            print("⚠️  Energi habis!")
        elif self.energi_tersisa < 20:
            print("⚠️  Energi rendah, kulkas butuh daya tambahan!")


laptop = Laptop()
kulkas = Kulkas()


def jalankan_perangkat(perangkat):
    perangkat.nyalakan()
    while True:
        try:
            jam = int(input(f"Masukkan durasi penggunaan {perangkat.__class__.__name__} (jam): "))
            if jam <= 0:
                print("❌ Durasi harus lebih dari 0 jam.")
                continue
            break
        except ValueError:
            print("❌ Masukkan angka yang valid!")

    perangkat.gunakan(jam)
    perangkat.status()
    perangkat.matikan()


def main():
    while True:
        print("=== MENU PERANGKAT ELEKTRONIK ===")
        print("1. Gunakan Laptop")
        print("2. Gunakan Kulkas")
        print("3. Keluar")
        pilihan = input("Pilih menu (1/2/3): ")
        print("-" * 40)

        if pilihan == '1':
            jalankan_perangkat(laptop)
        elif pilihan == '2':
            jalankan_perangkat(kulkas)
        elif pilihan == '3':
            print("👋 Terima kasih telah menggunakan program ini!")
            break
        else:
            print("❌ Pilihan tidak valid!\n")


if __name__ == "__main__":
    main()
