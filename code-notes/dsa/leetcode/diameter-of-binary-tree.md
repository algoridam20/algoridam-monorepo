### [diameter-of-binary-tree](https://leetcode.com/problems/diameter-of-binary-tree/)

## Approach 1 [bfs,diameter]

Time : O(n)
Space : O(h) worst case h -> n : O(n)

explanation
dfs function return max number of node below a given TreeNode
using this functions value for left and right child of given TreeNode, you can find the diameter of the tree.

```cpp
class Solution {
public:
    int dfs(TreeNode* root,int& ans){
        if(root == NULL) return 0;
        int left = dfs(root->left,ans);
        int right = dfs(root->right,ans);
        ans = max(ans,left+right);
        return max(left,right) + 1;
        
    }
    int diameterOfBinaryTree(TreeNode* root) {
        int ans = 0;
        dfs(root,ans);
        return ans;
    }
};
``` 

```cpp
[1,2,3,4,5]

3 is the length of the path [4,2,1,3] or [5,2,1,3].

3
```

## tags:
$tree$
$recursion$
$dfs$