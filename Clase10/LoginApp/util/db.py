import mysql.connector
class Database:
    def __init__(self):
        self.host = "localhost"
        self.user = "root"
        self.password = ""
        self.database = "tecnarapp"

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            self.cursor = self.connection.cursor()
            return self.cursor
        except mysql.connector.Error as error:
            print(error)

    def close(self):
        self.cursor.close()
        self.connection.close()

    def insert(self, sql):
        try:
            self.cursor = self.connect()
            self.cursor.execute(sql)
            self.connection.commit()
            self.close()
            return True
        except mysql.connector.Error as error:
            print(error)
            return False
    
    def select(self, sql):
        try:
            self.cursor = self.connect()
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
            self.close()
            return result
        except mysql.connector.Error as error:
            print(error)
            return False
    
    def update(self, sql):
        try:
            self.cursor = self.connect()
            self.cursor.execute(sql)
            self.connection.commit()
            self.close()
            return True
        except mysql.connector.Error as error:
            print(error)
            return False
        
    def delete(self, sql):
        try:
            self.cursor = self.connect()
            self.cursor.execute(sql)
            self.connection.commit()
            self.close()
            return True
        except mysql.connector.Error as error:
            print(error)
            return False
        