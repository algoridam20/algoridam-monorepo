### [flatten-binary-tree-to-linked-list](https://leetcode.com/problems/flatten-binary-tree-to-linked-list)

## Approach 1 [morris-traversal]

Time : O(n)
Space : O(1): no additional space is required

### explanation

```py
psudo code:
if root has left sub tree
    move root->right (reference to right sub tree) to right most node of roots left sub tree 
    swap root->left and root->right
    make root->left as null
move root to root->right
do this till root is not null
```

### code
```cpp
class Solution {
public:
    void flatten(TreeNode* root) {
        TreeNode* curr = root;
        while(curr != NULL){
            
            TreeNode* rightMostOfLeftSubTree = curr->left;
            if(rightMostOfLeftSubTree != NULL){
                while(rightMostOfLeftSubTree->right != NULL)
                    rightMostOfLeftSubTree = rightMostOfLeftSubTree->right;
                rightMostOfLeftSubTree->right = curr->right;
                curr->right = curr->left;
                curr->left = NULL;
            }
            curr = curr->right;
        }
    }
};
``` 

```cpp

input = [1,2,5,3,4,null,6]

output = [1,null,2,null,3,null,4,null,5,null,6]

```

## Approach 2 [recursion]

Time : O(n)
Space : O(h) h-> n in worst case

### explanation

```py
for a root:
    if root is not null:
        flatten left sub tree(recursion)
        flatten right sub tree(recursion)

        find the right most node of flattened left sub tree 
        attach root->right (ptr to right sub tree) to node found in previous step
        swap root->left and root->right
        make root->left as NULL
    return
```
### code
```cpp
class Solution {
public:
    void flatten(TreeNode* root) {
        if(root == NULL) return;
        flatten(root->left);
        flatten(root->right);
        swap(root->left,root->right);
        TreeNode* prev = root;
        TreeNode* curr = root->right;
        while(curr != NULL){
            prev = curr;
            curr = curr->right;
        }
        prev->right = root->left;
        root->left = NULL;
    }
};
``` 

```cpp

input = [1,2,5,3,4,null,6]

output = [1,null,2,null,3,null,4,null,5,null,6]

```


## tags:
$morris-traversal$
$tree$
$recursion$