# LAB 5
# REMINDER: The work in this assignment must be your own original work and must be completed alone.

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
    def __str__(self):
        return ("Node({})".format(self.value)) 

    __repr__ = __str__


class BinarySearchTree:
    """
        >>> my_tree = BinarySearchTree() 
        >>> my_tree.isEmpty()
        True
        >>> my_tree.isBalanced
        True
        >>> my_tree.insert(9) 
        >>> my_tree.insert(5) 
        >>> my_tree.insert(14) 
        >>> my_tree.insert(4)  
        >>> my_tree.insert(6) 
        >>> my_tree.insert(5.5) 
        >>> my_tree.insert(7)   
        >>> my_tree.insert(25) 
        >>> my_tree.insert(23) 
        >>> my_tree.getMin
        4
        >>> my_tree.getMax
        25
        >>> 67 in my_tree
        False
        >>> 5.5 in my_tree
        True
        >>> my_tree.isEmpty()
        False
        >>> my_tree.getHeight(my_tree.root)   # Height of the tree
        3
        >>> my_tree.getHeight(my_tree.root.left.right)
        1
        >>> my_tree.getHeight(my_tree.root.right)
        2
        >>> my_tree.getHeight(my_tree.root.right.right)
        1
        >>> my_tree.isBalanced
        False
        >>> my_tree.insert(10)
        >>> my_tree.isBalanced
        True
    """
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root=Node(value)
        else:
            self._insert(self.root, value)

    def _insert(self, node, value):
        if(value<node.value):
            if(node.left==None):
                node.left = Node(value)
            else:
                self._insert(node.left, value)
        else:   
            if(node.right==None):
                node.right = Node(value)
            else:
                self._insert(node.right, value)  

    def isEmpty(self):
        # YOUR CODE STARTS HERE
        return self.root == None

    @property
    def getMin(self): 
        # YOUR CODE STARTS HERE
        node = self.root
        if node is None:
            return None
        while node.left is not None:
            node = node.left
        return node.value

    @property
    def getMax(self): 
        # YOUR CODE STARTS HERE
        node = self.root
        if node is None:
            return None
        while node.right is not None:
            node = node.right
        return node.value
                    
    def __contains__(self,value):
        # YOUR CODE STARTS HERE
        return self._contains(self.root,value)
    
    def _contains(self,node,value):
        if node == None:
            return False
        elif node.value == value:
            return True
        elif value < node.value:
            return self._contains(node.left,value)
        elif value > node.value:
            return self._contains(node.right,value)

    def getHeight(self, node):
        # YOUR CODE STARTS HERE
        if node is None:
            return -1
        return 1 + max(self.getHeight(node.left), self.getHeight(node.right))

    @property
    def isBalanced(self):  # Do not modify this method
        return self._isBalanced(self.root)
    
    def _isBalanced(self, node):
        # YOUR CODE STARTS HERE
        if node is None:
            return True
        if abs(self.getHeight(node.left) - self.getHeight(node.right)) > 1:
            return False
        return self._isBalanced(node.left) and self._isBalanced(node.right)

def run_tests():
    import doctest
    doctest.testmod(verbose=True)
    
if __name__ == "__main__":
    run_tests()