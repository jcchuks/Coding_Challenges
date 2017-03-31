#define MAX(A,B) {int Z  =  A < B ? A : B; return Z+1;}
#define MINR(A,B) {int K = A < B ? A:B; return K + 1;}
#define ISLEAF(A)   !((*A).left || (*A).right) 
#define ISLNR(A)   (*A).left  && !(*A).right
#define ISRNL(A)   !(*A).left  && (*A).right
/**
 * 
 * https://leetcode.com/problems/minimum-depth-of-binary-tree/#/description
 * Given a binary tree, find its minimum depth. 
 * The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
 * 
 * 
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
int minDepth(struct TreeNode* root){
    if(!root){return 0;}
    return mDepth(root);
}

int mDepth(struct TreeNode* root){
    
    if(ISLEAF(root)){
        return 1;
    }else if(ISLNR(root)){
        int z = mDepth(root->left); 
        return z + 1;
    }else if(ISRNL(root)){
        int m = mDepth(root->right);
        return m + 1;
    }else {
        int z = mDepth(root->left);
        int m = mDepth(root->right);
        MINR (z,m);
    }
}
