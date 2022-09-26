class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def traversal(self):
        if self.head is None:
            print("It is an empty Linked List.")
        else:
            currentNode = self.head
            while currentNode is not None:
                print(currentNode.data)
                currentNode=currentNode.next

    def insertAtLast(self,value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
        else:
            currentNode = self.head
            while currentNode.next is not None:
                currentNode = currentNode.next
            currentNode.next = newNode

    def insertAtStart(self, value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
        else:
            currentNode = self.head
            # while self.head is not None:
            self.head = newNode
            newNode.next = currentNode




# node1 = Node(5)
# node2 = Node(7)
# node3 = Node(11)
# # print(node1)
# # print(node1.data)
# l1 = LinkedList()
# l1.traversal()
list1 = LinkedList()
list1.insertAtLast(5)
# list1.traversal()
list1.insertAtLast(13)
list1.insertAtStart(15)
list1.traversal()
