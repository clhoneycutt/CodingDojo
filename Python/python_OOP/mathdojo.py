class mathDojo:
    def __init__(self, *args):
        self.total = 0
    
    def add(self, *args):
        subtotal = 0
        for i in range(len(args)):
            subtotal += args[i]
        self.total += subtotal
        return self
        

    def sub(self, *args):
        subtotal = 0
        for i in range(len(args)):
            subtotal -= args[i]
        self.total -= subtotal
        return self

    def results(self):
        print("Total: ", self.total)
        return self
        


md = mathDojo()
md.add(2).add(2,5,1).sub(3,2).results()
