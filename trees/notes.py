"""
8 Trees:

8.1 General Trees:
    - trees also provide natural organization of data, and consequently
    have become ubiquitous structures in file systems, graphical user
    interfaces, databases, web sites and other computer systems
    - trees are hierarchial, with some objects being above and below others
    - parent, child, ancestor, descendant relationship

8.1.1 Tree Definitions and Properties:
    - a tree is a ADT that stores elements hierarchially, with the exception of
    top element
    - each element has a parent element and zero or more children
    - the top element is called the root of the tree

    ** Formal Tree Definition:
        - we define tree T as a set of nodes storing elements such that nodes
        have a parent-child relationship that satifies the following properties
        - if T is non empty, it has a special node called root of T with no
        parent
        - each node v of T different from the root has a unique parent node w;
        every node with parent w is a child of w

    - the convention allows us to define tree recursively such that a tree T is
    empty or consists of a node r, called the root of T and a possibly empty
    set of subtrees whose roots are children of r

    ** Other Node Relationships:
        - two nodes children of same parent are called siblings
        - a node v is external if v has no children
        - a node v is internal if it has one more more children
        - external nodes are also called leaves of the tree

    ** Edges and Paths in Trees:
        - an edge of a tree T is a pair of nodes (u,v) such that us is a parent
        of v, or vice-versa
        - a path of T is a sequence of nodes such that any two consecutive
        nodes in the sequence form an edge

    - Ex: 8.2 talks about the inheritance for Exceptions in Python represented
    in the form of a tree
    - in python all classes are organized into a single hierarchy, as there
    exists a built-in class named object as the ultimate base class

    - hierarch of various forms of tree
    [tree, [binary tree, [array binary tree, linked binary tree]], [linked tree]]

    - we provide implementations to Tree, Binary Tree, LinkedBinaryTree and
    high level sketches of Array Binary Tree and Linked Tree

    ** Ordered Trees:
        - a tree is ordered if there is a meaningful linear order among the
        children of each node; that is, we purposefully identify the children
        of a node as being the first, second, third and son on.
        - such an order is visualized from left to right according to their
        order
        - Ex: 8.3 talks about the organization of chapters in a book and how it
        is a ordered tree
        - family relationship tree is also modeled after ordered tree
        - in contrast an organizational chart for a company or inheritance
        hierarchy for classes is typically considered an unordered tree

8.1.2 The Tree ADT:
    - we define a tree ADT using a concept of position as an abstraction for a
    node of a tree
    - an element is stored at each position, and positions satisfy parent-child
    relationships that define the tree structure
    - a position of a tree supports the following method
        -- p.element() #returns the element stored at position p
    - following accessor methods are supported as well, allowing a user to
    navigate the various positions of the tree
        -- T.root()
        -- T.is_root(p)
        -- T.parent(p)
        -- T.num_children(p)
        -- T.children(p) #generate iteration of children of position p
        -- T.is_leaf(p)
        -- len(T)
        -- T.is_empty()
        -- T.positions() #generate an iteration of all positions of T
        -- iter(T) #generate iteration of all elements stored within Tree T
    - any of the above methods that accepts position as an argument should
    generate a ValueError if position p is not valid for T
    - if tree is ordered T.children(p) will report the children of p in natural
    order
    - if p is leaf, then T.childre(p) generates an empty iteration
    - we do not define any methods for creating or modifying trees at this
    point
    - we prefer to describe different tree update methods in conjunction with
    specific implementations of the tree interface, and specific applications
    of trees

    ** A Tree ABC in Python:
        - Tree is defined as ABC
        - The tree class provides a definition of a nested Position class
        (which is also abstract) and declarations of any accessor methods
        included in the tree ADT
        - the subclasses are responsible for some of the methods implementation
        depending on their chosen internal representation
        - The Tree class itself is abstract with impelementation of some
        accessor methods

8.1.3 Computing Depth and Height:
    - let p be the position of a node of a tree t.
    - the depth of p is the number of ancestors of p, excluding p itself
    - if p is root the depth is 0

    ** Height:
        - the height of position p in a tree T is also defined recursively
        - if p is a leaf the height of p is 0
        - otherwise, the height of p is one more than the maximum of the height
        of p's children
        - the height of a non-empty tree T is the height of the root T
        - the height of a nonempty tree is the maximum depth of it's leafs
        position


8.2 Binary Trees:
    - a binary tree is an ordered tree with the following properties
    - every node has at most two children
    - each child node is labeled as being either left child or right child
    - left child precedes right child in the order of a node
    - a binary tree is proper if each node has zero or two children
    - a binary tree not proper is improper
    - Ex 8.6 - a decision tree is a proper binary tree
    - Ex 8.7 - an arithmetic expression can be represented by a binary tree
    whose leaves are associated with the variables or constants and whose
    internal nodes are associated with one of the operations +, -, *, /. Each
    node in such a tree has a value associated with it
    - if a node is leaf then the value is variable or constant
    - if a node is internal then it's value is defined by applying it's
    operation to the value of it's children
    - An Aritmetic expression tree is a proper binary tree if you dont'w orry
    about the negation (-x) operation in which case it is improper binary tree
    
    ** A Recursive Binary Tree Definition:
        - a binary tree is either empty or consists of
        - a node r, called the root of T, that stores an element
        - a binary tree (possibly empty), called the left sub tree of T
        - a binary tree (possibly empty), called the right sub tree of T

8.2.1 The Binary Tree ADT:
    - An abstract data type for Binary Tree has the following three
    additionalaccessor methods
    - T.left(p) #returns the left child position of p
    - T.right(p) #return the right child position of p
    - T.sibling(p) # retun the position of sibling of p

8.2.2 Properties of Binary Tree:
    - binary trees have several interesting properties dealing with
    relationships between their heights and the number of nodes
    - we deonte the set of all nodes of a tree T at the same depth d as
    level d of T
    - level 0 has 1 node
    - level 1 has 2 nodes
    - 2^d nodes each level
    - several other properties of binary tree

    ** Relating Internal Nodes to External Nodes in a Proper Binary Tree:
        - in a non empty proper binary tree T, the NE = NI + 1

8.3 Implementing Trees:
    - the tree and binary tree classes that we have defined thus far in this
    chapter are both ABC
    - this section details how we represent a tree and how to navigate a tree
    etc.
    - each node has left child, right child, parent, key stored in it
    - the tree it self maintains an instance variable of the root and the size
    of the tree

8.3.1 Linked Structure for Binayr Trees:

    ** Python Implementation of a Linked Binary Tree:
        - T.add_root(e)
        - T.add_left(p, e)
        - T.add_right(p, e)
        - T.replace(p, e)
        - T.delete(p) #removes the node at position p, replacing it with child
                    #if two children returns error
        - T.attach(p, T1, T2)

8.3.2 Array-Based Representation of a Binary Tree:
    - An alternative representation of a binary tree T is based on a way of
    numbering the positions of T
    - for every position p of T, let f(p) be an integer defined as follows
    - if p is th eroot of the tree then f(p) = 0
    - if p is the left child of a position q, then f(p) = 2f(q) + 1
    - if p is the right child of a position q, then f(p) = 2f(q) + 2
    - the numbering function f is known as a level number of the positions in a
    binary tree T
    - the level numbering function f suggests a representation of a binary tree
    T by means of array-based structure A (such as a python list), with the
    element at position p of T stored at index f(p) of the array
    - one advantage of an array based representation of a binary tree is that a
    position p can be represented by a single integer f(p), and that the
    position-based methods such as root, parent, left and right can be
    implemeted by a formula
    - the space usage of an array based representation depends greatly on the
    shape of the tree
    - let n be the number of nodes of T, and let fm be the maximum value of
    f(p) over all the nodes of the T
    - the array A requires length N = 1 + fm, since the elements range from 0
    to fm
    - note that A may have a number of empty cells that do not refer to
    existing nodes of T
    - in fact, the worst case is N = 2^n -1
    - for binary heaps N = n
    - another draw back for array representation is that some of the update
    operations for trees cannot be efficiently supported.  for example,
    deleting a node and promoting it's child takes O(n) time, because
    everything needs to move

8.3.3 Linked Structure for General Trees:
    - when representing a binary tree with a linked structure, each node
    explicitly maintains left and right as references to individual children
    - for a general tree, there is no priori limit on the number of children
    that a node may have
    - a natural way to realize a general tree T as a linked structure is to
    have each node store a single container of references to it's children


8.4 Tree Traversal Algorithms:
    - a traversal of a tree is a systematic way of accessing or visiting all
    the positions of T
    - the specific action associated with the 'visit' of a position p depends
    on the application of this traversal, and could involve anything from
    incrementing a counter to performing some complex computation for p

8.4.1 Preorder and Postorder Traversal of General Trees:
    - in the pre-order traversal of a tree the root is traversed first, then
    the subtrees rooted at its children are traversed recursively
    - if a tree is ordered, then the subtrees are traversed according to their
    children
    - overall runtime for these tree traversals is O(n)
    - Pseudo Code Preorder:
        Algorithm preorder(T, p):
            perform visit to p
            for each children in T.children(p) do:
                preorder(T,c)
    - Pseudo Code Postorder:
        Algorithm postorder(T, p):
            for each children in T.children(p) do:
                postorder(T,c)
            perform visit to p

8.4.2 Breadth-First Tree Traversal:
    - although pre-order and post order are the common ways to visit a tree,
    another common approach is to traverse a tree so that we visit all the
    positions at depth d before visiting depth d + 1, such an algorithm is
    called depth first search
    - predominatly used in game trees.  Example is Tic-Tac-Toe
    Pseudo Code:
        Algorithm breadthfirst(T):
            Initialize a Q to contain T.root()
            while Q not empty do:
                p = Q.dequeue()
                perform 'visit action'
                for each children in T.children(p) do:
                    Q.enqueue(c)


8.4.3 Inorder Traversal of a Binary Tree:
    - the standard preorder, postorder and bfs can be applied to general trees,
    but inorder can only be applied on binary trees
    - during inorder traversal, we visit a position between the recursive
    traversals of it's left and right subtrees
    - inorder traversal can be considered as visiting the nodes from left to
    right
    - Pseudo Code for Inorder:
        Algorithm inorder(p):
            if p has left children:
                inorder(left children)
            visit p
            if p has right children:
                inorder(right children)
    - the inorder traversal visits positions in a consistent order with the
    standard representation of the expression

    ** Binary Search Trees:
        -



"""

