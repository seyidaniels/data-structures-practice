class BST(object):
    root = None

    def insert(self, data):
        if self.root:
            return self.root.insert(data)
        self.root = Node(data)
        return True

    def find(self, data):
        if self.root:
            return self.root.find(data)
        return False

    def preorder(self):
        if self.root:
            return self.root.preorder([])
        else:
            return []

    def postorder(self):
        if self.root:
            return self.root.postorder([])
        else:
            return []

    def inorder(self):
        if self.root:
            return self.root.inorder([])
        else:
            return []

    def remove(self, data):
        if self.root == None:
            return False
        if self.root.data == data:
            if self.root.left == None and self.root.right == None:
                self.root == None
                return True
            elif self.root.left and self.root.right == None:
                self.root = self.root.left
                return True
            elif self.root.right and self.root.left == None:
                self.root = self.root.right
                return True
            else:
                moveNode = self.root.right
                moveNodeParent = None
                while moveNode.left:
                    moveNodeParent = moveNode
                    moveNode = moveNode.left
                self.root.data = moveNode.data
                if moveNode.data < moveNodeParent.data:
                    moveNodeParent.left = None
                else:
                    moveNodeParent.right = None
                return True
        # Find node to remove
        parent = None
        node = self.root
        while node and node.data != data:
            parent = node
            if data < node.data:
                node = node.left
            elif data > node.data:
                node = node.right
        # Case 3: Node not found
        if node == None or node.data != data:
            return False
        # Case 4: Node has no children
        elif node.left is None and node.right is None:
            if data < parent.data:
                parent.left = None
            else:
                parent.right = None
            return True
        # Case 5: Node has left child only
        elif node.left and node.right is None:
            if data < parent.data:
                parent.left = node.left
            else:
                parent.right = node.left
            return True
        # Case 6: Node has right child only
        elif node.left is None and node.right:
            if data < parent.data:
                parent.left = node.right
            else:
                parent.right = node.right
            return True
        # Case 7: Node has left and right child
        else:
            moveNodeParent = node
            moveNode = node.right
        while moveNode.left:
            moveNodeParent = moveNode
            moveNode = moveNode.left
        node.data = moveNode.data
        if moveNode.right:
            if moveNode.data < moveNodeParent.data:
                moveNodeParent.left = moveNode.right
            else:
                moveNodeParent.right = moveNode.right
        else:
            if moveNode.data < moveNodeParent.data:
                moveNodeParent.left = None
            else:
                moveNodeParent.right = None
        return True


class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

    def insert(self, data):
        if self.data == data:
            return False
        elif data < self.data:
            if self.left != None:
                return self.left.insert(data)
            self.left = Node(data)
            return True
        else:
            if self.right != None:
                return self.right.insert(data)
            self.right = Node(data)
            return True

    def find(self, data):
        if self.data == data:
            return True
        elif self.data > data and self.right != None:
            return self.right.find(data)
        elif self.data < data and self.right != None:
            return self.left.find(data)
        return False

    def preorder(self, array):
        array.append(self.data)
        if self.left:
            self.left.preorder(array)
        if self.right:
            self.right.preorder(array)
        return array

    def inorder(self, array):
        if self.left:
            self.left.preorder(array)
        array.append(self.data)
        if self.right:
            self.right.preorder(array)
        return array

    def postorder(self, array):
        if self.left:
            self.left.preorder(array)
        if self.right:
            self.right.preorder(array)
        array.append(self.data)

        return array


bst = BST()
bst.insert(8)
bst.insert(3)
bst.insert(16)
bst.insert(2)
bst.insert(7)
bst.insert(10)
bst.insert(25)
print(bst.inorder())
