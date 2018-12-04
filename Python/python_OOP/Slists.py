class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class SList:
    def __init__(self, value):
        node = Node(value)
        self.head = node
    
    def addNode(self, addValue):
        node = Node(addValue)
        runner = self.head
        while(runner.next != None):
            runner = runner.next
        runner.next = node

    def removeNode(self,delValue):
        runner = self.head
        if runner is not None:
            if runner.value == delValue:
                self.head = runner.next
                runner = None
                return
        
        while(runner.next != None):
            if runner.value == delValue:
                break
            prev = runner
            runner = runner.next

        if runner == None:
            print(delValue, " Not Found")
            return

        prev.next = runner.next

        runner = None
       
    def printAllValues(self):
        runner = self.head
        while(runner.next != None):
            print(runner.value)
            runner = runner.next
        print(runner.value)
        


x = SList(1)
x.addNode(5)
x.addNode(23)
x.addNode(12)
x.addNode(2)
x.addNode(125)
x.printAllValues()
print("\n\n","="*50,"\n\n")
x.removeNode(1)
x.removeNode(23)
# x.removeNode(85)
x.printAllValues()