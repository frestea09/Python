from __future__ import print_function

def main():
    variabelString = input("Nama :")
    variabelInterger = int(input('Umur :'))
    #ingat float disini pake "." ya, contoh 4.5
    variabelFloat = float(input("IPK : "))
    #output
    print("Nama : %s"% variabelString)
    print("Umur : %d"% variabelInterger)
    #pasti nollnya banyak
    print("IPK : %f"% variabelFloat)
    #membatasi nol pada float %.2f artinya bilangan setelah "." hanya boleh 2 bilangan saja
    print("IPK : %.2f"%variabelFloat)
if __name__ == "__main__":
    main()