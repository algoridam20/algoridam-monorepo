### [longest-consecutive-sequence](https://leetcode.com/problems/longest-consecutive-sequence/)

## Approach 1 [set]

Time : O(n)
Space : O(n)

explanation: 

insert everything into unordered_set
to find the longest consecutive sequence efficiently , make sure you find the consecutive such that no number is iterated more than twice.

it is good idea to go through the sequences from top of the sequence, to avoid repeated access of middle elements .

and, a element is at the top or highest value in the sequence if ,the unordered_set does not contain value + 1.
but contain value - 1;

```cpp
class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        if(nums.size() < 1) return 0;
        int ans = 1;
        unordered_set val(nums.begin(),nums.end());
        for( auto num: val){
            // if num has no parent (num + 1) but only children (num + 1)
            if(val.find(num + 1) == val.end() && val.find(num - 1) != val.end()){
                int currLen = 1;
                int i = num-1;
                while(val.find(i) != val.end()){
                    i--;
                    currLen++;
                }
                ans = max(ans,currLen);
            }
        }
        return ans;
    }
};
``` 

```cpp
nums = [0,3,7,2,5,8,4,6,0,1]
unordered_set<int> val = [0,3,7,2,5,8,4,6,0,1]

output = 9
```
## tags:
$set$
$unordered-set$