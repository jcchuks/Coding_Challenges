
'''
https://leetcode.com/problems/path-sum/#/description
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        answer = False
        total = 0
        if root is None:
            return answer
        
        return self.sumAndCheck(root,total,sum,answer)
            
    def sumAndCheck(self,node,total,sum,answer):
        '''
        @thought process:
        - Use a depth first search,
        - set a base condition, if answer is true, just return and exit happily.
        - else, at each valid node, check if the node is a leaf and if the val plus total
        equal the sum, if true, you have found your result,just return.
        - if not, check on the left node, then check then check right and return answer.
        - Your base condition takes care of unnecessary traversal.
        - If you reach the leaf without finding the sum, return False.
        '''
        if answer:
            return True 
            
        elif node:
            if self.isLeaf(node) and (node.val + total) == sum:
                return True
            else:
                answer = self.sumAndCheck(node.left,node.val + total,sum, answer) 
                answer = self.sumAndCheck(node.right,node.val + total,sum,answer)
                return answer 
        else:
            return False
                
    def isLeaf(self,node):
        '''
        @params takes a valid node
        @return bool
        '''
        return not node.left and not node.right
        
