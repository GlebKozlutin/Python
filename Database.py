class Database:
    def __init__(self, sql_query):
        self.sql_query = sql_query
        if not self.sql_query:
            print("Sql_query is not set")

    def __connect(self):
        print("i am private function and i try to connect")

    def insert(self):
        self.__connect()
        print(f"i will give {self.sql_query} to db")

    def update(self):
        self.__connect()
        print(f"i will give {self.sql_query} to db")

    def delete(self):
        self.__connect()
        print(f"i will give {self.sql_query} to db")

    def select(self):
        self.__connect()
        print(f"i will give {self.sql_query} to db")
