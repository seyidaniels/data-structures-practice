class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None

    def getNode(self, index):
        if index > self.length() - 1:
            return -1
        if self.head != None:
            current = self.head
            i = 0
            while current != None:
                if i == index:
                    return current
                current = current.next
                i += 1
            return None

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index > self.length() - 1:
            return - 1
        return self.getNode(index).val

    def length(self):
        current = self.head
        length = 1
        while current.next != None:
            current = current.next
            length += 1
        return length

    def printLL(self):
        current = self.head

        while current != None:
            print(current.val)
            current = current.next

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        n = Node(val)
        if self.head != None:
            n.next = self.head
            self.head = n
            return
        self.head = n

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        current = self.head
        while current.next != None:
            current = current.next

        node = Node(val)
        current.next = node

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index > self.length() - 1:
            return -1

        # if index == self.length() - 1:
        #     self.addAtTail(val)
        #     return

        prevNode = self.getNode(index-1)

        prevIndex = index - 1

        current = self.head

        i = 0

        while current.next != None:
            if i == prevIndex:
                node = Node(val)
                node.next = prevNode.next
                prevNode.next = node
                break
            current = current.next
            i += 1

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index > self.length() - 1:
            return -1

        i = 0
        current = self.getNode(index)
        prevNode = self.getNode(index - 1)
        prevNode.next = current.next
        # prevIndex = index - 1
        # while current.next != None:
        #     if i == prevIndex:
        #         prevNode.next = prevNode.next.next
        #         break
        #     current = current.next
        #     i += 1


class Node:

    def __init__(self, val):
        self.val = val
        self.next = None


# Your MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList()
obj.addAtHead(7)
obj.addAtHead(2)
obj.addAtHead(1)
obj.addAtIndex(3, 0)
obj.deleteAtIndex(2)
obj.addAtHead(6)
obj.addAtTail(4)
print(obj.deleteAtIndex(4))
# obj.printLL()
# obj.addAtIndex(1, 2)
# print (obj)
# print(obj.get(6))
# # obj.printLL()
# print(obj.get(1))


# obj.deleteAtIndex(1)


# param_1 = obj.get(6)
# obj.addAtHead(5)
# obj.addAtTail(6)
# obj.addAtIndex(1,1)
# obj.deleteAtIndex(2)

# ["MyLinkedList", "addAtHead", "addAtTail",
#     "addAtIndex", "get", "deleteAtIndex", "get"]
# [[], [1], [3], [1, 2], [1], [1], [1]]
