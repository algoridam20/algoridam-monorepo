### [delete-and-earn](https://leetcode.com/problems/delete-and-earn/)


## Approach 1 [dp]

Time : O(M) max number in input , if can initialize array in other after finding M
Space : O(M)

### explanation
```
similar to house robber, only some houses are in neighbour here .
```

```cpp
class Solution {
public:
    int MAX = 10004;
    int deleteAndEarn(vector<int>& nums) {
        vector<int> count(MAX,0);
        int maxVal = 0;
        int sumWith = 0;
        int sumWithout = 0;
        for(auto& num:nums) {
            count[num]++;
            if(num > maxVal) maxVal = num;
        }
        for(int i=1;i<=maxVal;i++){
            if(count[i] == 0) continue;
            int prevSumWith = sumWith;
            int prevSumWithout = sumWithout;
            int m = max(prevSumWith,prevSumWithout);
            if(count[i-1] > 0)    
                sumWith = prevSumWithout + count[i]*i;
            else
                sumWith = m + count[i]*i;
            sumWithout = m;
        }
        return max(sumWith,sumWithout);
    }
};
``` 

```cpp
input

snapshots

output
```

## tags:
$dp$