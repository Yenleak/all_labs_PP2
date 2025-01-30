class Person:
    count = 0 

    def __init__(self, name, family_name, age, occupation, nationality):
        self.name = name
        self.family_name = family_name
        self.age = age
        self.occupation = occupation
        self.nationality = nationality
        Person.count += 1

    def year_born(self, cur_year):
        return cur_year - self.age 

    def get_name(self):
        return f"{self.name} {self.family_name}"  # surename

    def get_nationality(self):
        return self.nationality  # ulty

    def get_age(self):
        return self.age  # jasy

    def get_occupation(self):
        return self.occupation  # zhumysy

person1 = Person(name="Brad", family_name="Pitt", age=50, occupation="actor", nationality="American")

# 2019-50=1949
year_born = person1.year_born(cur_year=2019)
print(f"{person1.get_name()} was born in {year_born}")
