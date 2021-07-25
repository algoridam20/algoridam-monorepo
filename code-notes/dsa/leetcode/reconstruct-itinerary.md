### [reconstruct-itinerary](https://leetcode.com/problems/reconstruct-itinerary/)

## Approach 1 [euler-path,back-tracking]

Time : O(ElogE)
Space : O(E+V)

### explanation
```
euler path using dfs-backtracking called **Hierholzer's algorithm**
use each ticket once
```

### implementation 1 [list,sort]


```cpp
class Solution {
public:
    
    void dfs(string u,unordered_map<string,list<string>>& adj,vector<string>& ans){
        
        while(!adj[u].empty()){
            string v = adj[u].front();
            adj[u].pop_front();
            dfs(v,adj,ans);
        }
        ans.push_back(u);
    }
    vector<string> findItinerary(vector<vector<string>>& tickets) {
        unordered_map<string,list<string>> adj;
        vector<string> ans;
        for(auto& ticket: tickets){
            string u = ticket[0];
            string v = ticket[1];
            adj[u].push_back(v);
        }
        for(auto& u:adj){
            u.second.sort();
        }
        dfs("JFK",adj,ans);
        reverse(ans.begin(),ans.end());
        return ans;
    }
};
``` 

```cpp
input = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]

output = ["JFK","ATL","JFK","SFO","ATL","SFO"]
```

### implementation 2 [priority-queue]

### explanation

```cpp
class Solution {
public:
    unordered_map<string,priority_queue<string,vector<string>,greater<string>>> adj;
    vector<string> ans;
    
    void dfs(string u){
        auto& pqu = adj[u];
        while(!pqu.empty()){
            string v = pqu.top();
            pqu.pop();
            dfs(v);
        }
        ans.push_back(u);
    }
    vector<string> findItinerary(vector<vector<string>>& tickets) {
        adj.clear();
        ans.clear();
        for(auto& ticket: tickets){
            string u = ticket[0];
            string v = ticket[1];
            adj[u].push(v);
        }
        dfs("JFK");
        reverse(ans.begin(),ans.end());
        return ans;
    }
};


``` 

```cpp
Input: tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"] but it is larger in lexical order.
```


## tags:
$euler-path$
$dfs$
$graph$
$priority-queue$
$list$
$sort$