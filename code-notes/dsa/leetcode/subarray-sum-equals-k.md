### [subarray-sum-equals-k](https://leetcode.com/problems/subarray-sum-equals-k/)

## Approach 1 [hash-map]

Time : O(n)
Space : O(n)

### explanation
```
if for a given i there exist a j< i such that
sumTill(i) - K = sumTill(j)
then sum between i and j = k;
```

```cpp
class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        int ans = 0,sum = 0;
        unordered_map<int,int> cumSum;
        cumSum[0] = 1;
        for(auto num:nums){
            sum += num;
            if(cumSum.find(sum-k) != cumSum.end())
                ans += cumSum[sum-k];
            cumSum[sum]++;
        }        
        return ans;
    }
};
``` 

```cpp
nums = [1,1,1], k = 2

output: 2
```

## tags:
$hash-map$
$cumulative-sum$