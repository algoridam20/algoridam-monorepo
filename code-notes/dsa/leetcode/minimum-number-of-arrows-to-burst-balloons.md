### [minimum-number-of-arrows-to-burst-balloons](https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/)

## Approach 1 [greedy]

Time : O(nlogn)
Space : O(n)

### explanation
```
Intuition

If we sort the intervals by their start value, then each set of intervals that can be merged will appear as a contiguous "run" in the sorted list.

or grow the merge-able intervals (intersection)
```

```cpp
class Solution {
public:
    static bool comp(vector<int>& left,vector<int>& right){
        return left[0] < right[0];
        // return (left[0] != right[0]) ? left[0] < right[0] : left[1] - right[1];
    }
    int findMinArrowShots(vector<vector<int>>& points) {
        int ans = 0;
        int n = points.size();
        if(n<1) return 0;
        sort(points.begin(),points.end(),comp);
        int intersectionStart = points[0][0];
        int intersectionEnd = points[0][1];
        for(int i=1;i<n;i++){
            int currStart = points[i][0];
            int currEnd = points[i][1];
            if(currStart <= intersectionEnd){
                intersectionStart = currStart;
                intersectionEnd = min(intersectionEnd,currEnd);
            }else{
                intersectionStart = currStart;
                intersectionEnd = currEnd;
                ans ++;
            }
        }
        return ans + 1;
    }
};
``` 

```cpp
Input: points = [[10,16],[2,8],[1,6],[7,12]]
Output: 2
Explanation: One way is to shoot one arrow for example at x = 6 (bursting the balloons [2,8] and [1,6]) and another arrow at x = 11 (bursting the other two balloons).
```

## tags:
$greedy$
$sort$