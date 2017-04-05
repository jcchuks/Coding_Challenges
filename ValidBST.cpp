/**
 * Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
Example 1:
    2
   / \
  1   3
Binary tree [2,1,3], return true.
Example 2:
    1
   / \
  2   3
Binary tree [1,2,3], return false.

 * 
 * https://leetcode.com/problems/validate-binary-search-tree/#/description
 * 
 *Solution using inorder Property of BSTs
 * 
 * 
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 * 
 * 
 * 
 */
class Solution {
    private:
    TreeNode* prev = NULL;
public:
    bool isValidBST(TreeNode* root) {
       if(!root){
           return true;
       }
       return check(root);
       
      
    }
    
    bool check(TreeNode* root){ 
         if (!root){
             return true;
         }
          bool goRight = true;
          goRight = check(root->left);
          if (!goRight){
              return goRight;
          }
          
         if(prev != NULL && prev->val >= root->val){
             return false;
         }
         prev = root;
         
         return check(root->right);
        
    }
       
};
