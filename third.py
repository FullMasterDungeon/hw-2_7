class Person():
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    def calculate_age(self, after_years):
        self.sum_years = after_years + self.age
        print(f"через {after_years} лет {self.name} будет {self.sum_years} лет")

p = Person('John', 23, 'male')
p.calculate_age(10)