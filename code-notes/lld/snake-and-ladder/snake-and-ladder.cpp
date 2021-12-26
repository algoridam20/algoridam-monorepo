#include <iostream>
#include <stdio.h>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <unordered_map>
#include <unordered_set>
#include <ctime>
#include <algorithm>
#include <iterator>
#include <utility>
#include <queue>
#include <list>

using namespace std;

class Player
{
public:
    int id;
    string name;
    vector<int> moves;
    bool isWinner;
    Player(int id, string name)
    {
        this->id = id;
        this->name = name;
        this->isWinner = false;
        this->moves = vector<int>(1, 0);
    }
    void printAllMoves(){
        for(auto move:this->moves){
            cout<<move<<"->";
        }cout<<"won!"<<endl;
    }
};

class SnakeGame
{
public:
    vector<int> board;
    vector<vector<int> > ladders;
    vector<Player *> allPlayers;
    int currentPlayerId;
    int totalNumberOfPlayers;

    

    SnakeGame(vector<vector<int> > &snakes, vector<vector<int> > &ladders, vector<string> &players)
    {
        this->board = vector<int>(101, 0);
        for (int i = 0; i < ladders.size(); i++)
        {
            int head = ladders[i][0];
            int tail = ladders[i][1];
            int value = head - tail;
            board[tail] = value;
        }
        for (int i = 0; i < snakes.size(); i++)
        {
            int head = snakes[i][0];
            int tail = snakes[i][1];
            int value = head - tail;
            board[head] = -1 * value;
        }
        totalNumberOfPlayers = players.size();
        for (int i = 0; i < totalNumberOfPlayers; i++)
        {
            Player *p = new Player(i, players[i]);
            allPlayers.push_back(p);
        }
        currentPlayerId = -1;
    }
    int nextPlayer()
    {
        currentPlayerId++;
        return currentPlayerId % totalNumberOfPlayers;
    }
    int makeMove(int playerId)
    {
        Player *currPlayer = allPlayers[playerId];
        int currentPositon = currPlayer->moves.back();
        int diceRoll = getDiceRoll();
        int newPosition = currentPositon + diceRoll;
        if (newPosition > 100)
        {
            // we stay at same postion if dice roll exceed 100th block
            newPosition = currentPositon;
        }
        else
        {

            // 100 99 98 .... 7 6 5 4 3 2 1 0
            // [7] =  - 3
            // [4] =  - 3
            // [1] = +99

            // we move untill we are not on eiter snake or ladder;
            while (board[newPosition] != 0)
                newPosition += board[newPosition];
        }
        currPlayer->moves.push_back(newPosition);
        return newPosition;
    }
    int getDiceRoll()
    {
        srand(time(NULL)+rand());
        int val = rand() % 6 + 1;
        cout<< val << endl;
        return val;
    }
    bool isCycel(vector<int> &board, vector<int> skip, bool isSnake)
    {
        unordered_set<int> indexSet;
        int head = skip[0];
        int tail = skip[1];
        int value = head - tail;
        if (isSnake)
        {
            int start = head;
            int temp = board[head];
            board[head] = -1 * value;
            while (indexSet.count(start) == 0 && board[start] != 0)
            {
                start += board[start];
            }
            if (indexSet.count(start) > 0)
            {
                board[head] = temp;
                return true;
            }
        }
        // similarly for ladder
        return false;
    }
};

bool valid(vector<int> &snake)
{
    return true;
}
// game runner class in main
int main(void)
{
    int totalSnakes, totalLadders, totalPlayers;
    cin >> totalSnakes;
    vector<vector<int> > snakes;
    for (int i = 0; i < totalSnakes; i++)
    {
        int head, tail;
        cin >> head >> tail;
        vector<int> snake;
        snake.push_back(head);
        snake.push_back(tail);
        snakes.push_back(snake);
    }
    cin >> totalLadders;
    vector<vector<int> > ladders;
    for(int i=0;i<totalLadders;i++)
    {
        int head, tail;
        cin >> head >> tail;
        vector<int> ladder;
        ladder.push_back(head);
        ladder.push_back(tail);
        ladders.push_back(ladder);
    }
    cin >> totalPlayers;
    vector<string> players;
    if (totalPlayers > 10)
    {
        cout << "Total Players cannot exceed 10" << endl;
        return 0;
    }
    for(int i=0;i<totalPlayers;i++){
        string player;
        cin >> player;
        players.push_back(player);
    }
    SnakeGame* currentGame = new SnakeGame(snakes,ladders,players);
    while(true){
        int playerId = currentGame->nextPlayer();
        Player *currPlayer = currentGame->allPlayers[playerId];
        cout << "Player " << currPlayer->name << " roll the dice by pressing a number"<<endl;
        int k = 0;
        cin >> k;
        int newPosition = currentGame->makeMove(playerId);
        if(newPosition == 100){
            cout << "Game won by " << currPlayer->name << endl;
            currPlayer->printAllMoves();
            return 0;
        }
        else
            cout << currPlayer->name << "Your new position is :" << newPosition << endl;
    }
    return 0;
}

// test case
// 5
// 98 23
// 67 4
// 32 14
// 99 2
// 87 32
// 3
// 78 23
// 55 33
// 97 47
// 2
// ridam
// tinku