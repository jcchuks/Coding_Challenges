#define ISEQL(A,B) A->val == B->val

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
bool isSameTree(struct TreeNode* p, struct TreeNode* q) {
    
    if (!p && !q){
        return true;
    }else if(p && q && ISEQL(p,q)){
        #repeat on child nodes
         bool lefts = isSameTree(p->left,q->left);
         bool rights = isSameTree(p->right,q->right);
         if (lefts && rights){
             return true; 
         }else{
             return false; 
         }
    }else{
        return false;
    }
    
}
