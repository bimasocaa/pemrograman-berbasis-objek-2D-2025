class Pengiriman:
    def __init__(self, asal, tujuan):
        self.asal = asal
        self.tujuan = tujuan

    def estimasi_waktu(self):
        return 5  


class PengirimanDarat(Pengiriman):
    def __init__(self, asal, tujuan, maskapai):
        super().__init__(asal, tujuan)
        self.maskapai = maskapai

    def estimasi_waktu(self):
        if self.maskapai.lower() == "jne":
            return 4
        elif self.maskapai.lower() == "tiki":
            return 5
        elif self.maskapai.lower() == "pos indonesia":
            return 6
        else:
            return 7


class PengirimanUdara(Pengiriman):
    def __init__(self, asal, tujuan, maskapai):
        super().__init__(asal, tujuan)
        self.maskapai = maskapai

    def estimasi_waktu(self):
        if self.maskapai.lower() == "garuda":
            return 2
        elif self.maskapai.lower() == "lion air":
            return 3
        else:
            return 4


class PengirimanInternasional(PengirimanDarat, PengirimanUdara):  
    def __init__(self, asal, tujuan, maskapai, jalur):
        Pengiriman.__init__(self, asal, tujuan)  
        self.maskapai = maskapai
        self.jalur = jalur  

    def estimasi_waktu(self):
        if self.jalur == "darat":
            waktu = PengirimanDarat.estimasi_waktu(self)
        elif self.jalur == "udara":
            waktu = PengirimanUdara.estimasi_waktu(self)
        else:
            waktu = super().estimasi_waktu()

        if self.tujuan.lower() != "indonesia":
            waktu += 3  
        return waktu



pengiriman1 = PengirimanInternasional("Jakarta", "Malaysia", "JNE", "darat")
pengiriman2 = PengirimanInternasional("Bandung", "Indonesia", "TIKI", "darat")
pengiriman3 = PengirimanInternasional("Surabaya", "Singapura", "Pos Indonesia", "darat")
pengiriman4 = PengirimanInternasional("Sidoarjo", "Jepang", "JNT", "darat")
pengiriman5 = PengirimanInternasional("Bali", "Australia", "Garuda", "udara") 

pengiriman_list = [pengiriman1, pengiriman2, pengiriman3, pengiriman4, pengiriman5]


print("=" * 50)
print("  📦 INFO ESTIMASI PENGIRIMAN INTERNASIONAL 📦")
print("=" * 50)

for pengiriman in pengiriman_list:
    print(f"🌍 Dari: {pengiriman.asal}")
    print(f"📍 Tujuan: {pengiriman.tujuan}")
    print(f"🚚 Maskapai: {pengiriman.maskapai}")
    print(f"✈️ Jalur: {pengiriman.jalur}")
    print(f"⏳ Estimasi Waktu: {pengiriman.estimasi_waktu()} hari")
    print("-" * 50)
