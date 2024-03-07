class Mahasiswa:
    def __init__(self, nim, nama, angkatan, isMahasiswa=True):
        self.__nim = nim
        self.__nama = nama
        self.angkatan = angkatan
        self.isMahasiswa = isMahasiswa

    def get_nim(self):
        return self.__nim

    def set_nim(self, nim):
        self.__nim = nim

    def get_nama(self):
        return self.__nama

    def set_nama(self, nama):
        self.__nama = nama

    def cek_lulus(self, ipk):
        if ipk >= 2.75:
            return "Lulus"
        else:
            return "Tidak Lulus"

    def hitung_usia(self, tahun_lahir):
        import datetime
        tahun_sekarang = datetime.datetime.now().year
        return tahun_sekarang - tahun_lahir

    def cek_mahasiswa(self):
        if self.isMahasiswa:
            return "Mahasiswa Aktif"
        else:
            return "Bukan Mahasiswa Aktif"


mahasiswa1 = Mahasiswa("122140013", "Irfan", 2019, True)
print("Mahasiswa 1:")
print("Nama:", mahasiswa1.get_nama())
print("NIM:", mahasiswa1.get_nim())
print("Angkatan:", mahasiswa1.angkatan)
print("Status:", mahasiswa1.cek_mahasiswa())

mahasiswa2 = Mahasiswa("122140028", "Imad", 2020)
print("\nMahasiswa 2:")
print("Nama:", mahasiswa2.get_nama())
print("NIM:", mahasiswa2.get_nim())
print("Angkatan:", mahasiswa2.angkatan)
print("Status:", mahasiswa2.cek_mahasiswa())

print("\nPengujian Metode:")
print("Irfan status lulus dengan IPK 3.0:", mahasiswa1.cek_lulus(3.0))
print("Usia Imad saat ini:", mahasiswa2.hitung_usia(1998), "tahun")
