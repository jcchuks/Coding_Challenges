/**
 * 
 * https://leetcode.com/problems/binary-tree-paths/#/description
 * 
 * Given a binary tree, return all root-to-leaf paths.

   For example, given the following binary tree:

        1
      /   \
     2     3
      \
       5
     All root-to-leaf paths are:

     ["1->2->5", "1->3"]
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
 */
class Solution {
 
public:
    vector<string> binaryTreePaths(TreeNode* root) {
        vector<string> array;
        if(!root){
            return array;
        }
        
        string newStr;
        dfs(root,newStr,array,true); 
        return array;
    }
    
    void dfs (TreeNode* node, string newstr, vector<string> &array,bool ROOT){
        /*
        * A depth first search problem
        * @Thoughts: problems like this often need the 01,10,11,00 condition.
        * @params String newarray: used for for storing concatenated strings
        * @params array vector: (note passing by reference)
        * @params bool ROOT, used to distinguish the root from the rest nodes
        */
        if(!node){
            return ;
        }
        newstr = ROOT? std::to_string(node->val) : newstr + "->" + std::to_string(node->val);
        if(node->left && !node->right) {dfs(node->left,newstr,array,false);}
        if(node->right && !node->left){dfs(node->right,newstr,array,false);}
        if(node->right && node->left){
            dfs(node->left,newstr,array,false);
            dfs(node->right,newstr,array,false);
        }
        if(!node->left && !node->right){
             array.push_back(newstr); 
        }
    }
    
    
};
