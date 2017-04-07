
#https://leetcode.com/problems/binary-tree-level-order-traversal/#/description

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Node(object):
    def __init__(self,node,level):
        self.node = node
        self.level = level 
        
class Solution(object):
    
    def __init__(self):
        self.array = [] 
        self.level_counter = 0
        self.result = []
        self.levelq = []
    
    def queue(self,node):
        self.array.append(node)
    
    def isNotEmpty(self):
        return self.array
        
    def popValue(self): 
        value = self.array[0]
        del self.array[0]
        return value
    
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return self.result
        self.queue(Node(root,0)) 
        while self.isNotEmpty(): 
            bigNode = self.popValue()   
            if bigNode.level > self.level_counter: 
                self.level_counter = bigNode.level   
                self.result.append(self.levelq[:])
                self.levelq[:] = []   
                
            self.levelq.append(bigNode.node.val) 
            if bigNode.node.left  : 
                self.queue(Node(bigNode.node.left, bigNode.level + 1))
            if bigNode.node.right  :
                self.queue(Node(bigNode.node.right, bigNode.level + 1))
        if self.levelq:
            self.result.append(self.levelq[:])
            
        return self.result
             
            
            
            
