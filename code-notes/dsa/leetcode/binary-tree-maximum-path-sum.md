### [binary-tree-maximum-path-sum](https://leetcode.com/problems/binary-tree-maximum-path-sum)

## Approach 1 [dfs,diameter]

Time : O(n)
Space : O(h) h->n in worst case

explanation
Similar to calculating diameter of tree , 
* dfs function return max sum (left or right) branch , while including the TreeNode Value.
* when running this function for all nodes of the tree, 
   max sum path could be max of
    - left + right max branches passing through - TreeNode,
    - only max left along with TreeNode value
    - only max right along with TreeNode value
    - only TreeNode value
    - previously calculated path sum


```cpp
class Solution {
public:
    long ans;
    long maximum(long b, long c, long d, long e, long f){
        return max(b,max(c,max(d,max(e,f))));
    }
    long dfs(TreeNode* root){
        if(!root) return INT_MIN;
        if(!root->left && !root->right){
            ans = max(ans,(long)root->val);
            return (long)root->val;
        }
        long left = dfs(root->left);
        long right = dfs(root->right);
        long val = root->val;
        ans = maximum(ans, val, left+val, right+val, left+right+val);
        return max(max(left,right) + val,val);
    }
    int maxPathSum(TreeNode* root) {
        ans = INT_MIN;
        dfs(root);
        return (int)ans;
    }
};
``` 

```cpp
tree = [-10,9,20,null,null,15,7]

output = 42
The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.
```

## tags:
$tree$
$recursion$
$dfs$