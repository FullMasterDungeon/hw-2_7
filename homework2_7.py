class person:
    age = 30
    height = 183
    weight = 71
    def printer(self):
        print(f"возраст = {self.age}, рост = {self.height}, вес = {self.weight}")
ex = person()
ex.printer()