class hewan:
    def __init__(self, nama, jenis_kelamin):
        self.nama = nama
        self.nama_kelamin = jenis_kelamin
        
    def suara(self):
        pass
    
    def makanan(self, makanan):
        print(f"{self.nama} sedang makan : {makanan}")
        
    def minum(self):
        print(f"{self.nama} sedang minum")
        
class kucing(hewan):
    def suara(self):
        print(f"Kucing {self.nama} bersuara : meongg")
            
class anjing(hewan):
    def suara(self):
        print(f"anjing {self.nama} bersuara : GukGuk")
            

if __name__ == "__main__":
    hewan1 = kucing("Zumbul", "Jantan")
    hewan2 = anjing("Vladimier", "Betina")
    
    print(hewan1.nama)
    print(hewan2.nama)
    
    hewan1.suara()
    hewan1.makanan("Whiskas")
    
    hewan2.suara()
    hewan2.makanan("Tulang")
    
    
    