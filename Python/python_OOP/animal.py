class animal:
    def __init__(self, name, health=100):
        self.name = name
        self.health = health

    def walk(self):
        self.health -= 1
        return self

    def run(self):
        self.health -= 5
        return self

    def display_health(self):
        print("Health: ", self.health)


# dog = animal("Fido", 100)
# dog.walk().walk().walk().run().run().display_health()

class dog(animal):
    def __init__(self, name, health=150):
        super().__init__(name, health)

    
    def pet(self):
        self.health += 5
        return self


class dragon(animal):
    def __init__(self, name, health=170):
        super().__init__(name, health)

    def fly(self):
        self.health -= 10
        return self

    def display_health(self):
        super().display_health()
        print("I am a Dragon")
        return self


# fido = dog('Fido')
# fido.walk().walk().walk().run().run().pet().display_health()

# print("\n","*"*50,"\n")



# akatosh = dragon('akatosh')
# akatosh.fly().display_health()

# horse = animal("Roger")

# horse.walk().walk().run().pet().display_health()
# horse.walk().walk().run().fly().display_health()