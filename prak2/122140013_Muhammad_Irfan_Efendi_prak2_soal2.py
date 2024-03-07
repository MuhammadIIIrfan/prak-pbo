class kucing:
    def __init__(self, jenis, warna, umur):
        self.jenis = jenis
        self.warna = warna
        self.umur = umur
        
    def __del__(self):
        print(f"kucing {self.jenis} {self.warna} umur {self.umur} telah dihapus")
        
    @staticmethod
    def hitung_usia(tahun_lahir):
        import datetime
        tahun_sekarang = datetime.datetime.now().year
        return tahun_sekarang - tahun_lahir
    
    def info_kucing(self):
        print(f"Info kucing : {self.jenis} {self.warna} umur {self.umur} ")
        print(f"Usia Kucing : {self.hitung_usia(self.umur)} tahun")
        
        
def cek_tahun_lahir(func):
    def wrapper(self, umur):
        if umur > 2024:
            print("tahun lahir kucing tidak valid")
        else :
            func(self, umur)
    return wrapper

class hewan:
    def __init__(self, spesies, usia):
        self.spesies = spesies
        self.usia = usia
        
    def __del__(self):
        print(f"Hewan {self.spesies} tahub {self.usia} telah dihapus")
        
    @staticmethod
    def hitung_usia(tahun_lahir):
        import datetime
        tahun_sekarang = datetime.datetime.now().year
        return tahun_sekarang - tahun_lahir
    
    def info_hewan(self):
        print(f"Informasi hewan : {self.spesies} tahun {self.usia}")
        print(f"Usia hewan : {self.hitung_usia(self.usia)} tahun")

def cek_tahun_valid(func):
    def wrapped(self, usia):
        if usia > 2024:
            print("Tahun Lahir Hewan Tidak Valid !")
        else :
            func(self, usia)
    return wrapped


print("===kucing===")
kucing_1 = kucing("Anggora,", "putih", 2016)
kucing_1.info_kucing()
kucing_2 = kucing("Persia", "hitam", 2019)
kucing_2.info_kucing()
del kucing_1
del kucing_2

print("\n===hewan===")
hewan_1 = hewan("anjing", 2015)
hewan_1.info_hewan()
hewan_2 = hewan("singa", 2017)
hewan_2.info_hewan()
del hewan_1
del hewan_2
            