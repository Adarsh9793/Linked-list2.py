# Linked List Implementation with Insertion a new node

from requests import head


class Node:
    def __init__(self, value):
        self.val = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def printLinkedList(self):
        temp = self.head
        while temp is not None:
            print(temp.val, end=" ")
            temp = temp.next
        print()  # for newline

    def insertionAtTail(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node

    def insertionAtHead(self, value):
        temp = Node(value)
        temp.next = self.head
        self.head = temp

    def insertion(self , value , k):
        if k==0:
            self.insertionAtHead(value)
            return
        
        count = 2
        temp = self.head
        while count < k:
            count += 1
            temp = temp.next

        rest = temp.next
        temp.next = Node(value)
        temp.next.next = rest




# Test
linkedList = LinkedList()
linkedList.insertionAtTail(1)
linkedList.insertionAtTail(2)
linkedList.insertionAtTail(3)
linkedList.insertionAtHead(0)
linkedList.insertion(5,4)

linkedList.printLinkedList()
