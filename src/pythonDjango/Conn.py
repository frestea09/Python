from __future__ import print_function
from abc import ABCMeta,abstractmethod
from pathlib import Path
import os,psycopg2,sys

class KerangkaCopy(metaclass=ABCMeta):
    @abstractmethod
    def conn(self):
        pass

class Conn(KerangkaCopy):
    def __int__(self,insertUserName=None,insertPassword=None,insertHost=None,insertDatabase=None):
        self.__host = insertHost
        self.__username = insertUserName
        self.__password = insertPassword
        self.__database = insertDatabase
    def setUserName(self,insertUsername):
        self.__username = insertUsername
    def setPassword(self,insertPassword):
        self.__password = insertPassword
    def setHost(self,insertHost):
        self.__host = insertHost
    def setDatabase(self,insertDatabase):
        self.__database = insertDatabase
    def getUsername(self):
        return self.__username
    def getPassword(self):
        return self.__password
    def getDatabase(self):
        return self.__database
    def getHost(self):
        return self.__host
    def conn(self):
        try:
            connect = psycopg2.connect(
                host='localhost',
                user='postgres',
                password ='',
                database = 'db_barang'
            )
            try:
                curr = connect.cursor()
                return curr
            except:
                print("Can't Reach Database")
                sys.exit(1)
            else:
                connect.close()
        except (Exception,psycopg2.Error) as e:
            print('Error : ',e)
        else:
            connect.close()




