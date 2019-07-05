class car:
    def __init__(self,price,speed,fuel,mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if self.price > 10000:
            self.tax = 0.15
        else:
            self.tax = 0.12

    def display_all(self):
        print("\nPrice: ", self.price,
            "\nSpeed: ", self.speed, "mph",
            "\nFuel: ", self.fuel,
            "\nMileage: ", self.mileage, "mpg",
            "\nTax: ", self.tax, "\n")
        return self


honda = car(2000, 35, "Full", 15)
honda.display_all()
    
chevy = car(2000, 5, "Not Full", 105)
chevy.display_all()

pontiac = car(2000, 15, "Kind of Full", 95)
pontiac.display_all()

volvo = car(2000, 25, "Full", 25)
volvo.display_all()

subaru = car(2000, 45, "Empty", 25)
subaru.display_all()

lambo = car(20000000, 35, "Empty", 15)
lambo.display_all()
