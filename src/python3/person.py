class Person:
        def __init__(self, name, age, food):
            self.name = name
            self.age = age
            self.food = food

        def speak(self):
            print(f"Feed me more {self.food}s")

        def get_name(self):
            print("The name of this person is", self.name)

        # now you can do print(Person('Bob', 30, 'Tacos')) which will print Bob
        def __str__(self):
            return self.name

