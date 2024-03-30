import math

class persegi:
    def __init__(self, sisi):
        self.sisi = sisi
        
    def luas(self):
        return self.sisi ** 2
    
class oval:
    def __init__(self, jari_jari):
        self.jari_jari = jari_jari
        
    def luas(self):
        return math.pi * self.jari_jari ** 2
    
    
if __name__ == "__main__":
    persegi = persegi(5)
    oval = oval(3)
    
    print(f"Luas Persegi : {persegi.luas()}")
    print(f"oval : {oval.luas()}")