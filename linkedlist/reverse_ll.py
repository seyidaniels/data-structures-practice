# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        previous = None

        while head != None:
            nextNode = head.next
            head.next = previous
            previous = head
            head = nextNode
        return previous
