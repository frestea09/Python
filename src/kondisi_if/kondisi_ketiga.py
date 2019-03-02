#name-file : kondisi_pertama.py
from __future__ import print_function

def main():
    #input
    inputKalimatPertama = input('Kalimat Pertama : ')
    inputKalimatKedua  = input('Kalimat Kedua : ')
    #membuat satu variabel penampung
    hasilPembanding = " "
    if(inputKalimatPertama==inputKalimatKedua):
        hasilPembanding = "Kalimat Pertama Sama dengan Kalimat Kedua"
    else:
        hasilPembanding = "Kalimat Pertama tidak sama dengan Kalimat Kedua"
    #menampilkan Variabel dan hasil
    print("==========================")
    print("=========Hasil============")
    print("==========================")
    print("Kalimat Pertama  = %s "%(inputKalimatPertama))
    print("Kalimat Kedua = %s"%(inputKalimatKedua))
    print("Hasil Perbandingan : %s"%(hasilPembanding))
if __name__ == "__main__":
    main()