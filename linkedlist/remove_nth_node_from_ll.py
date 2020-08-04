# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        length = 0
        dummy = ListNode(0)
        dummy.next = head
        c = head
        while c != None:
            length += 1
            c = c.next
        index = length - n
        first = dummy
        while index > 0:
            index -= 1
            first = first.next

        first.next = first.next.next

        return dummy.next
