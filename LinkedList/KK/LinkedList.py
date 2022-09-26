
class Node():

    def __init__(self,value,next=None):
        self.value = value
        self.next = next

    # def

class LinkedList():

    def __init__(self):
        self.head = None

    def insertAtStart(self,value):
        if self.head == None:
            newNode = Node(value)
            self.head = newNode
        else:
            newNode = Node(value)
            newNode.next = self.head
            self.head = newNode

    def display(self):
        temp = self.head
        while(temp):
            print(f'{temp.value} --> ',end='')
            temp = temp.next
        print("None")

    def insertAtEnd(self,value):
        temp = self.head
        newNode = Node(value)
        while(temp.next!=None):
            temp = temp.next
        temp.next = newNode

    def insertBetween(self,value,index):

        if index==0:
            self.insertAtStart(value)
        else:
            temp = self.head
            while(temp!=index-1):
                temp = temp.next
            newNode = Node(value)
            newNode.next = temp.next
            temp.next = newNode

    def deleteFromStart(self):
        temp = self.head
        temp.next = None
        self.head = temp
        # temp = self.head.next
        # self.head.next = None
        # self.head = temp

    def deleteFromEnd(self):
        temp = self.head
        while(temp)




l1 = LinkedList()
l1.display()
l1.insertAtStart(10)
l1.display()
l1.insertAtEnd(11)
l1.display()
l1.insertAtStart(15)
l1.display()
# l1.insertBetween(17,2)
# l1.deleteFromStart()
# l1.display()
