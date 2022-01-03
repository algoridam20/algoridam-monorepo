### [jump-game-ii](https://leetcode.com/problems/jump-game-ii/)

## Question
```
Given an array of non-negative integers nums, you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Your goal is to reach the last index in the minimum number of jumps.
You can assume that you can always reach the last index.
```

## Approach 1 [dp,ad-hoc]

Time : O(n)
Space : O(1)

### explanation
```cpp
change this problem to a BFS problem, where nodes in level i are all the nodes that can be reached in i-1th jump.  

[2,3,1,1,4]
(2)(3,1)(1,4)
l1   l2   l3
so two jumps
```

```cpp
class Solution {
public:
    int jump(vector<int>& nums) {
        int n = nums.size();
        int jumps = 0;
        int prevFarthest = 0;
        int currFarthest = 0;
        for(int i=0;i<n;i++){
            if(i > prevFarthest){
                jumps++;
                prevFarthest = currFarthest;
            }
            currFarthest = max(currFarthest,i+nums[i]);
        }
        return jumps;
    }
};
``` 

```cpp
Example 1:
Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:
Input: nums = [2,3,0,1,4]
Output: 2
```

## tags:
$bfs$
$dp$
$ad-hoc$