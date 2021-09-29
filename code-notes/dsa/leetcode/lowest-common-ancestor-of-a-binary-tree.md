### [lowest-common-ancestor-of-a-binary-tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree)

## Approach 1 []

Time : O(n)
Space : O(n)

### explanation
```
lowestCommonAncestor function is finding p and q as well as returning lca
if lca from left is not null and lca from right is also not null that means root is lca
else lca is from left or right which ever is not null

lca return p or q if root->val is same as p's or q's
and null other wise

try a few examples to get the feel of the algo.
```


```cpp
class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        if(root == NULL) return NULL;
        if(root->val == p->val) return p;
        if(root->val == q->val) return q;
        TreeNode* fromLeft = lowestCommonAncestor(root->left,p,q);
        TreeNode* fromRight = lowestCommonAncestor(root->right,p,q);
        if((fromLeft == p || fromLeft == q) && (fromRight == p || fromRight == q))
            return root;
        if(fromLeft) return fromLeft;
        if(fromRight) return fromRight;
        return NULL;
    }
};
``` 

```cpp
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
```


## tags:
$recursion$
$tree$