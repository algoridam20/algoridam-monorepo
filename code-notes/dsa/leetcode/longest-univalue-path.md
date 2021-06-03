### [longest-univalue-path](https://leetcode.com/problems/longest-univalue-path/)

## Approach 1 [bfs,diameter]

Time : O(n)
Space : O(h) h->n O(n)

explanation
longestPathPassingThroughNode return the longest left or right univalue branch ,

longest path is:
     max of paths among all TreeNode

and paths for a TreeNode can be calculated by adding:
    longest left branch and longest right branch, passing through the TreeNode.

```cpp
class Solution {
public:
    int ans;
    int longestPathPassingThroughNode(TreeNode* root){
        if(root == NULL) return 0;
        int left = longestPathPassingThroughNode(root->left);
        int right = longestPathPassingThroughNode(root->right);
        int newLeft = 0;
        int newRight = 0;
        if(root->left != NULL && root->left->val == root->val) newLeft = left + 1;
        if(root->right != NULL && root->right->val == root->val) newRight = right + 1;
        ans = max(ans,newLeft+newRight);
        return max(newLeft,newRight);
    }
    int longestUnivaluePath(TreeNode* root) {
        ans = 0;
        longestPathPassingThroughNode(root);
        return ans;
    }
};
``` 

```cpp
tree = [1,4,5,4,4,5]

longest path contains 2 edges
```


## tags:
$tree$
$recursion$
$dfs$