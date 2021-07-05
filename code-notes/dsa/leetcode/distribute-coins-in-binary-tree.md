### [distribute-coins-in-binary-tree](https://leetcode.com/problems/distribute-coins-in-binary-tree/)

## Approach 1 [recursion]

Time : O(n)
Space : O(h) h->n in worst case

### explanation
```
1. for a sub-tree number of outgoing or incoming coins delta = sum(sub-tree) - nodeCount(sub-tree)
2. sign indicate direction of flow
3. total moves to distribute coins is nothing but sumOf(abs(delta) for all subtrees in a tree)
```

```cpp
class Solution {
public:
    pair<int,int> helper(TreeNode* root,int& ans){
        if(root == NULL) return {0,0};
        pair<int,int> lst = helper(root->left,ans);
        pair<int,int> rst = helper(root->right,ans);
        int lDelta = abs(lst.first-lst.second);
        int rDelta = abs(rst.first-rst.second);
        ans += (lDelta + rDelta);
        return {1+lst.first+rst.first,root->val+lst.second+rst.second};
        
    }
    int distributeCoins(TreeNode* root) {
        int ans = 0;
        pair<int,int> nodeAnsSum = helper(root,ans);
        return ans;
    }
};
``` 

```cpp
Input: root = [0,3,0]
Output: 3
Explanation: From the left child of the root, we move two coins to the root [taking two moves]. Then, we move one coin from the root of the tree to the right child.
```

## tags:
$tree$
$recursion$