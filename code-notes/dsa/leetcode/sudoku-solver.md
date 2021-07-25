### [sudoku-solver](https://leetcode.com/problems/sudoku-solver/)

## Approach 1 [back-tracking]

Time : O(9 ^ m (m represents the number of blanks to be filled in))
Space : O(n)

### explanation
```
Algorithm

Now everything is ready to write down the backtrack function backtrack(row = 0, col = 0).

    Start from the upper left cell row = 0, col = 0. Proceed till the first free cell.

    Iterate over the numbers from 1 to 9 and try to put each number d in the (row, col) cell.

        If number d is not yet in the current row, column and box :

            Place the d in a (row, col) cell.
            Write down that d is now present in the current row, column and box.
            If we're on the last cell row == 8, col == 8 :
                That means that we've solved the sudoku.
            Else
                Proceed to place further numbers.
            Backtrack if the solution is not yet here : remove the last number from the (row, col) cell.
```
or simply :

back track for each empty cell
for (val : range[1:9])
    if val is valid insert and recursive call the function
    if function return true , return true
    else make it blank again


```cpp
public:
    bool isValidElement(int row,int col,char val,vector<vector<char>>& board){
        
        for(int i=0;i<9;i++){
            if(i != col && board[row][i]  == val)
                return false;
            if(i != row && board[i][col]  == val)
                return false;
        }
        
        int startRow = (row/3)*3;
        int startCol = (col/3)*3;
        
        for(int i=startRow;i<startRow+3;i++){
            for(int j=startCol;j<startCol+3;j++)
                if((i!= row && j!= col) && board[i][j] == val){
                    return false;
                }                    
        }
        
        return true;
    }
    bool solver(vector<vector<char>>& board){
        for(int i=0;i<9;i++){
            for(int j=0;j<9;j++){
                
                
                if(board[i][j] == '.'){
                    for(char k='1';k<='9';k++){
                        if(isValidElement(i,j,k,board)){
                            board[i][j] = k;
                            if(solver(board))
                                return true;
                            else
                                board[i][j] = '.';
                        }
                    }
                    return false;
                }
                
                
            }
        }
        return true;
    }
    void solveSudoku(vector<vector<char>>& board) {
        bool solved = solver(board);
        return;
    }
};
``` 

```cpp
Input: board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]]

Output: [
    ["5","3","4","6","7","8","9","1","2"],
    ["6","7","2","1","9","5","3","4","8"],
    ["1","9","8","3","4","2","5","6","7"],
    ["8","5","9","7","6","1","4","2","3"],
    ["4","2","6","8","5","3","7","9","1"],
    ["7","1","3","9","2","4","8","5","6"],
    ["9","6","1","5","3","7","2","8","4"],
    ["2","8","7","4","1","9","6","3","5"],
    ["3","4","5","2","8","6","1","7","9"]]
```


## tags:
$back-tracking$