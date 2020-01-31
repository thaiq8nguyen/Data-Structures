
import sys
sys.path.append('../queue_and_stack')
from dll_stack import Stack
from dll_queue import Queue


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if self.value is None:
            self.value = BinarySearchTree(value)
            
        else:
            if self.value > value:
                # go to the left side
                if self.left is not None:
                    self.left.insert(value)
                else:
                    self.left = BinarySearchTree(value)
                    return
            else:
                # go to the right side
                if self.right is not None:
                    self.right.insert(value)
                else:
                    self.right = BinarySearchTree(value)
                    return

    # Return True if the tree contains the value
    # False if it does not

    def contains(self, target):
        if self.value > target:
            # go left
            if self.left is None:
                return False
            return self.left.contains(target)


        elif target > self.value:
            # go right
            if self.right is None:
                return False
            return self.right.contains(target)
        else:
            return True

    # Return the maximum value found in the tree
    def get_max(self):
        
        if self.right is None:
            # go left
            return self.value
        else:
            return self.right.get_max()



    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        
        if self.right is not None:
            self.right.for_each(cb)
        if self.left is not None:
            self.left.for_each(cb)
        cb(self.value)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if self.left is not None:
            self.left.in_order_print(self.left)
        print(self.value)
        if self.right is not None:
            self.right.in_order_print(self.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
       
        

        
        queue = Queue()
        queue.enqueue(node)
        while queue.len() > 0:
            current = queue.dequeue()
            print(current.value)
            if current.left is not None:
                queue.enqueue(current.left)
            if current.right is not None:
                queue.enqueue(current.right)
            
        


    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        stack = Stack()
        stack.push(node)

        while stack.len() != 0:
            current = stack.pop()
            print(current.value)
            if current.right is not None:
                stack.push(current.right)
            if current.left is not None:
                stack.push(current.left)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
