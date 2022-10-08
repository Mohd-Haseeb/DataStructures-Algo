
from main import Node

def reverseLL(head:Node) -> Node:
    curr:Node = head
    prev:Node = None

    while curr != None:
        temp : Node = curr.next
        curr.next = prev
        curr = temp
    
    return prev


def traverseLL(head:Node):
    
    if head==None:
        return

    curr:Node = head
    while(curr.next):
        print(curr.data, end=" -> ")
        curr = curr.next






if __name__ == '__main__':
    n1 = Node(12)
    n2 = Node(43)
    n3 = Node(98)
    n4 = Node(9328)
    n5 = Node(54)
    n6 = Node(1)
    n7 = Node(86)

    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = n6
    n6.next = n7

    new_head = reverseLL(n1)
    traverseLL(new_head)