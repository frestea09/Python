#name-file : kondisi_kedua.py
#info : contoh dengan satu kondisi if tampa pilihan kedua atau else
from __future__ import print_function

def main():
    #input
    inputBilanganPertama = input('Bilangan Pertama : ')
    inputBilanganKedua = input('Bilangan Kedua : ')
    #membuat satu variabel penampung
    hasilPembanding = " "
    if(inputBilanganPertama==inputBilanganKedua):
        hasilPembanding = "Bilangan Pertama sama dengan  bilangan Kedua"
    #menampilkan Variabel dan hasil
    print("==========================")
    print("=========Hasil============")
    print("==========================")
    print("Bilangan Pertama = %s "%(inputBilanganPertama))
    print("Bilangan Kedua = %s"%(inputBilanganKedua))
    print("Hasil Perbandingan : %s"%(hasilPembanding))
if __name__ == "__main__":
    main()