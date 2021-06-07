import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT # Avoid sql injection


class User:
    def __init__(self, host="localhost", name="postgres", password="********", database="postgres"):
        self.__host = host
        self.__name = name
        self.__password = password
        self.__database = database;

    def get_host(self):
        return self.__host

    def get_username(self):
        return self.__name

    def get_password(self):
        return self.__password

    def get_database(self):
        return self.__database

    def set_database(self, new_database):
        self.__database = new_database


class Database:
    def __init__(self, user):
        try:
            self.user = user
            self.conn = psycopg2.connect(
                host=self.user.get_host(),
                user=self.user.get_username(),
                password=self.user.get_password(),
                database=self.user.get_database())

            self.cursor = self.conn.cursor()
            self.conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            print("Connection with database was not established.\n")

    def use_database(self, database_name):
        self.user.set_database(database_name)
        self.__init__(self.user)