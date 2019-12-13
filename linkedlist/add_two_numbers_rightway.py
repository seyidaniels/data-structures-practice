# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        firstValue = (self.getValues(l1)[::-1])
        secondValue = (self.getValues(l2)[::-1])

        firstValue = int(''.join([str(s) for s in firstValue]))
        secondValue = int(''.join([str(s) for s in secondValue]))

        finalValue = str(firstValue + secondValue)

        finalValue = [int(s) for s in finalValue][::-1]

        print(finalValue)

        node = ListNode(finalValue[0])

    def getValues(self, l1):
        current = l1
        data = []
        while current.next != None:
            data.append(current.val)
            current = current.next
        data.append(current.val)

        return data
    