#abstraksi 

from abc import ABC, abstractmethod

class Bentuk(ABC):
    @abstractmethod
    def hitung_luas(self):
        pass

    @abstractmethod
    def hitung_keliling(self):
        pass

class Persegi(Bentuk):
    def __init__(self, sisi):
        self.sisi = sisi

    def hitung_luas(self):
        return self.sisi ** 2

    def hitung_keliling(self):
        return 4 * self.sisi

# Penggunaan
persegi = Persegi(4)
print("Luas:", persegi.hitung_luas())         # Output: 16
print("Keliling:", persegi.hitung_keliling()) # Output: 16

