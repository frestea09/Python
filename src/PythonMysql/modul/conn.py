from __future__ import print_function
import os,sys,pymysql

def selectAllDatabase():
    try:
        conn = pymysql.connect(
            host = "*",
            user = "*",
            password = "*",
            database = "*"
        )
        curr = conn.cursor()
        query = """
                SELECT NIP,Nama,Alamat,NoHP FROM pegawai ORDER BY NIP
        """
        curr.execute(query)
        row = curr.fetchall()
    except pymysql.InternalError as e:
        print("Error ",e)
        sys.exit()
    else:
        for element in row:
            nip = element[0]
            nama = element[1]
            alamat = element[2]
            noHp = element[3]
            print("%s %s %s %s "%(nip,nama,alamat,noHp))
        curr.close()
    conn.close()
def insertoToDatabase(inputNIP,inputNama,inputAlamat,inputNoHP):
    try:
        conn = pymysql.connect(
            host="*",
            user="*",
            password="*",
            database="*"
        )
        curr = conn.cursor()
        data = (
            inputNIP,inputNama,inputAlamat,inputNoHP
        )
        query = """
            INSERT INTO pegawai(NIP,Nama,Alamat,NoHP) VALUES (%s,%s,%s,%s)
        """
        curr.execute(query,data)
    except pymysql.InternalError as e:
        print("Error ",e)
        conn.rollback()
        sys.exit()
    else:
        conn.commit()
        curr.close()
    conn.close()

def UpdateToDatabase(inputNIP,inputNama,inputAlamat,inputNoHP):
    try:
        data = (
            inputNama,inputAlamat,inputNoHP,inputNIP
        )
        conn = pymysql.connect(
            host="*",
            user="*",
            password="*",
            database="*"
        )
        curr = conn.cursor()
        query = """
                UPDATE pegawai SET  Nama =%s, Alamat=%s, NoHP = %s WHERE NIP = %s
        """
        curr.execute(query,data)
    except pymysql.InternalError as e:
        print("Error",e)
        conn.rollback()
        sys.exit()
    else:
        conn.commit()
        curr.close()
    conn.close()