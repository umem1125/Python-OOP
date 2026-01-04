class Mahasiswa:
    nim = 0
    nama = ""

    def __init__(self, nim, nama):
        self.nama = nama
        self.nim = nim

mhs = Mahasiswa("Jokowi", 99998)
print(mhs.nama)
print(mhs.nim)

class BankAccount:
    no = ""
    saldo = 0

    def __init__(self, no, saldo=0):
        # validasi saldo
        if saldo < 0:
            raise ValueError("Saldo tidak boleh negatif")


budi = BankAccount("2221111", 1000)
# joko = BankAccount("2221111", -1000)

class Siswa:
    nama = ""
    nis = 0

    def __init__(self, nama, nis):
        self.nama = nama
        self.nis = nis

    def __str__(self):
        return f"Siswa nis '{self.nis}', Nama '{self.nama}'"
    
    def __eq__(self, other):
        return self.nis == other.nis and self.nama == other.nama
    
class Perbandingan:
    a = 0

    def __init__(self, a):
        self.a = a

    def __lt__(self, other):
        return self.a < other.a
    
    def __gt__(self, other):
        return self.a > other.a
    
    def __le__(self, other):
        return self.a <= other.a
    
    def __ge__(self, other):
        return self.a >=  other.a


# swa1 = Siswa("Jokowi", 29919)
# swa2 = Siswa("Jokowi", 29989)
# print(f"Info {swa}")
# print(swa1 == swa2)

check1 = Perbandingan(5)
check2 = Perbandingan(3)
check3 = Perbandingan(5)

print(check1 < check2) # false
print(check1 > check2) # true
print(check1 <= check2) # false
print(check1 >= check2) # true

print(check1 >= check3) # true
        