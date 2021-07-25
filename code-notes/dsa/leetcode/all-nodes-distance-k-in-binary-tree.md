### [all-nodes-distance-k-in-binary-tree](https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/)

## Approach 1 [parent-pointer,dfs]

Time : O(n)
Space : O(n)

### explanation

```
save link to parent pointer , and start dfs from given targe node address
till level of dfs == k
```

```cpp
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    unordered_map<TreeNode*,TreeNode*> parent;
    unordered_set<TreeNode*> vis;
    vector<int> ans;
    
    void addParent(TreeNode* root){
        if(root == NULL) return;
        if(root->left != NULL){
            parent[root->left] = root;
        }
        if(root->right != NULL){
            parent[root->right] = root;
        }
        addParent(root->left);
        addParent(root->right);
    }
    
    void dfs(TreeNode* root,int k){
        if(root == NULL || vis.find(root) != vis.end()) 
            return;
        vis.insert(root);
        if(k == 0){
            ans.push_back(root->val);
            return;
        }
        if(root->left != NULL){
            dfs(root->left,k-1);
        }
        if(root->right != NULL){
            dfs(root->right,k-1);
        }
        if(parent.find(root) != parent.end()){
            dfs(parent[root],k-1);
        }
            
        
    }
    vector<int> distanceK(TreeNode* root, TreeNode* target, int k) {
        addParent(root);
        dfs(target,k);
        return ans;
    }
};
``` 

```cpp
[3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2
Output: [7,4,1]
Explanation: The nodes that are a distance 2 from the target node (with value 5) have values 7, 4, and 1.
```

## Approach 2 [parent-pointer,bfs]

Time : O()
Space : O()

### explanation

```cpp
class Solution {
public:
    void addParent(TreeNode* root,unordered_map<TreeNode*,TreeNode*>& parent){
        if(root == NULL) return;
        if(root->left != NULL){
            parent[root->left] = root;
        }
        if(root->right != NULL){
            parent[root->right] = root;
        }
        addParent(root->left,parent);
        addParent(root->right,parent);
    }
    vector<int> distanceK(TreeNode* root, TreeNode* target, int k) {
        if(k == 0) return {target->val};
        vector<int> ans;
        unordered_map<TreeNode*,TreeNode*> parent;
        unordered_set<TreeNode*> vis;
        addParent(root,parent);
        queue<TreeNode*> q;
        q.push(target);
        vis.insert(target);
        
        while(!q.empty()){
            int size = q.size();
            k--;
            for(int i=0;i<size;i++){
                auto top = q.front();q.pop();
                if(top->left != NULL && vis.count(top->left) == 0){
                    q.push(top->left);
                    vis.insert(top->left);
                }
                if(top->right != NULL && vis.count(top->right) == 0){
                    q.push(top->right);   
                    vis.insert(top->right);
                }
                if(parent.find(top) != parent.end() && vis.count(parent[top]) == 0){
                    q.push(parent[top]);
                    vis.insert(parent[top]);
                }
            }
            if(k == 0){
                while(!q.empty()){
                    ans.push_back(q.front()->val);
                    q.pop();
                }
            }
        }
        return ans;
    }
};
``` 



## tags:
$tree$
$graph$
$dfs,bfs$