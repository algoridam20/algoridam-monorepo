### [lowest-common-ancestor-of-a-binary-search-tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree)

## Approach 1 [recursive]

Time : O(n)
Space : O(n)

### explanation
code is self explanatory

```cpp
class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        if(!root || root == p || root == q) return root;    
        if(p->val < root->val && q->val < root->val) 
            return lowestCommonAncestor(root->left,p,q);
        if(p->val > root->val && q->val > root->val) 
            return lowestCommonAncestor(root->right,p,q);
        return root;
        
    }
};
``` 

```cpp
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.
```

## Approach 2 [iterative]

Time : O(n)
Space : O(n)

### explanation
code is self explanatory

```cpp
class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        if(!root || root == p || root == q) return root;    
        TreeNode* curr = root;
        while(curr != NULL){
            int currVal = curr->val;
            int pVal = p->val;
            int qVal = q->val;
            if(currVal > pVal && currVal > qVal)
                curr = curr->left;
            else if(currVal < pVal && currVal < qVal)
                curr = curr->right;
            else
                return curr;
        }
        return NULL;
    }
};
``` 

```cpp
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.
```


## tags:
$recursion$
$tree$