from __future__ import print_function
from abc import ABCMeta,abstractmethod
from src.pythonDjango.Conn import *
import os,sys,psycopg2
def getAll():
    objConn = Conn()
    try:
        curr = objConn.conn()
        query = """
                    SELECT * FROM fruit ORDER BY id_fruit
                """
        curr.execute(query)
        for (id_fruit, name_fruit, qty, prize) in curr:
            print(id_fruit, '\t', name_fruit, '\t', qty, '\t', prize)
    except:
        print("Can't Reach Database")
        sys.exit(1)
    else:
        curr.close()
def insertDB(insertName,insertQty,insertPrize):
    connectionDB = psycopg2.connect(
        host="*",
        user="*",
        password="",
        database="*"
    )
    try:
        curr = connectionDB.cursor()
        data = (insertName, insertQty, insertPrize)
        query = """
                   INSERT INTO fruit(id_fruit,name_fruit,qty,prize)
                   VALUES(default,%s,%s,%s)
            """
        curr.execute(query, data)
    except (Exception, psycopg2.Error) as e:
        print("Can't Reach Database ", e)
        connectionDB.rollback()
        sys.exit(1)
    else:
        connectionDB.commit()
        curr.close()
def updateDb(insertID,insertName,insertQty,insertPrize):
    connectionDB = psycopg2.connect(
        host="*",
        user="*",
        password="",
        database="*"
    )
    try:
        curr = connectionDB.cursor()
        data = (insertName, insertQty, insertPrize,insertID)
        query = """
                   UPDATE fruit SET name_fruit=%s,qty=%s,prize=%s WHERE id_fruit=%s
            """
        curr.execute(query, data)
    except (Exception, psycopg2.Error) as e:
        print("Can't Reach Database ", e)
        connectionDB.rollback()
        sys.exit(1)
    else:
        connectionDB.commit()
        curr.close()
def deleteDb(insertID):
    connectionDB = psycopg2.connect(
        host="*",
        user="*",
        password="",
        database="*"
    )
    try:
        curr = connectionDB.cursor()
        data = (insertID)
        query = """
                   DELETE FROM fruit WHERE id_fruit = %s
            """
        curr.execute(query, data)
    except (Exception, psycopg2.Error) as e:
        print("Can't Reach Database ", e)
        connectionDB.rollback()
        sys.exit(1)
    else:
        connectionDB.commit()
        curr.close()

def main():
    deleteDb('2')
if __name__ == "__main__":
    main()