### [count-complete-tree-nodes](https://leetcode.com/problems/count-complete-tree-nodes/)

## Approach 1 [divide and conquer]

Time : O(log n * log n)
Space : O(h) h -> n

### explanation
```
    1.return 0 if null
    2.calculate left height
    3.calculate right height
    4.if left most height and right most hight are equal 
        return 2^h-1;
    5.else
        return 1 + recursion(LST) + recursion(RST) 
```

```cpp
class Solution {
public:
    
    int countNodes(TreeNode* root) {
        if(root == NULL) return 0;
        int leftH=0;
        int rightH=0;
        TreeNode* left = root;
        TreeNode* right = root;
        while(left != NULL) {
            leftH++;
            left = left->left;
        }
        while(right != NULL) {
            rightH++;
            right = right->right;
        }
        if(leftH == rightH) return (1 << leftH) - 1;
        return 1 + countNodes(root->left) + countNodes(root->right);
    }
};
``` 

```cpp
tree = [1,2,3,4,5,6]
output = 6
```

## Approach 2 [binary-search]

Time : O(log n * log n)
Space : O(h) h -> n

### explanation
```
assume last level as an array
[1,1,1,1,1,0,0,0,0]
where 
    1 => not null 
    0 => null

objective is to find the position of last non null value in this array , that can be easily be done using binary search. 

Given tree is complete binary tree,
in binary search to access mid and mid + 1 
mid = right most element of LST
mid+1 = left most element of RST

or 

binary representation of index to be read, can be exploited to traverse the tree.

```

### implementation 1
```cpp
class Solution {
public:
    int getH(TreeNode* root){
        int i=0;
        while(root != NULL){
            i++;
            root = root->left;
        }
        return i-1;
    }
    TreeNode* find(TreeNode* root,int num, int h){
        
        int power = 1 << (h-1);
        while(power){
            // power & num == 0 will be incorrect due to operator precedence
            if((power & num) == 0)
                root = root->left;
            else
                root = root->right;
            power /= 2;
        }
        return root;
    }
    int getX(TreeNode* root,int h, int start, int end){
        int veryEnd = end;
        while(start < end){
            int mid = start + (end - start)/2;
            TreeNode* midVal = find(root,mid,h);
            TreeNode* midPlus1Val = find(root,mid+1,h);
            if(midVal != NULL){
                if(mid >= veryEnd || midPlus1Val == NULL)
                    return mid;
                else
                    start = mid + 1;
            }else {
                end = mid - 1;
            }
        }
        return end;
    }
    int countNodes(TreeNode* root) {
        int h = getH(root);
        if(h <= 0) return h+1;
        int y = 1 << h;
        int x = getX(root,h,0,y-1);
        return y + x;
    }
};
``` 

### implementation 2

```cpp
class Solution {
public:
    int getH(TreeNode* root){
        int i=0;
        while(root != NULL){
            i++;
            root = root->left;
        }
        return i-1;
    }
    TreeNode* findMid(TreeNode* root,int h){
        h--;
        root = root->left;
        for(int i=0;i<h;i++){
            root = root->right;
        }
        return root;
    }
    TreeNode* findMidPlusOne(TreeNode* root,int h){
        h--;
        root = root->right;
        for(int i=0;i<h;i++){
            root = root->left;
        }
        return root;
    }
    int getX(TreeNode* root,int h, int start, int end){
        while(start < end){
            int mid = start + ((end - start)/2);
            TreeNode* midNode = findMid(root,h);
            TreeNode* midPlusOneNode = findMidPlusOne(root,h);
            if(midNode != NULL){
                if(midPlusOneNode == NULL)
                    return mid;
                else {
                    start = mid+1;
                    root = root->right;
                }
            } else {
                end = mid-1;
                root = root->left;
            }
            h--;
        }
        return end;
    }
    int countNodes(TreeNode* root) {
        int h = getH(root);
        if(h <= 0) return h+1;
        int y = 1 << h;
        int x = getX(root,h,0,y-1);
        return y + x ;
    }
};
```


```cpp
tree = [1,2,3,4,5,6]
output = 6
```

## tags:
$divide and conquer$
$binary-search$
$tree$