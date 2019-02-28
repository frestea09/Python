from __future__ import print_function
from src.conn import *
from abc import ABCMeta,abstractmethod
import os,sys,math,psycopg2

class KerangkaFruit(metaclass=ABCMeta):
    @abstractmethod
    def getAll(self):
        pass
    @abstractmethod
    def insertFruit(self):
        pass
    @abstractmethod
    def updateFruit(self):
        pass
    @abstractmethod
    def deleteFruit(self):
        pass
class Fruit(KerangkaFruit):
    def __init__(self,insertNameFruit=None,insertQtyFruit=None,insertPrize=None):
        objConn = Conn()
        self.__nameFruit = insertNameFruit
        self.__qtyFruit = insertQtyFruit
        self.__prizeFruit = insertPrize
        self.__curr = objConn.conn()
    def setName(self,insertName):
        self.__nameFruit = insertName
    def setQty(self,insertQty):
        self.__qtyFruit = insertQty
    def setPrize(self,insertPrize):
        self.__prizeFruit = insertPrize
    def getName(self):
        return self.__nameFruit
    def getPrize(self):
        return self.__prizeFruit
    def getQty(self):
        return self.__qtyFruit
    def getAll(self):
        try:
            connectionDB = psycopg2.connect(
                #u r host
                host="*",
                #u r user
                user="*",
                #u r password
                password="",
                #u r database
                database="*"
            )
            curr = connectionDB.cursor()
            query = """
                       SELECT * FROM fruit ORDER BY id_fruit
                   """
            curr.execute(query)
            for (id_fruit, name_fruit, qty, prize) in curr:
                print(id_fruit, '\t', name_fruit, '\t', qty, '\t', prize)
        except:
            print("Can't Get Data from Database")
            sys.exit(1)
        else:
            curr.close()

    def insertFruit(self):
        try:
            connectionDB = psycopg2.connect(
                host="*",
                user="*",
                password="*",
                database="*"
            )
            curr = connectionDB.cursor()
            data = (self.getName(),self.getQty(),self.getPrize())
            query = """
                INSERT INTO fruit(id_fruit,name_fruit,qty,prize)
                VALUES(default,%s,%s,%s)
            """
            curr.execute(query,data)
        except(Exception,psycopg2.Error) as e:
            print("Error ",e)
            connectionDB.rollback()
            sys.exit(1)
        else:
            connectionDB.commit()
            curr.close()
    def updateFruit(self):
        pass
    def deleteFruit(self):
        pass