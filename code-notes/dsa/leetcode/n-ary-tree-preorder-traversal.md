# [n-ary-tree-preorder-traversal](https://leetcode.com/problems/n-ary-tree-preorder-traversal/submissions/)

## Approach 1

Time : O(n)
Space : O(h), worst case h -> n i.e. O(n)

```cpp
/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> children;

    Node() {}

    Node(int _val) {
        val = _val;
    }

    Node(int _val, vector<Node*> _children) {
        val = _val;
        children = _children;
    }
};
*/

class Solution {
public:
    void inOrderTraversal(Node* root,vector<int> &ans){
        if(root == NULL) return;
        int n = root->children.size();
        ans.push_back(root->val);
        for(int i=0;i<n;i++)
            inOrderTraversal(root->children[i],ans);
    }
    vector<int> preorder(Node* root) {
        vector<int> ans;
        inOrderTraversal(root,ans);
        return ans;
    }
};
```

## tags: dfs, tree, preorder, recursion