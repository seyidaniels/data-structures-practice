# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def addTwoNumbers( l1, l2):
    while l1.next != None:
        print (l1)


def getValues( l1):
    current = l1
    data = []
    while current.next != None:
        data.append(current.val)
        current = current.next
    data.append(current.val)

    return data


p = addTwoNumbers([2, 4, 3], [5, 6, 4])

print (p)
