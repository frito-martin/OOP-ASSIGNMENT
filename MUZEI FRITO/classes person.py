class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce_yourself(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# Create   

person1 = Person("MUZEI", 100)

# Call the method
person1.introduce_yourself()

