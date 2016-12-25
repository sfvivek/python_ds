class BinaryTree:
    '''class to implement a binary tree'''

    def __init__(self, rootObj):
        '''initalization to the class'''
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newNode):
        '''insert to the left of the root node'''
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t 

    def insertRight(self, newNode):
        '''insert to the right of the node'''
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getRightChild(self):
        '''returns the right child of root'''
        return self.rightChild

    def getLeftChild(self):
        '''returns the left child of root'''
        return self.leftChild

    def setRootVal(self, obj):
        self.key = obj

    def getRootVal(self):
        return self.key

    def preorder(self):
        '''preorder tree traversal'''
        print (self.key)
        if self.leftChild:
            self.leftChild.preorder()
        if self.rightChild:
            self.rightChild.preorder()

    def inorder(self):
        '''inorder tree traversal'''
        if self.leftChild:
            self.leftChild.preorder()
        print (self.key)
        if self.rightChild:
            self.rightChild.preorder()

    def postorder(self):
        '''postorder tree traversal'''
        if self.leftChild:
            self.leftChild.preorder()
        if self.rightChild:
            self.rightChild.preorder()
        print (self.key)
