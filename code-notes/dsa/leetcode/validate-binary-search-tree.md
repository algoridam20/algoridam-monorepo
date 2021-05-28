# [validate-binary-search-tree](https://leetcode.com/problems/validate-binary-search-tree)

## Approach 1 [in-order]

Time : O(n)
Space : O(h), worst case h -> n i.e. O(n)

bst -> inorder traversal is sorted ,
can use that fact to check weather a tree is BST or not

```cpp
class Solution {
public:
    
    bool inOrderTraversal(TreeNode* root,TreeNode* &prev){
        if(root == NULL) return true;
        if(!inOrderTraversal(root->left,prev)) return false;
        if(prev != NULL && prev->val >= root->val) return false;
        prev = root;
        if(!inOrderTraversal(root->right,prev)) return false;
        return true;
        
    }
    bool isValidBST(TreeNode* root) {
        TreeNode* prev = NULL;
        return inOrderTraversal(root,prev);
    }
};
```

## Approach 2 [recursion]

Time : O(n)
Space : O(h), worst case h -> n i.e. O(n)


```cpp
bool isValidBST(TreeNode* root) {
    return isValidBST(root, NULL, NULL);
}

bool isValidBST(TreeNode* root, TreeNode* minNode, TreeNode* maxNode) {
    if(!root) return true;
    if(minNode && root->val <= minNode->val || maxNode && root->val >= maxNode->val)
        return false;
    return 
        isValidBST(root->left, minNode, root) && 
        isValidBST(root->right, root, maxNode);
}
```

## tags:
$recursion$
$tree$
$dfs$
$in-order$