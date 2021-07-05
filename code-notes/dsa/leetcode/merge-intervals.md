### [merge-intervals](https://leetcode.com/problems/merge-intervals/)

## Approach 1 [greedy]

Time : O(nlogn)
Space : O(n)

### explanation
```
Intuition

If we sort the intervals by their start value, then each set of intervals that can be merged will appear as a contiguous "run" in the sorted list.

or grow the merge-able intervals (union)

```

```cpp
class Solution {
public:
    static bool comp(vector<int>& left,vector<int>& right){
        return left[0] < right[0];
    }
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        int n = intervals.size();    
        vector<vector<int>> ans;
        sort(intervals.begin(),intervals.end(),comp);
        int mergeStart = intervals[0][0];
        int mergeEnd = intervals[0][1];
        for(int i=1;i<n;i++){
            int currStart = intervals[i][0];
            int currEnd = intervals[i][1];
            if(currStart <= mergeEnd){
                mergeEnd = max(currEnd,mergeEnd);
            }else{
                ans.push_back({mergeStart,mergeEnd});
                mergeStart = currStart;
                mergeEnd = currEnd;
            }
        }
        ans.push_back({mergeStart,mergeEnd});
        return ans;
    }
};
``` 

```cpp
input = [[2,15],[36,45],[9,29],[16,23],[4,9]]

output = [[2,29],[36,45]]
```


## tags:
$greedy$
$sort$