# [binary-tree-right-side-view](https://leetcode.com/problems/binary-tree-right-side-view/solution/)


## Approach 1

Time : O(n)
Space : O(w), worst case w->n/2, i.e. O(n)

bfs and push right most value 

```cpp
class Solution {
public:
    vector<int> rightSideView(TreeNode* root) {
        vector<int> ans;
        if(root == NULL) return ans;
        queue<TreeNode*> q;
        q.push(root);
        while(!q.empty()){
            TreeNode* top;
            int levelCount = q.size();
            for(int i=0;i<levelCount-1;i++){
                top = q.front();
                if(top->left != NULL) q.push(top->left);
                if(top->right != NULL) q.push(top->right);
                q.pop();
            }
            top = q.front();
            if(top->left != NULL) q.push(top->left);
            if(top->right != NULL) q.push(top->right);
            q.pop();
            ans.push_back(top->val);
        }
        return ans;
    }
};
```

## Approach 2

Time : O(n)
Space : O(h), worst case h -> n i.e. O(n)

reverse pre-order traversal
res.size()<level only when new level is encountered and right most element is pushed .

```cpp
class Solution {
public:
    void recursion(TreeNode *root, int level, vector<int> &res)
    {
        if(root==NULL) return ;
        if(res.size()<level) res.push_back(root->val);
        recursion(root->right, level+1, res);
        recursion(root->left, level+1, res);
    }
    
    vector<int> rightSideView(TreeNode *root) {
        vector<int> res;
        recursion(root, 1, res);
        return res;
    }
};
```

## tags: bfs, queue, preorder, dfs, tree