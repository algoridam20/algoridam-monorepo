### [n-queens](https://leetcode.com/problems/n-queens/)

## Approach 1 [back-tracking]

Time : O(exponential)
Space : O(n)

### explanation
```
We'll create a recursive function backtrack that takes a few arguments to maintain the board state. The first parameter is the row we're going to place a queen on next, and then we will have 3 sets that track which columns, diagonals, and anti-diagonals have already had queens placed on them. Additionally, we will store the actual board so that when we find a valid solution, we can include it in our answer. The function will work as follows:

1. If the current row we are considering is equal to n, then we have a solution. Add the current board state to a list of solutions, and return. We'll make use of a small helper function to get our board into the correct output format.

2. Iterate through the columns of the current row. At each column, we will attempt to place a queen at the square (row, col) - remember we are considering the current row through the function arguments.

    Calculate the diagonal and anti-diagonal that the square belongs to. If a queen has not been placed in the column, diagonal, or anti-diagonal, then we can place a queen in this column, in the current row.

    If we can't place the queen, skip this column (move on and try the next column).

3. If we were able to place a queen, then add the queen to the board and update our 3 sets (cols, diagonals, and antiDiagonals), and call the function again, but with row + 1.

4. The function call made in step 3 explores all valid board states with the queen we placed in step 2. Since we're done exploring that path, backtrack by removing the queen from the square - this includes removing the values we added to our sets on top of removing the "Q" from the board.
```

```cpp
class Solution {
public:
    vector<vector<string>> ANS;
    string rowToString(vector<int>& row,int& n){
        string s(n,'.');
        for(int i=0;i<n;i++){
            if(row[i] == 1)
                s[i] = 'Q';
        }
        return s;
    }
    bool isValid(int x,int y,vector<vector<int>>& board,int& n){
        int k = n-1;
        for(int i=0;i<n;i++){
            if(board[i][y] == 1 || board[x][i] == 1) return false;
        }
        int lx = x - min(x,y);
        int ly = y - min(x,y);
        int rx,ry;
        if(k  < x + y){
            rx = x - (k-y);
            ry = k;
        }else{
            rx = 0;
            ry = x + y;
        }        
        while(lx < n && ly < n){
            if(board[lx][ly] == 1)
                return false;
            lx++;
            ly++;
        }
        while(rx < n && ry >= 0 ){
            if(board[rx][ry] == 1)
                return false;
            rx++;
            ry--;
        }
        return true;
    }
    void solver(int row,vector<vector<int>>& board,int& n){
        for(int i=row;i<n;i++){
            for(int j=0;j<n;j++){
                if(board[i][j] == 0 && isValid(i,j,board,n)){
                    board[i][j] = 1;
                    solver(i + 1,board,n);
                    board[i][j] = 0;
                }
            }
            int sum = 0;
            for(int j=0;j<n;j++){
                sum += board[row][j];
            }
            if(sum != 1) return;
        }
        vector<string> ans;
        for(int i=0;i<n;i++){
            ans.push_back(rowToString(board[i],n));
        }
        ANS.push_back(ans);
    }
    vector<vector<string>> solveNQueens(int n) {
        ANS.clear();
        vector<vector<int>> board(n,vector<int>(n,0));
        solver(0,board,n);
        return ANS;
    }
};
``` 

```cpp
Input: n = 4
Output: [
    [".Q..",
     "...Q",
     "Q...",
     "..Q."],
    
    ["..Q.",
     "Q...",
     "...Q",
     ".Q.."]]
```

## tags:
$back-tracking$
