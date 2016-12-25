from tree_abc import Tree


class BinaryTree(Tree):
    '''abstract base class for binary tree implementation defining additional
    methods'''

    def left(self, p):
        '''returns a position representing p's left child
        returns None if p doesn't have a valide left child'''
        raise NotImplementedError('must be impelemented by a subclass')

    def right(self, p):
        '''returns a position representing p's right child
        returns None if p doesn't have a valide left child'''
        raise NotImplementedError('must be impelemented by a subclass')

    def sibling(self, p):
        '''return a position representing p's sibling, None if nothing'''
        parent = self.parent(p)
        if parent is None:
            return NOne
        else:
            if p == self.left(parent):
                return self.right(parent)
            else:
                return self.left(parent)

    def children(self, p):
        '''generate iteration for positions of p's children'''
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)

