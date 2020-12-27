import mysql.connector
import configparser

class DB():
    def read_config(self):
        read_config = configparser.ConfigParser()
        read_config.read("./config/config.ini")
        self.__host = read_config.get("database", "DbServer")
        self.__user = read_config.get("database", "DbUser")        
        self.__password = read_config.get("database", "DbPass")
        self.__database = read_config.get("database", "DbName")

    def __init__(self):
        self.read_config()
        self.db = mysql.connector.connect(
          host = self.__host,
          user=self.__user,
          password=self.__password,
          database=self.__database
        )

    def execute(self,sqlqr):
        cursor = self.db.cursor()
        cursor.execute(sqlqr)
        result = cursor.fetchone()
        cursor.close()
        return result

    def __del__(self):
        self.db.close()