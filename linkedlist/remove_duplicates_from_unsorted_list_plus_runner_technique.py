
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        current = head

        while current != None:
            runner = current
            while runner.next != None:
                if runner.val == runner.next.val:
                    runner.next = runner.next.next
                else:
                    runner = runner.next
            current = current.next

        return head

#         previous = None
#         arr = []
#         current = head
#         while current != None:
#             if current.val in arr:
#                 previous.next = current.next
#             else:
#                 arr.append(current.val)
#                 previous = current
#             current = current.next
#         return head
