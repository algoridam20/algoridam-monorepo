### [container-with-most-water](https://leetcode.com/problems/container-with-most-water/)

## Approach 1 [two-pointers]

Time : O(n)
Space : O(1)

explanation:

S = (j-i)*min(a[i]*a[j]);
* we need to find i and j for which S is max
* when j > i and a[i] > a[j]
  * we don't need to check all values between i and j :
  * as a[j]*(i-j-k) will always be less than (j-i)*min(a[i]*a[j]) for any positive value k between i and j
  * so all we have to do is move the pointer at j as only then there is hope of finding a bigger S

[proof of correctness](https://leetcode.com/problems/container-with-most-water/discuss/200246/Proof-by-formula) 

```cpp
class Solution {
public:
    int maxArea(vector<int>& height) {
        int ans = INT_MIN;
        int left = 0;
        int right = height.size() - 1;
        while(left < right){
            ans = max(ans,(right-left)*min(height[left],height[right]));
            if(height[left] <= height[right])
                left++;
            else
                right--;
        }
        return ans;
    }
};
``` 

```cpp
input = [4,3,2,1,4]

output = 16
```

## tags:
$two-pointer$
