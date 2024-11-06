class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    def __str__(self):
        return f"Name: {self.name}\nBreed: {self.breed}"