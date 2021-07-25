### [network-delay-time](https://leetcode.com/problems/network-delay-time/)

## Approach 1 [dijkstra]

Time : O((E+V)logV)
Space : O(E+V)

### explanation

```
dijkstra is a greedy algo that works on graph with non negative weight

pseudo code:
pq -> set containing all the nodes
all the nodes are processed from this set , till this set is empty

for all nodes:
    dist[node] = infinity

dist[source] = 0;

priority of pq (left, right): 
    dist[left] < dist[right]

while( pq is not empty() ):
    u = extract min (min distance from sources)
    for all edges from u:
        relax(distance)
    
relax(u,v,w):
    if(dist[v] > dist[u] + w):
        update dist[v]

```

```cpp
class Solution {
public:
    int INF = 1000006;
    int networkDelayTime(vector<vector<int>>& edges, int n, int s) {
        set<pair<int,int>> pq; // set is used as priority queue
        vector<int> dist(n+1,INF); // storing distance 
        vector<vector<pair<int,int>>> adj(n+1,vector<pair<int,int>>());
        for(int u=1;u<=n;u++){
            pq.insert({INF,u});
        }
        pq.erase({INF,s});
        pq.insert({0,s});

        dist[s] = 0;
        for(auto edge:edges){
            int u = edge[0];
            int v = edge[1];
            int w = edge[2];
            adj[u].push_back({v,w});
        }        
        while(!pq.empty()){
            auto top = (pq.begin());
            int u = top->second;
            pq.erase(top);
            for(int i=0;i<adj[u].size();i++){
                int v = adj[u][i].first;
                int w = adj[u][i].second;
                if(dist[v] > dist[u] + w){
                    pq.erase({dist[v],v});
                    dist[v] = dist[u] + w;
                    pq.insert({dist[v],v});
                }
            }
        }
        int maxDel = INT_MIN;
        for(int i=1;i<=n;i++){
            int del = dist[i];
            maxDel = max(maxDel,del);
        }
        return (maxDel != INF) ? maxDel : -1;
    }
};
``` 

```cpp
[[2,1,1],[2,3,1],[3,4,1]]
4
2

output = 2
```

## Approach 2 [bellman-ford]

Time : O(EV)
Space : O(E+V)

### explanation

```
bellman-ford is algo that works on graph with negative weight

pseudo code:

for all nodes:
    dist[node] = infinity

dist[source] = 0;

for V-1 times:
    for all edges:
        relax(edge) 

for all edges:
    if edge can still be realaxed:
        dist[v] = -infinity



```

```cpp
class Solution {
public:
    int INF = 1000006;
    int networkDelayTime(vector<vector<int>>& edges, int n, int s) {
        vector<int> dist(n+1,INF);
        dist[s] = 0;
        for(int i=0;i<n-1;i++){
            for(auto edge:edges){
                int u = edge[0];
                int v = edge[1];
                int w = edge[2];
                if(dist[v] > dist[u] + w){
                    dist[v] = dist[u] + w;
                }
            }
        }
        
        // for negative cycles , not required for this problem.
        for(auto edge:edges){
            int u = edge[0];
            int v = edge[1];
            int w = edge[2];
            if(dist[v] > dist[u] + w){
                dist[v] = INT_MIN;
            }
        }
        
        
        int maxDel = INT_MIN;
        for(int i=1;i<=n;i++){
            maxDel=max(maxDel,dist[i]);
        }
        return (maxDel != INF) ? maxDel : -1;
    }
};
```

## tags:

$dijkstra$
$bellman-ford$
$single-source-shortest-path$