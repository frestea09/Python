from __future__ import print_function
from abc import ABCMeta,abstractmethod
from src.config import config
import os,math,psycopg2,sys
class KerangkaConn(metaclass=ABCMeta):
    @abstractmethod
    def conn(self):
        pass

class Conn(KerangkaConn):
    def __init__(self,insertUsername=None,insertPassword=None,insertHost=None,insertDatabase=None):
        self.__username = insertUsername
        self.__password = insertPassword
        self.__host = insertHost
        self.__database = insertDatabase
    def setUsername(self,insertUsername):
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
       return  self.__password
    def getHost(self):
        return self.__host
    def getDatabase(self):
        return self.__database
    def conn(self):
        try:
            connectionDB = psycopg2.connect(
                host = "*",
                user = "*",
                password = "*",
                database = "*"
            )
            try:
                curr = connectionDB.cursor()
                print('Berhasil')
                return curr
            except:
                print("Can't reach the Database")
                sys.exit(1)
            else:
                curr.close()
        except (Exception,psycopg2.Error) as e:
            print('Error',e)
        else:
            connectionDB.close()

