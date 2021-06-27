### [find-first-and-last-position-of-element-in-sorted-array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/)

## Approach 1 [binary-search]

Time : O(nlogn)
Space : O(1)


```cpp
class Solution {
public:
    int findFirstOccurance(vector<int>& arr,int start,int end,int x){
        while(start<=end){
            int mid = start + (end-start)/2;
            if(arr[mid] == x && (mid == start || (mid-1 >= start && arr[mid-1] < x)))
                return mid;
            else if(arr[mid] >= x)
                end = mid - 1;
            else
                start = mid + 1;       
        }
        return -1;
    }
    int findLastOccurance(vector<int>& arr,int start,int end,int x){
        while(start <= end){
            int mid = start + (end-start)/2;
            if(arr[mid] == x && (mid == end || (mid+1 <= end && arr[mid+1] > x)))
                return mid;
            else if(arr[mid] <= x)
                start = mid + 1;
            else
                end = mid - 1;
        }
        return -1;
    }
    vector<int> searchRange(vector<int>& arr, int target) {
        vector<int> ans(2,-1);
        ans[0] = findFirstOccurance(arr,0,arr.size()-1,target);
        ans[1] = findLastOccurance(arr,0,arr.size()-1,target);
        return ans;
    }
};
``` 

```cpp
nums = [5,7,7,8,8,10], target = 8

output = [3,4]
```


## tags:
$binary-search$
