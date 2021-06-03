### [longest-increasing-subsequence](https://leetcode.com/problems/longest-increasing-subsequence/)

## Approach 1 [binary-search,dp]

Time : O(nlogn)
Space : O(n)

dp = potential LIS , dp.size() = max possible length till iterated index
[wiki](https://en.wikipedia.org/wiki/Longest_increasing_subsequence)

```cpp
class Solution {
public:
    // return -1 if num is found else return index of smallest value > num
    int binarySearchCeil(vector<int>& arr,int start,int end,int num){
        while(start <= end){
            int mid = start + (end-start)/2;
            if(arr[mid] == num)
                return -1;
            else if(arr[mid] < num)
                start = mid + 1;
            else
                end = mid - 1;
        }
        return start;    
    }
    
    int lengthOfLIS(vector<int>& nums) {
        int n = nums.size();
        if(n < 2) return n;
        vector<int> dp(1,nums[0]);
        int dp_end_ptr = 0;
        for(int i=1;i<n;i++){
            int num = nums[i];
            if(dp[dp_end_ptr] < num){
                dp.push_back(num);
                dp_end_ptr++;
            }
            else if(dp[0] > num)
                dp[0] = num;
            else{
                int index = binarySearchCeil(dp,0,dp_end_ptr,num);
                if(index != -1)
                    dp[index] = num;
            }
        }
        return dp_end_ptr+1;
    }
};
``` 

```
nums = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]

dp snapshot ()
0 
0 8 
0 4 
0 4 12 
0 2 12 
0 2 10 
0 2 6 
0 2 6 14 
0 1 6 14 
0 1 6 9 
0 1 5 9 
0 1 5 9 13 
0 1 3 9 13 
0 1 3 9 11 
0 1 3 7 11 
0 1 3 7 11 15 
```

## Approach 2 [dp]

Time : O(n*n)
Space : O(n)

```cpp
class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        int ans = 0;
        int n = nums.size();
        vector<int> dp(n,1);
        for(int i=0;i<n;i++){
            int maxLength = 0;
            int currEnd = nums[i];
            for(int j=i-1;j>=0;j--){
                if(nums[j] < currEnd){
                    maxLength = max(maxLength,dp[j]);
                }
            }
            dp[i] = 1 + maxLength;
            ans = max(ans,1 + maxLength);
        }
        return ans;
    }
};
```

## tags:
$dp$
$binary-search$