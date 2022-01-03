### [house-robber-ii](https://leetcode.com/problems/house-robber-ii/)

## Approach 1 [dp]

Time : O(n)
Space : O(1)

### explanation
```
max of houseRobber(0,n-2),houseRobber(1,n-1) to take of circular dependency.
```

```cpp
class Solution {
public:
    int rob1(vector<int>& nums,int start,int end){
        int currR = 0;
        int currNR = 0;
        for(int i=start;i<=end;i++){
            int newR = currNR + nums[i];
            int newNR = max(currR,currNR);
            currR = newR;
            currNR = newNR;
        }
        return max(currR,currNR);
    }
    int rob(vector<int>& nums) {
        int n = nums.size();
        if(n == 1) return nums[0];
        return max(rob1(nums,0,n-2),rob1(nums,1,n-1));
    }
};
``` 

```cpp
Example 1:
Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.

Example 2:
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Example 3:
Input: nums = [1,2,3]
Output: 3
```

## tags:
$dp$