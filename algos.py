# binary search
class search(object):
    def last_position(self, nums, target):
        '''
        :type nums: List[int]
        :type target: int
        :rtype: int
        '''
        if nums is None or len(nums) == 0:
            return -1
        	
        left = 0
        right = len(nums)-1
            
        while left + 1 < right:
            m = int( left + (right - left) * 1.0 / 2 ) # prevent overflow
            if nums[m] == target:
                left = m
            elif nums[m] < target:
                left = m
            elif nums[m] > target:
                right = m
            else:
                pass
        
        if nums[right] == target:
            return right
        elif nums[left] == target:
            return left
        else:
            return -1

# implementation of binary search tree
# below code (class Node and Tree) are from answer in below SO thread, with some of minor changes made by me
# this is purely for me to learn and understand the implementation of binary search tree
# https://stackoverflow.com/questions/2598437/how-to-implement-a-binary-tree
class Node:
    def __init__(self, val):
        self.l = None
        self.r = None
        self.v = val

class Tree:
    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root

    def add(self, val):
        if(self.root == None): # if an empty tree, value assigned to root
            self.root = Node(val) # crate a new node, and assign to root
        else:
            self._add(val, self.root) # if not an empty tree, use _add function

    def _add(self, val, node):
        if(val < node.v):
            if node.l is None: #exit case
                node.l = Node(val)
            else:
                self._add(val, node.l)
        else:
            if node.r is None: #exit case
                node.r = Node(val) 
            else: 
                self._add(val, node.r) 
            
    def find(self, val):
        if(self.root is not None):
            return self._find(val, self.root)
        else:
            return None
                       
    def _find(self, val, node): 
        if(val == node.v): 
            return node
        elif(val < node.v and node.l != None): 
            return self._find(val, node.l) # add return so that recursive calls can run
        elif(val > node.v and node.r != None): 
            return self._find(val, node.r) # add return so that recursive calls can run

    def deleteTree(self):
        self.root = None

    def printTree(self):
        if(self.root is not None):
            self._printTree(self.root)

    def _printTree(self, node):
        if(node is not None):
            self._printTree(node.l)
            print str(node.v) + ' '
            self._printTree(node.r)


