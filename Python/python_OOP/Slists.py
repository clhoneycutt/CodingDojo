class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class SList:
    def __init__(self, value):
        node = Node(value)
        self.head = node
    
    def addNode(self, value):
        node = Node(value)
        runner = self.head
        while(runner.next != None):
            runner = runner.next
        runner.next = node

    def removeNode(self,value):
        node = Node(value)
        runner = self.head
        while(runner.next != None):
            if node.value == value:
                runner = runner.next.next
            
        

    def printAllValues(self):
        runner = self.head
        while(runner.next != None):
            print(runner.value)
            runner = runner.next
        print(runner.value)
        


x = SList(1)
x.addNode(5)
x.printAllValues()