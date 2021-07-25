### [course-schedule-ii](https://leetcode.com/problems/course-schedule-ii/)

## Approach 1 [dfs,topological-sort]

Time : O(E+V)
Space : O(E+V)

### explanation

``` 
2 step dfs with
0 -> unvisited
1 -> visiting
2 -> visited

if while visiting node u , node u is found then graph is not a DAG
```


```cpp
class Solution {
public:
    bool topologicalSort(int u,vector<vector<int>>& adj,vector<int>& colour,vector<int>& ans){
        if(colour[u] == 1) return false;
        colour[u] = 1;
        for(auto& v:adj[u]){
            if(colour[v] != 2){
                if(!topologicalSort(v,adj,colour,ans))
                    return false;
            }
        }
        colour[u] = 2;
        ans.push_back(u);
        return true;
    }
    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
        vector<int> ans;
        vector<vector<int>> adj(numCourses,vector<int>());
        vector<int> colour(numCourses,0);
        for(auto& edge: prerequisites){
            int u = edge[0];
            int v = edge[1];
            adj[u].push_back(v);
        }
        for(int u=0;u<adj.size();u++){
            if(colour[u] == 0 && !topologicalSort(u,adj,colour,ans)){
                return {};
            }
        }
        return ans;
    }
};
``` 

```cpp
Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].
```

## Approach 2 [indegree,topological-sort]

Time : O(E+V)
Space : O(E+V)

### explanation

```
1. Initialize a queue, Q to keep a track of all the nodes in the graph with 0 in-degree.
2. Iterate over all the edges in the input and create an adjacency list and also a map of node v/s in-degree.
3. Add all the nodes with 0 in-degree to Q.
4. The following steps are to be done until the Q becomes empty.
    1. Pop a node from the Q. Let's call this node, N.
    2. For all the neighbors of this node, N, reduce their in-degree by 1. If any of the nodes' in-degree reaches 0, add it to the Q.
    3. Add the node N to the list maintaining topologically sorted order.
    4. Continue from step 4.1.

```

```cpp
class Solution {
public:
    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
        vector<int> ans(numCourses,0);
        vector<int> indegree(numCourses,0);
        vector<vector<int>> adj(numCourses,vector<int>());
        queue<int> q;
        
        for(auto& edge: prerequisites){
            int v = edge[0];
            int u = edge[1];
            adj[u].push_back(v);
            indegree[v]++;
        }
        for(int u=0;u<numCourses;u++){
            if(indegree[u] == 0)
                q.push(u);
        }
        int i = 0;
        while(!q.empty()){
            int u = q.front();
            ans[i++] = u;
            for(int i=0;i<adj[u].size();i++){
                int v = adj[u][i];
                indegree[v]--;
                if(indegree[v] == 0)
                    q.push(v);
            }
            q.pop();
        }
        if(i == numCourses)
            return ans;
        return {};
    }
};
``` 

```cpp
Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].
```


## tags:
$graph$
$dag$
$indegree$
$topological-sort$