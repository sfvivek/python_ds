class Tree:
    '''abstract base class representation of a tree structure'''

    class Position:
        '''an abstraction representing the locaiton of a single element'''

        def element(self):
            '''return the element stored at this position'''
            raise NotImplementedError('must be impelemented by subclass')

        def __eq__(self, other):
            '''returns True if other Position represents the same locaiton'''
            raise NotImplementedError('must be implemented by subclass')

        def __ne__(self, other):
            '''return True if other doesnot represent the same location'''
            return not(self == other)

    def root(self):
        '''return position representing the tree's root (or None if empty)'''
        raise NotImplementedError('must be implemented by subclass')

    def parent(self, p):
        '''return Position representing p's parent (or None if p is root)'''
        raise NotImplementedError('must be implemented by subclass')

    def num_children(self, p):
        '''returns the number of children that position p has'''
        raise NotImplementedError('must be implemented by subclass')

    def children(self, p):
        '''generate iteration for children of the position p'''
        raise NotImplementedError('must be implemented by subclass')

    def __len__(self):
        '''return total number of elements in the tree'''
        raise NotImplementedError('must be implemented by subclass')

    def is_root(self, p):
        '''return True if Position P represents the root of tree'''
        return self.root() == p

    def is_leaf(self, p):
        '''return true if position p has no children'''
        return self.num_children(p) == 0

    def is_empty(self):
        '''return true if the tree has no elements'''
        return len(self) == 0

    def depth(self, p):
        '''returns number of levels separating p from the root'''
        if self.is_root(p):
            return 0
        else:
            return 1 + self.depth(self.parent(p))

    def _height1(self):
        '''returns the height of the tree based on maximum of the depths of p's
        leafs, runs in o(n^2)'''
        return max(self.depth(p) for p in self.positions() if self.is_leaf(p))

    def _height2(self, p):
        '''returns the height of a subtree rooted at position p'''
        if self.is_leaf(p):
            return 0
        else:
            return 1 + max(self._height2(c) for c in self.children(p))

    def height(self, p=None):
        '''return the height of subtree rooted at P
        if p is none, returns the height of the entire tree'''
        if p is None:
            p = self.root()
        return self._height2(p)
