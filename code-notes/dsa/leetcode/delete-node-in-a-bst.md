### [](https://leetcode.com/problems/)

## Approach 1 [recursion]

Time : O(h) h->n
Space : O(h) h->n

### explanation
```
the required function itself returns pointer, use that fact to design recursion

use the power of recursion always :
also leverage the fact that given tree is binary search tree
all the cases can be easily thought of , using pen and paper :)
```


```cpp
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    TreeNode* findMax(TreeNode* root){
        if(root == NULL) return NULL;
        TreeNode* curr = root;
        while(curr->right != NULL)
            curr = curr->right;
        return curr;
    }
    TreeNode* deleteNode(TreeNode* root, int x) {
        if(root == NULL) return NULL;
        if(root->val == x){
            if(root->left == NULL) return root->right;
            if(root->right == NULL) return root->left;
            TreeNode* max = findMax(root->left);
            max->right = root->right;
            return root->left;
        }
        if(root->val > x){
            root->left = deleteNode(root->left,x);
        }else{
            root->right = deleteNode(root->right,x);
        }
        return root;
    }
};
``` 

```cpp
Input: root = [5,3,6,2,4,null,7], key = 3
Output: [5,4,6,2,null,null,7]
Explanation: Given key to delete is 3. So we find the node with value 3 and delete it.
One valid answer is [5,4,6,2,null,null,7], shown in the above BST.
Please notice that another valid answer is [5,2,6,null,4,null,7] and it's also accepted.
```


## tags:
$tree$
$recursion$
$bst$