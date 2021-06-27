### [trapping-rain-water](https://leetcode.com/problems/trapping-rain-water/)

## Approach 1 [stack]

Time : O(n) each element is touched only twice
Space : O(n) 

### explanation

[fill water level by level using stack ](https://leetcode.com/problems/trapping-rain-water/solution/)

```cpp
class Solution {
public:
    int trap(vector<int>& height) {
      int n = height.size();
      int ans = 0;
      //indexStack
      stack<int> st;
      
      for(int i=0;i<n;i++){  
        while(!st.empty() && height[st.top()] <= height[i]){
          int top = st.top();
          st.pop();
          if(st.empty()) break;
          int newTop = st.top();
          int delta = min(height[newTop] , height[i]) - height[top];
          ans += delta * (i-newTop-1);
        }
        st.push(i);
      }
      return ans;
    }
};
``` 

```cpp
input = [0,1,0,2,1,0,1,3,2,1,2,1]

stack : 1 0  delta : 1 distance : 1
stack : 2 1 0  delta : 1 distance : 1
stack : 2 1 delta : 0 distance : 2
stack : 2 1  delta : 1 distance : 3
stack : 3 2 1  delta : 1 distance : 1
stack : 3 2  delta : 0 distance : 2


output = 6
```

## Approach 2 [two-pointer]

Time : O(n)
Space : O(1)

### explanation
```
code is psudo-code
```

```cpp
class Solution {
public:
    int trap(vector<int>& height) {
      int left = 0, right = height.size() - 1;
      int ans = 0;
      int left_max = 0, right_max = 0;
      while (left < right) {
        if (height[left] < height[right]) {
          (height[left] >= left_max)
            ? (left_max = height[left]) 
            : ans += (left_max - height[left]);
          left++;
        }
        else {
          height[right] >= right_max
            ? (right_max = height[right]) 
            : ans += (right_max - height[right]);
          right--;
        }
      }
      return ans;
    }
};
``` 


## tags:
$stack$
$two-pointer$