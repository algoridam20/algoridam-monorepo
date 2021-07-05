### [longest-arithmetic-subsequence](https://leetcode.com/problems/longest-arithmetic-subsequence/)

## Approach 1 [dp]

Time : O(n*n)
Space : O(n*n)

### explanation
```
The main idea is to maintain a map of differences seen at each index.

We iteratively build the map for a new index i, by considering all elements to the left one-by-one.
For each pair of indices (i,j) and difference d = A[i]-A[j] considered, we check if there was an existing chain at the index j with difference d already.

    If yes, we can then extend the existing chain length by 1.
    
    Else, if not, then we can start a new chain of length 2 with this new difference d and (A[j], A[i]) as its elements.

At the end, we can then return the maximum chain length that we have seen so far.
```

```cpp
class Solution {
public:
    int numMax = 500;
    int longestArithSeqLength(vector<int>& nums) {
        int ans = 0;
        int n = nums.size();
        vector<vector<int>> dp(n,vector<int>(1001,0));
        for(int i=1;i<n;i++){
            for(int j=i-1;j>=0;j--){
                int delta = (nums[i] - nums[j]) + numMax;
                dp[i][delta] = max(dp[j][delta] + 1,dp[i][delta]);
                ans = max(dp[i][delta],ans);
            }
        }
        return ans+1;
    }
};
``` 

```cpp
Input: nums = [20,1,15,3,10,5,8]
Output: 4
Explanation: 
The longest arithmetic subsequence is [20,15,10,5].
```


## tags:
$dp$