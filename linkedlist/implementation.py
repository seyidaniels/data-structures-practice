# Data is stored in multiple non-contiguous blocks of Memories
# Data is stored with Link to the next Node
# The address of the Last Node is None
# The addresses are random and are not in sequence
# The identity of the LInked List is the adress of the First Node


class Node:
    next = None

    def __init__(self, data):
        self.data = data


class LinkedList:
    def __init__(self, head):
        node = Node(head)
        self.head = node

    # def isEmpty(self):
    #     if len(self.list) == 0:
    #         return True
    #     return False

    # def __str__(self):
    #     for l in self.list:
    #         print('Data is ', l.data, 'NEXT is ', l.next)

    def insert(self, data):
        node = Node(data)
        currentNode = self.head
        print (currentNode.data)
        while (currentNode.next != None):
            currentNode = currentNode.next

        currentNode.next = node
    
    def find(self, data):
        currentNode = self.head
        index = 0
        if currentNode.data == data:
            return 0
        while currentNode.next != None:
            currentNode = currentNode.next
            if (currentNode.data == data):
                return index
        
            index += 1
        return - 1

    def reverse(self):
        currentNode = self.head
        print (currentNode)
        data = []
        while currentNode.next != None:
            data.append(currentNode.data)
            print(data)
            currentNode = currentNode.next
        return data
    



linkedList = LinkedList('1')
linkedList.insert('a')
linkedList.insert('b')
linkedList.insert('c')
linkedList.insert('d')
# linkedList.printData()
find = linkedList.find('d')
print(find)
reverse = linkedList.reverse()
print (reverse[::-1])

