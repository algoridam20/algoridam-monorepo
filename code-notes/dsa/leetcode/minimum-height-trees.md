### [minimum-height-trees](https://leetcode.com/problems/minimum-height-trees/)

## Approach 1 [indegree,topological-sort]

Time : O(n)
Space : O(n)

### explanation

```
remove the nodes with indegree == 1 , and update the indegree of edges for these nodes
the last nodes to have indegree == 1 are the one to be used to create trees with min height
(similar to topological sort)
```

```cpp
class Solution {
public:
    vector<int> findMinHeightTrees(int n, vector<vector<int>>& edges) {
        if(n == 1) return {0};
        vector<int> indegree(n,0);
        vector<int> dist(n,0);
        vector<vector<int>> adj(n,vector<int>());
        queue<int> q;
        for(auto edge:edges){
            int u = edge[0];
            int v = edge[1];
            adj[u].push_back(v);
            adj[v].push_back(u);
            indegree[v]++;
            indegree[u]++;
        }
        vector<int> curr;
        vector<int> prev;
        for(int u=0;u<n;u++){
            if(indegree[u] == 1){
                q.push(u);
                indegree[u]--;
                curr.push_back(u);
            }
        }
        while(!q.empty()){
            int k = q.size();
            prev = curr;
            curr.clear();
            for(int i = 0;i<k;i++){
                int u = q.front();q.pop();
                for(int v:adj[u]){
                    indegree[v]--;
                    if(indegree[v] == 1){
                        curr.push_back(v);
                        q.push(v);
                    }
                }
            }
        }
        
        return  prev ;
    }
};
``` 

```cpp
7
[[0,1],[1,2],[1,3],[2,4],[3,5],[4,6]]
output = [1,2]
```

## tags:
$indegree$
$topological-sort$
$graphs$
$trees$