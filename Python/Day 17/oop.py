class Employee:
    def __init__(self, name, age, position, gender):
        self.name = name
        self.age = age
        self.position = position
        self.gender = gender


employee1 = Employee("Soroush", 28, "Web Developer", "Male")
employee2 = Employee("Someyeh", 27, "Manager", "Female")

print(employee1.name)