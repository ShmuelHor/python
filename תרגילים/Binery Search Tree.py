class TreeNode:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None
class BinerySearchTree:
    root = None
    def isEmpty(self):
        if not self.root == None:
            return "It's empty"
    def insert(self,val):
        newNode = TreeNode(val)
        if self.root is None:
            self.root = newNode
        else:
            self.rec_insert(newNode,self.root)
    def rec_insert(self,newNode,current):
        if newNode.data < current.data and current.left is None:
            current.left = newNode
            return
        if newNode.data > current.data and current.right is None:
            current.right = newNode
            return
        if newNode.data < current.data:
            self.rec_insert(newNode,current.left)
        else:
            self.rec_insert(newNode, current.right)
    def search(self,val):
        current = self.root
        prev = None
        if self.root is None:
            return "העץ ריק"
        while current.data != val:
            prev = current
            if current.data > val:
                current = current.left
            else:
                current = current.right
        if prev != None:
            return prev
        else:
            return current
    def deleteAle(self,val):
        if self.root == val:
            self.root = None
        prev = self.search(val)
        if prev.left.data == val:
            current = prev.left
        else:
            current = prev.right
        if prev.data > val:
            prev.left = None
        else:
            prev.right = None
    def deleteOneChild(self,val):
        prev = self.search(val)
        if prev.left.data == val:
            current = prev.left
        else:
            current = prev.right
        if current.left != None:
            current = current.left
        else:
            current = current.right
        if current.data > prev.data:
            prev.right = current
        else:
            prev.left = current
    def deleteTwoChildren(self, val):
        prev = self.search(val)
        if self.root == prev:
            current = prev
        elif prev.left.data == val:
            current = prev.left
        else:
            current = prev.right
        left_child = current.left
        right_child = current.right
        max_left = self.found_max(left_child)
        left_child.right = max_left.left
        max_left.left = left_child
        max_left.right = right_child
        if prev.data == val:
            self.root = max_left
        elif prev.data < val:
            prev.right = max_left
        else:
            prev.left = max_left
    def found_min(self,current):
        if self.isEmpty():
            return
        while current.left != None:
            current = current.left
        return current
    def found_max(self,current):
        while current.right != None:
            current = current.right
        return current
    def printi(self):
        self.rec(self.root)
    def rec(self, current):
        if current is None:
            return
        self.rec(current.left)
        if current.data is not None:
            print(current.data)
        self.rec(current.right)

a1 = BinerySearchTree()
a1.insert(56)
a1.insert(88)
a1.insert(30)
a1.insert(93)
a1.insert(66)
a1.insert(45)
a1.insert(12)
a1.insert(70)
a1.insert(60)
a1.insert(65)
a1.deleteTwoChildren(56)
a1.printi()