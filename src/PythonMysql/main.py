from __future__ import print_function
from abc import ABCMeta,abstractmethod
from pathlib import Path
import modul.conn
import sys,os,pymysql

def main():
    myModul = modul.conn
    print("Tabel Pegawai")
    myModul.selectAllDatabase()
    print("\n")
    print("Data Input")
    inputNIP = input("NIP : ")
    inputNama = input("Nama : ")
    inputAlamat = input("Alamat : ")
    inputNoHP = input("No HP : ")
    myModul.insertoToDatabase(inputNIP,inputNama,inputAlamat,inputNoHP)
    print("\n")
    print("Table setelah Update")
    myModul.selectAllDatabase()
    print("\n")
    inputNipSearch = input("Nip :")
    inputNamaUpdate = input("Nama : ")
    inputAlamatUpdate = input("Alamat :")
    inputNoHPupdate = input("No hp : ")
    myModul.UpdateToDatabase(inputNipSearch,inputNamaUpdate,inputAlamatUpdate,inputNoHPupdate)
    print("tabel setelah update")
    myModul.selectAllDatabase()
    os.system("pause")

if __name__ == "__main__":
    main()