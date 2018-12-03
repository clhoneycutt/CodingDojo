class product:
    def __init__(self,price,name,weight,brand,status="For Sale"):
        self.price = price
        self.name = name
        self.weight = weight
        self.brand = brand
        self.status = status

    def sell(self):
        self.status = "Sold"
        return self

    def addTax(self, tax):
        self.price += (self.price * tax)
        return self

    def returnItem(self, reason_for_return):
        if reason_for_return == "defective":
            self.status = "defective"
        elif reason_for_return == "like_new":
            self.status = "For Sale"
        elif reason_for_return == "opened":
            self.status = "Used"
            self.price *= .80
        return self

    def display_info(self):
        print("\nPrice: ", self.price,
            "\nName: ", self.name,
            "\nWeight: ", self.weight,
            "\nBrand: ", self.brand,
            "\nStatus: ", self.status, "\n")
        return self


    
toycar = product(50, "speedracer", 5, "Mattel", "For Sale")
toycar.addTax(0.06).display_info()