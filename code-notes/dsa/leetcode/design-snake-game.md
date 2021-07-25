### [design-snake-game](https://leetcode.com/problems/design-snake-game/)

## Question: 
```
Design a Snake game that is played on a device with screen size height x width. Play the game online if you are not familiar with the game.

The snake is initially positioned at the top left corner (0, 0) with a length of 1 unit.

You are given an array food where food[i] = (ri, ci) is the row and column position of a piece of food that the snake can eat. When a snake eats a piece of food, its length and the game's score both increase by 1.

Each piece of food appears one by one on the screen, meaning the second piece of food will not appear until the snake eats the first piece of food.

When a piece of food appears on the screen, it is guaranteed that it will not appear on a block occupied by the snake.

The game is over if the snake goes out of bounds (hits a wall) or if its head occupies a space that its body occupies after moving (i.e. a snake of length 4 cannot run into itself).

Implement the SnakeGame class:

    * SnakeGame(int width, int height, int[][] food) Initializes the object with a screen of size height x width and the positions of the food.
    
    * int move(String direction) Returns the score of the game after applying one direction move by the snake. If the game is over, return -1.
```


## Approach 1 [list,hash-set]

for each operation
Time : O(1) 
Total Additional Space : O(s)
s = max size of snake

### explanation

```
use as hash-set to check if newHead is part of snakeBody

newHead is valid if its in boundary and (newHead is **not** snakeBody or **newHead is on oldTail**)

if newHead is invalid :
    GAME_OVER

if on food: 
    increase score
    and get next food
else: 
    pop_back snake tail and delete its coordinates from snakeBody

add newHead to snakeBody set
add newHead to front of snake (list)

```

```cpp
class SnakeGame {
public:
    /** Initialize your data structure here.
        @param width - screen width
        @param height - screen height 
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0]. */
    struct pair_hash {
        inline std::size_t operator()(const std::pair<int,int> & v) const {
            return v.first*31+v.second;
        }
    };
    
    
    
    list<pair<int,int>> snake;
    unordered_set<pair<int,int>,pair_hash> snakeBody;
    vector<vector<int>> food;
    unordered_map<char,pair<int,int>> dir;
    pair<int,int> currFood;
    int currFoodIndex;
    int foodSize;
    int n,m;
    int score;
    pair<int,int> getNextFood(){
        if(currFoodIndex < foodSize){
            int i = currFoodIndex;
            currFoodIndex++;
            return {food[i][0],food[i][1]};
        }
        return {-1,-1};
    }
    
    bool isValid(pair<int,int> newHead,pair<int,int> oldTail){
        int x = newHead.first;
        int y = newHead.second;
        if(x >=0 && y>=0 && x < n && y < m && (snakeBody.count({x,y})==0 || newHead == oldTail))
            return true;
        return false;
    }
    SnakeGame(int width, int height, vector<vector<int>>& food_in) {
        
        dir['U'] = {-1,0};
        dir['D'] = {1,0};
        dir['L'] = {0,-1};
        dir['R'] = {0,1};
        
        n = height;
        m = width;
        score = 0;
        currFoodIndex = 0;
        food = food_in;
        foodSize = food.size();
        
        snake.push_front({0,0});
        snakeBody.insert({0,0});
        
        currFood = getNextFood();
    }
    int move(string direction) {
        auto oldHead = snake.front();
        int newX = oldHead.first + dir[direction[0]].first;
        int newY = oldHead.second + dir[direction[0]].second;
        pair<int,int> newHead = {newX,newY};
        pair<int,int> oldTail = snake.back();
        if(isValid(newHead,oldTail)){
            if(newHead == currFood){
                score++;
                currFood = getNextFood();
            }
            else{
                snake.pop_back();
                snakeBody.erase(oldTail);
            }
            snakeBody.insert(newHead);
            snake.push_front(newHead);
            return score;
        }
        return -1;
    }
};

/**
 * Your SnakeGame object will be instantiated and called as such:
 * SnakeGame* obj = new SnakeGame(width, height, food);
 * int param_1 = obj->move(direction);
 */

## tags:
$hash-set$
$list$