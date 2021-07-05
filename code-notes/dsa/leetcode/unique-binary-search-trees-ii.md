### [unique-binary-search-trees-ii](https://leetcode.com/problems/unique-binary-search-trees-ii/)

## Approach 1 [recursion]

// not sure
Time : O(Catalan(n))
Space : O(Catalan(n))


```cpp
class Solution {
public:
    vector<TreeNode*> generateHelper(int left,int right){
        vector<TreeNode*> ans;
        if(left > right) return {NULL};
        
        for(int i=left;i<=right;i++){
            vector<TreeNode*> leftSubTrees = generateHelper(left,i-1);
            vector<TreeNode*> rightSubTrees = generateHelper(i+1,right);
            for(auto leftSubTree : leftSubTrees){
                for(auto rightSubTree: rightSubTrees){
                    TreeNode* root = new TreeNode(i);
                    root->left = leftSubTree;
                    root->right = rightSubTree;
                    ans.push_back(root);
                }
            }
        }
        
        return ans;
    }
    vector<TreeNode*> generateTrees(int n) {
        return generateHelper(1,n);  
    }
};
``` 

```cpp
input = 3

output = [[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]
```

## Approach 2 [dp]

[explanation](https://leetcode.com/problems/unique-binary-search-trees-ii/discuss/31493/Java-Solution-with-DP)


## tags:
$tree$
$catalan$
$binary-search-tree$