"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
import sys

sys.path.append('/stack.py')
from stack import Stack

sys.path.append('/queue.py')
from queue import Queue

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value >= self.value:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)
        else:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    # def contains(self, target):
    #     node = self
    #     while node.value != target:
    #         if node.value < target:
    #             node = node.right
    #         else:
    #             node = node.left
    #         if node is None:
    #             return False
    #     return True

    def contains(self, target):
        if self.value == target:
            return True

        elif target >= self.value:
            if self.right is not None:
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        max_value = 0
        node = self
        while True:
            if node.value > max_value:
                max_value = node.value
            elif node.right == None:
                return max_value
            else:
                node = node.right
        return max_value
    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)

        if self.left:
            self.left.for_each(fn)

        if self.right:
            self.right.for_each(fn)

        return None

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node.left:
            node.left.in_order_print(node.left)

        print(node.value)

        if node.right:
            node.right.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        bft_queue = Queue()
        bft_queue.enqueue(node)
        
        while bft_queue.__len__ != 0:
            current_node = bft_queue.dequeue()
            if current_node.left is not None:
                bft_queue.enqueue(current_node.left)
            if current_node.right is not None:
                bft_queue.enqueue(current_node.right)
            print(current_node.value)
        # make a queue
        # enqueue the node
        # as long as the queue is not empty
        # dequeue from the front of the queue, this is our current node
        # enqueue the kids of the current node on the queue

        #queue = Queue(12, 8)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        dft_stack = Stack()
        dft_stack.push(node)

        while dft_stack.__len__ != 0:
            current_node = dft_stack.pop()
            if current_node.left is not None:
                dft_stack.push(current_node.left)
            elif current_node.right is not None:
                dft_stack.push(current_node.right)
            print(current_node)

        # make a stack
        # push the node on the stack
        # as long as the stack is not empty
        # pop off the stack, this is our current node
        # put the kids of the current node on the stack
        # (check that they are not None, then put them on the stack)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass

t = BSTNode(1)
t.insert(8)
t.insert(5)
t.insert(7)
t.insert(6)
t.insert(3)
t.insert(4)
t.insert(2)
t.bft_print(t)