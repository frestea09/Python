#name-file : kondisi_pertama.py
#info : bentuk umum sebuah kondisi yang harus kamu kenal
from __future__ import print_function

def main():
    #input
    inputBilanganPertama = int(input('Bilangan Pertama : '))
    inputBilanganKedua = int(input('Bilangan Kedua : '))
    #membuat satu variabel penampung
    hasilPembanding = " "
    #cobain sama < ye kalau sudah mengerti >
    if(inputBilanganPertama>inputBilanganKedua):
        hasilPembanding = "Bilangan Pertama Lebih besar dari bilangan Kedua"
    else:
        hasilPembanding = "Bilangan Kedua lebih besar dari bilangan Pertama"
    #menampilkan Variabel dan hasil
    print("Bilangan Pertama = %d "%(inputBilanganPertama))
    print("Bilangan Kedua = %d"%(inputBilanganKedua))
    print("Hasil Perbandingan : %s"%(hasilPembanding))
    #mmm~ ada kelemahannya kasih tau apa ya..
if __name__ == "__main__":
    main()