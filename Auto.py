from Database import Database   # hier die Klasse importieren!

class Auto(Database):
    def __init__(self, name="", brand="", sql_query=""):
        super().__init__(sql_query)

        self.name = name
        self.brand = brand

        if not self.name:
            self.name = "name is not set"
        if not self.brand:
            self.brand = "brand is not set"

    def show(self):
        print(self.name)
        print(self.brand)


