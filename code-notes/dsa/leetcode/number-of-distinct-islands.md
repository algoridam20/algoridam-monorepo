### [number-of-distinct-islands](https://leetcode.com/problems/number-of-distinct-islands)

## Questions
```
You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

An island is considered to be the same as another if and only if one island can be translated (and not rotated or reflected) to equal the other.

Return the number of distinct islands.
```


## Approach 1 [dfs]

Time : O(n*n)
Space : O(n*n)

### explanation

```
save the path of islands traversal as unique way to identify an island
don't forget to save an identifier when back-tracking dfs
```

```cpp
class Solution {
public:
    vector<int> delX = {0,0,1,-1};
    vector<int> delY = {1,-1,0,0};
    unordered_map<int,unordered_map<int,char>> dir;
    int n,m;
    void dfs(int x,int y,vector<vector<int>>& grid,string& str){
        grid[x][y] = 0;
        for(int i=0;i<4;i++){
            int newX = x + delX[i];
            int newY = y + delY[i];
            if(newX >= 0 && newX < n && newY >= 0 && newY < m && grid[newX][newY] != 0){
                str += dir[delX[i]][delY[i]];
                dfs(newX,newY,grid,str);
            }
        }
        str += 'b';
    }
    int numDistinctIslands(vector<vector<int>>& grid) {
        unordered_set<string> islands;
        n = grid.size();
        m = grid[0].size();
        dir[0][1] = 'r';
        dir[0][-1] = 'l';
        dir[-1][0] = 'u';
        dir[1][0] = 'd';
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                if(grid[i][j] != 0){
                    string str = "";
                    dfs(i,j,grid,str);
                    islands.insert(str);
                    cout<<str<<endl;
                }
            }
        }
        return islands.size();
    }
};
``` 

```cpp
Input: grid = [[1,1,0,1,1],[1,0,0,0,0],[0,0,0,0,1],[1,1,0,1,1]]
Output: 3
```

## Approach 2 [bfs]

Time : O(n*n)
Space : O(n*n)

### explanation

```
save the bfs string to uniquely identify an island
to get bfs string for an island
     covert current bfs coordinated to string 
     after shifting them to origin (by subtracting offset)
```

```cpp
class Solution {
public:
    vector<int> delX = {0,0,1,-1};
    vector<int> delY = {1,-1,0,0};
    int n,m;
    string bfs(int x,int y,vector<vector<int>>& grid){
        string res = "";
        queue<pair<int,int>> q;
        grid[x][y] = 0;
        q.push({x,y});
        while(!q.empty()){
            pair<int,int> top = q.front();q.pop();
            for(int i=0;i<4;i++){
                int newX = top.first + delX[i];
                int newY = top.second + delY[i];
                if(newX >= 0 && newY >= 0 && newX < n && newY < m && grid[newX][newY] != 0){
                    grid[newX][newY] = 0;
                    res += to_string(newX - x) + to_string(newY - y);
                    q.push({newX,newY});
                }
            }
        }
        return res;
    }
    int numDistinctIslands(vector<vector<int>>& grid) {
        unordered_set<string> islands;
        n = grid.size();
        m = grid[0].size();
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                if(grid[i][j] != 0){
                    islands.insert(bfs(i,j,grid));
                }
            }
        }
        return islands.size();
    }
};
``` 


## tags:
$grid$
$bfs$
$dfs$
$back-tracking$