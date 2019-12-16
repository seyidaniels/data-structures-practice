# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeElements(self, head: ListNode, val):
        sentinel = ListNode(0)
        sentinel.next = head
        current = head
        previous = sentinel
        while current != None:
            if current.val == val:
                previous.next = current.next
            else:
                previous = current
            current = current.next
        return sentinel.next
