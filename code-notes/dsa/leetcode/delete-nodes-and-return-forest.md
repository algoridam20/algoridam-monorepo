### [delete-nodes-and-return-forest](https://leetcode.com/problems/delete-nodes-and-return-forest)

## Approach 1 [post-order,recursion]

Time : O(n)
Space : O(k)

### explanation
```

```

```cpp
class Solution {
public:
    vector<TreeNode*> forest;
    unordered_set<int> del;
    void helper(TreeNode* root,TreeNode* parent){
        if(root == NULL) return;
        helper(root->left,root);
        helper(root->right,root);
        if(del.count(root->val) != 0){
            if(root->left != NULL) forest.push_back(root->left);
            if(root->right != NULL) forest.push_back(root->right);
            if(parent != NULL){
                if(parent->left == root) parent->left = NULL;
                else parent->right = NULL;
            }
            else{
                swap(forest[0],forest[forest.size()-1]);
                forest.pop_back();
            }
        }
    }
    vector<TreeNode*> delNodes(TreeNode* root, vector<int>& to_delete) {
        forest = {root};
        del.clear();
        for(int val:to_delete){
            del.insert(val);
        }
        helper(root,NULL);
        return forest;
    }
};
``` 

```cpp
input

snapshots

output
```

## Approach 2 [recursion,brute-force]

k size of to delete array
n nodes in tree

Time : O(k*n)
Space : O(k)

### explanation
```
find in forest and delete
finding and deleting in each tree inside the forest.
```

```cpp
class Solution {
public:
    bool findAndDelete(vector<TreeNode*>& forest,int TreeIndex,TreeNode* root,TreeNode* parent,int val){
        if(root == NULL) return false;
        if(root->val == val){
            if(root->left != NULL)
                forest.push_back(root->left);
            if(root->right != NULL)
                forest.push_back(root->right);
            if(parent == NULL){
                swap(forest[TreeIndex],forest[forest.size()-1]);
                forest.pop_back();
            }else{
                if(parent->left == root) parent->left = NULL;
                else parent->right = NULL;
            }
            return true;
        }
        return findAndDelete(forest,TreeIndex,root->left,root,val) || 
            findAndDelete(forest,TreeIndex,root->right,root,val);
    }
    vector<TreeNode*> delNodes(TreeNode* root, vector<int>& to_delete) {
        vector<TreeNode*> forest = {root};
        for(int del: to_delete){
            for(int i=0;i<forest.size();i++){
                if(findAndDelete(forest,i,forest[i],NULL,del))
                    break;
            }
        }
        return forest;
    }
};
``` 

```cpp
input

snapshots

output
```


## tags:
$post-order$
$recursion$
$tree$