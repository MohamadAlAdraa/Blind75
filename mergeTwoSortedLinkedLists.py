from typing import Type, List, Union

class Node:
    next = None
    value = None

    def __init__(self, value: int):
        self.value = value
        self.next = None

class LinkedList:
    head = None

    def __init__(self, headNode: Type[Node] = None):
        self.head = headNode

    def add(self, val: int):
        if not isinstance(val, int):
            raise TypeError('Expected integer value')

        newNode = Node(val)
        if self.head is None:
            self.head = newNode
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = newNode

    def addMultiple(self, l: List[int]):
        for i in l:
            self.add(i)

    def traverse(self):
        temp = self.head
        if temp is None:
            print('Linked list is empty')
        else:
            i=0
            while temp.next is not None:
                print('Node', i+1, ':', temp.value)
                temp = temp.next
                i+=1
            print('Node', i+1, ':', temp.value)

    def size(self) -> int:
        temp = self.head
        if temp is None:
            return 0
        s = 0
        while temp is not None:
            s += 1
            temp = temp.next
        return s

# Using my own custom LinkedList class
def merge_v0(l1: LinkedList, l2: LinkedList) -> Union[LinkedList, None]:
    if l1.head is None and l2.head is None:
        return None
    elif l1.head is None:
        return l2
    elif l2.head is None:
        return l1
    temp1 = l1.head
    temp2 = l2.head
    l3 = LinkedList()
    while temp1 and temp2:
        if temp1.value <= temp2.value:
            l3.add(temp1.value)
            temp1 = temp1.next
        else:
            l3.add(temp2.value)
            temp2 = temp2.next
    return l3

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_v1(l1: Union[ListNode, None], l2: Union[ListNode, None]) -> Union[ListNode, None]:
    if l1 is None and l2 is None:
        return None
    elif l1 is None:
        return l2
    elif l2 is None:
        return l1
    temp1 = l1
    temp2 = l2
    l3 = ListNode()
    head = l3
    while temp1 and temp2:
        if temp1.val <= temp2.val:
            l3.next = temp1
            temp1 = temp1.next
        else:
            l3.next = temp2
            temp2 = temp2.next
        l3 = l3.next
    return head.next

if __name__ == '__main__':
    # l1 = LinkedList()
    # l1.addMultiple([2,3,10,20])
    # l2 = LinkedList()
    # l2.addMultiple([1,4,5,11,15])
    # l3 = merge_v0(l1, l2)
    # l3.traverse()
    l1 = ListNode(2,ListNode(3, ListNode(10, ListNode(20))))
    l2 = ListNode(1,ListNode(4, ListNode(5, ListNode(11, ListNode(15)))))
    l3 = merge_v1(l1,l2)
    temp = l3
    while temp is not None:
        print(temp.val, ' ')
        temp = temp.next


