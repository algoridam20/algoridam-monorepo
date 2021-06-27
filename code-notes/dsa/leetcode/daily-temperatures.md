### [daily-temperatures](https://leetcode.com/problems/daily-temperatures/)

## Approach 1 [stack]

Time : O(n)
Space : O(n)

explanation
iterate from back
and make sure stack top is lower than all elements below


```cpp
class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& nums) {
        int n = nums.size();
        vector<int> ans(n,0);
        vector<int> indexOf(101,-1);
        stack<int> st;
        for(int i=n-1;i>=0;i--){
            while(!st.empty() && st.top() <= nums[i])
                st.pop();
            if(!st.empty())
                ans[i] = indexOf[st.top()]-i;    
            st.push(nums[i]);
            indexOf[nums[i]] = i;
        }
        return ans;
    }
};
``` 

```cpp
input = [73,74,75,71,69,72,76,73]

output = [1,1,4,2,1,1,0,0]
```

## Approach 2 [stack]

explanation
```
use index stack
```

```cpp
class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& nums) {
        int n = nums.size();
        vector<int> ans(n,0);
        // inverted index stack
        stack<int> st;
        for(int i=n-1;i>=0;i--){
            while(!st.empty() && nums[st.top()] <= nums[i])
                st.pop();
            if(!st.empty())
                ans[i] = st.top()-i;    
            st.push(i);
        }
        return ans;
    }
};
``` 


## tags:
$stack$
