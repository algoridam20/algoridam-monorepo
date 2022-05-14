# Disjoinet set with path compression and size (rank) optimization.

## Theory notes

![notes](images/graph-djs.png?raw=true "notes")

## code impl: 

```cpp
class DisjoinedSet {
public:
    vector<int> size;
    vector<int> parent;
    int totalSets;
    DisjoinedSet(int n){
        size = vector<int>(n,1);
        parent = vector<int>(n,1);
        totalSets = n;
        for(int i=0;i<n;i++){
            size[i] = 1;
            parent[i] = i;
        }
    }
    int find(int x){
        if(parent[x] == x){
            return x;
        }
        return parent[x] = find(parent[x]);
    }
    void unionSet(int x,int y){
        int X = find(x);
        int Y = find(y);
        if(X == Y) return;
        if(size[X] > size[Y]){
            parent[Y] = X;
        }else if(size[X] < size[Y]){
            parent[X] = Y;
        }else{
            parent[X] = Y;
            size[Y]++;
        }
        totalSets--;
        return;
    }
    bool inSameSet(int x,int y){
        return find(x) == find(y);
    }
};
```

## tags:
$disjoint-set$
$sets$
$mst$
$graph$