### [connecting-cities-with-minimum-cost](https://leetcode.com/problems/connecting-cities-with-minimum-cost/)

## Question
```
There are n cities numbered from 1 to n.

You are given connections, where each connections[i] = [city1, city2, cost] represents the cost to connect city1 and city2 together.  (A connection is bidirectional: connecting city1 and city2 is the same as connecting city2 and city1.)

Return the minimum cost so that for every pair of cities, there exists a path of connections (possibly of length 1) that connects those two cities together.  The cost is the sum of the connection costs used. If the task is impossible, return -1.
```

## Approach 1 [kruskal]

Time : O((V*)*ElogE)
Space : O(E+V)

V* -> 5 at most 5 in all practical cases

### explanation

```
path compression and rank/size optimization in unionfind_set data structures can be used to find cycles
pick edges one by one sorted based on weights
```

```cpp
class Solution {
public:
    static bool comp(vector<int>& left,vector<int>& right){
        return left[2] < right[2];
    }
    int find(int a,vector<int>& parent){
        while(a != parent[a]){
            parent[a] = parent[parent[a]];
            a = parent[a];
        }
        return a;
    }
    void unionIfPossible(int a,int b,vector<int>& parent,vector<int>& size){
        int parent_a = find(a,parent);
        int parent_b = find(b,parent);
        if(size[parent_a] == size[parent_b]){
            parent[parent_b] = parent_a;
            size[parent_a]++;
        }
        else if(size[parent_a] > size[parent_b]){
            parent[parent_b] = parent_a;
        }else{
            parent[parent_a] = parent_b;
        }
    }
    int minimumCost(int n, vector<vector<int>>& connections) {
        int totalCost = 0;
        int totalRoads = 0;
        vector<int> parent(n+1,0);
        vector<int> size(n+1,1);
        for(int i=0;i<=n;i++){
            parent[i] = i;
            size[i] = 1;
        }
            
        sort(connections.begin(),connections.end(),comp);
        for(auto& connection: connections){    
            int u = connection[0];
            int v = connection[1];
            int cost = connection[2];
            
            if(find(u,parent) != find(v,parent)){
                unionIfPossible(u,v,parent,size);
                totalCost += cost;
                totalRoads++;
            }
        }
        return (totalRoads == n-1) ? totalCost : -1;
    }
};
``` 

```cpp
Input: n = 3, connections = [[1,2,5],[1,3,6],[2,3,1]]
Output: 6
Explanation: 
Choosing any 2 edges will connect all cities so we choose the minimum 2.
```



## tags:
$kruskal$
$mst$