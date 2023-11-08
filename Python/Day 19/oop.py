class Employee:
    def __init__(self, name, age, position, gender, pronoun):
        self.name = name
        self.age = age
        self.position = position
        self.gender = gender
        self.pronoun = pronoun
    
    def info(self):
        print(f"{self.name} is a very good employee. {self.pronoun} works as a {self.position} and {self.pronoun} is very good at the job, considering the fact that {self.name} is only {self.age}.")


employee1 = Employee("Soroush",28,"Web Developer","Male","He")
employee2 = Employee("Someyeh",27,"Manager","Female","She")

print(employee1.name)
