

class bike:
    def __init__(self, price, max_speed, miles):
        self.price = price
        self.max_speed = max_speed
        self.miles = miles
        

    def displayInfo(self):
        print("Price = ",self.price,
            "Max Speed = ", self.max_speed,
            "Total Miles = ", self.miles)
        return self

    def ride(self):
        print("riding")
        self.miles += 10
        return self

    def reverse(self):
        print("Reversing")
        self.miles -= 5
        return self


honda = bike(5000, 80, 10000)
# honda.ride().ride().ride().reverse().displayInfo()

# honda.ride().ride().reverse().reverse().displayInfo()

# honda.reverse().reverse().reverse().displayInfo()


# What would you do to prevent the instance from having negative miles?
# -define self.min_miles = 0 and write an if statement under reverse stating that if miles < min_miles then print("Unable to reverse") else self.miles -=5



# Which methods can return self in order to allow chaining methods?
# -any method other than dunder init