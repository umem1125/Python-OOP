class Kampus:
    nama = ""
    alamat = ""

class Mahasiswa:
    nama = ""
    nim = 0

    def perkenalan(self):
        print(f"Halo nama saya: {self.nama}")

    def hello(self, nama):
        print(f"Hello {nama}, nama saya {self.nama}")

mahasiswa = Mahasiswa()
mahasiswa.nama = "Jokowi"
mahasiswa.perkenalan()
mahasiswa.hello("Gibran")


