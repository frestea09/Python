from src.Fruit import *
import psycopg2
def main():
    try:
        insertName = input('Nama Buah : ')
        insertQty = int(input("Qty Buah : "))
        insertPrize = int(input("Prize Buah: "))
        objFruit = Fruit()
        objFruit.getAll()
        objFruit.setName(insertName)
        objFruit.setPrize(insertPrize)
        objFruit.setQty(insertQty)
        objFruit.insertFruit()
        objFruit.getAll()
    except(Exception,psycopg2.Error) as e :
        print(e)
        sys.exit(1)
    else:
        sys.exit(1)
if __name__ == "__main__":
    main()