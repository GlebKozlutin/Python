class Database:
    def __init__(self, sql_query):
        self.sql_query = sql_query
        if not self.sql_query:
            print("Sql_query is not set")

    def __connect(self):
        print("i am private function and i try to connect")

    def insert(self):
        self.__connect()
        print(f"i will insert {self.sql_query} to db")

    def __update(self):
        self.__connect()
        print(f"i will update {self.sql_query} to db")

    def __delete(self):
        self.__connect()
        print(f"i will delete {self.sql_query} from db")

    def __select(self):
        self.__connect()
        print(f"i will select {self.sql_query} from db")

    def superUpdate(self):
        self.__update()
        print("super update")