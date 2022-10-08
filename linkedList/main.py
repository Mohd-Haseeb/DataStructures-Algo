
class Node:
    next
    data:int
    def __init__(self,data) -> None:
        self.data=data
        self.next = None


def traverseLL(head:Node):

    if head==None:
        return

    curr:Node = head
    while(curr.next):
        print(curr.data, end=" -> ")
        curr = curr.next

def middleLL(head:Node):
    slow:Node = head
    fast:Node = head

    while (fast != None and fast.next != None):
        slow = slow.next
        fast = fast.next.next

    return slow.data


# Delete an element whose pointer is given in linked LIST



    


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

    traverseLL(n1)
    print()
    middle_ll = middleLL(n1)
    print(f"Middle element in Linked list is -> {middle_ll}")