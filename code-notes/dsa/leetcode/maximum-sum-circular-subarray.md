### [maximum-sum-circular-subarray](https://leetcode.com/problems/maximum-sum-circular-subarray/)

## Approach 1 [kadanes]

```
Given a circular integer array nums of length n, return the maximum possible sum of a non-empty subarray of nums.
```

Time : O(n)
Space : O(1)

### explanation
```
use kadanes algo to find max sub array,let it's sum be maxSum
use kadanes algo to find min sub array,let it's sum be minSum

if minSum != total then 
    max(maxSum,(total-minSum)) 
    as sum could be in normal part(maxSum) or circular part(total-minSum)
else
    maxSum
```

```cpp
class Solution {
public:
    
    int maxSubarraySumCircular(vector<int>& nums) {
        ios_base::sync_with_stdio(false);
        cin.tie(NULL);
    
        int maxSum = INT_MIN;
        int minSum = INT_MAX;
        int currSum1 = 0;
        int currSum2 = 0;
        int total = 0;
        for(auto& num:nums){
            
            currSum1 += num;
            if(currSum1 > maxSum) maxSum = currSum1;
            if(currSum1 < 0) currSum1 = 0;
            
            currSum2 += num;
            if(currSum2 < minSum) minSum = currSum2;
            if(currSum2 > 0) currSum2 = 0;
            
            total += num;
        }
        
        return (total == minSum)
            ? maxSum
            : max(maxSum,(total-minSum));
    }
};
``` 

```cpp
Example 1:
Input: nums = [1,-2,3,-2]
Output: 3
Explanation: Subarray [3] has maximum sum 3.

Example 2:
Input: nums = [5,-3,5]
Output: 10
Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10.

Example 3:
Input: nums = [-3,-2,-3]
Output: -2
Explanation: Subarray [-2] has maximum sum -2.
```

## tags:
$kadanes$