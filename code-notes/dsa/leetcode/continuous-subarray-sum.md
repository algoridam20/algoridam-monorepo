### [continuous-subarray-sum](https://leetcode.com/problems/continuous-subarray-sum/)

## Questions
```
Given an integer array nums and an integer k, return true if nums has a continuous subarray of size at least two whose elements sum up to a multiple of k, or false otherwise.

An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.

similar to [problme](code-notes/dsa/leetcode/subarray-sum-equals-k.md)
```

## Approach 1 [hash-map,cummulative-sum]

Time : O(n)
Space : O(k)

### explanation
```
math : 
    let s[i] = sumTill[i] = a*k + b;
    let s[j] = sumTill[j] = c*k + d;

sum between i and j = s[i]-s[j]
for that sum to be mutiple of k 
    (a-c)*k + (b-d) = e*k
for that b should be equal to d

if 
    for any i there exist a j such that
        1. i-j > 1
        2. s[i]%k == s[j]%k

for that we can use a simple hashMap 
with <key:value> as <s[i]%k,i> to lookback 
that if same remainder has already occured and at what index;
    
```

```cpp
class Solution {
public:
    bool checkSubarraySum(vector<int>& nums, int k) {
        unordered_map<int,int> hashMap;
        hashMap[0] = -1;
        int sum = 0;
        for(int i=0;i<nums.size();i++){
            sum += nums[i];
            int mod = sum%k;
            if(hashMap.find(mod) != hashMap.end()){
                if(i - hashMap[mod] > 1)return true;
            }else{
                hashMap[mod] = i;
            }
        }
        return false;
    }
};
``` 

```cpp
[0,0]
1

true
```

```cpp
[0]
1

false
```

```cpp
[23,2,4,6,6]
7

true
```

## tags:
$hash-map$
$map$
$cummulative-sum$
$dp$