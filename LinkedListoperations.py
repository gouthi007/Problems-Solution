class Node:
    def __init__(self, data, NextNode = None):
        self.data = data
        self.NextNode = NextNode

class LinkedList:
    def __init__(self, head = None):
        self.head = head
        self.size = 0
    def getSize(self):
        return self.size
    def addNode(self, data):
        newNode = Node(data, self.head)
        self.head = newNode
        self.size += 1
    def print(self):
        curr = self.head
        while curr is not None:
            print("Data is: ", + curr.data)
            curr = curr.NextNode
    def deleteNode(self, data):
        curr = self.head
        previousNode = None
        while curr is not None:
            if curr.data == data:
                print("data deleted", data)
                print("original size:", self.size, "now size is:", self.size)
                self.size -= 1
                print("now size is:", self.size)
                previousNode.NextNode = curr.NextNode
                return
            elif curr.data != data and curr.NextNode is not None:
                previousNode = curr
                curr = curr.NextNode
            else:
                print("not present")
                return
    
mylist = LinkedList()
mylist.addNode(123)
print(mylist.getSize())
mylist.addNode(2123)
print(mylist.getSize())
mylist.addNode(333123)
print(mylist.getSize())
mylist.addNode(14444423)
print(mylist.getSize())
mylist.addNode(123555555)
mylist.addNode(123666666)
print(mylist.getSize())
mylist.print()
mylist.deleteNode(33323)
print(mylist.getSize())
