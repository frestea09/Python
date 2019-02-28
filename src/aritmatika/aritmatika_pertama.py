#name-file : aritmatika.py
from __future__ import print_function
import os
def main():
    #mengambil input dari dekstop
    bilanganPertama = int(input('Bilangan Pertama: '))
    bilanganKedua = int(input('Bilangan Kedua: '))
    #aritmatika python
    hasilPenjumlahan = bilanganPertama + bilanganKedua
    hasilPengurangan = bilanganPertama - bilanganKedua
    hasilPerkalian = bilanganPertama * bilanganKedua
    hasilPembagian = bilanganPertama / bilanganKedua
    #menampilkan hasil perhitungan
    print("%d + %d = %d"%(bilanganPertama,bilanganKedua,hasilPenjumlahan))
    print("%d - %d = %d"%(bilanganPertama,bilanganKedua,hasilPengurangan))
    print("%d * %d = %d"%(bilanganPertama,bilanganKedua,hasilPerkalian))
    print("%d / %d = %d"%(bilanganPertama,bilanganKedua,hasilPembagian))

if __name__ == "__main__":
    main()