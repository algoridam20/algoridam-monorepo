### [coin-change](https://leetcode.com/problems/coin-change/)

## Approach 1 [dp]

Time : O(m*n) + ( O(mlogm) for sort optimization)
Space : O(1)

explanation

```
    dp[0] = 0
    dp[i] = min(dp[i],1 + dp[i-coin])
```

```cpp
class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        int n = amount + 1;
        vector<int> dp(n,n);
        dp[0]=0;
        sort(coins.begin(), coins.end());
        for(int i=1;i<n;i++){            
            for(auto coin:coins){
                if(i >= coin)
                    dp[i] = min(dp[i],1 + dp[i-coin]);
                else
                    break;
            }
        }
        
        return (dp[amount] == n) ? -1 : dp[amount];
    }
};
``` 

```cpp
coins = [1,2,5]
amount = 19

dp[] = 0 1 1 2 2 1 2 2 3 3 2 3 3 4 4 3 4 4 5 5 

5
```

## tags:
$sort$
$dp$