### [search-in-rotated-sorted-array](https://leetcode.com/problems/search-in-rotated-sorted-array/)

## Approach 1 [binary-search]

Time : O(logn)
Space : O(1)

explanation
-> use graphs to come up with logic

```cpp
class Solution {
public:
    int search(vector<int>& nums, int x) {
        int start = 0;
        int end = nums.size()-1;
        int midVal,startVal,endVal;
        while(start <= end){
            int mid = start + (end-start)/2;
            midVal = nums[mid];
            startVal = nums[start];
            endVal = nums[end];
            if(midVal == x) return mid;
            if(startVal == x) return start;
            if(endVal == x) return end;
            
            if(midVal > startVal){
                if(x > midVal) start = mid + 1;
                else{
                    if(x > startVal) end = mid - 1;
                    else start = mid + 1;
                }
            }else{
                if( x < midVal) end = mid - 1;
                else{
                    if( x < endVal) start = mid + 1;
                    else end = mid - 1;
                }
            }
            
            
        }
        return -1;
    }
};
``` 

```cpp
in>>
nums = [4,5,6,7,0,1,2] 
x = 0 

out<<
index = 4
```

## Approach 1 [binary-search]

Time : O(logn)
Space : O(1)

2 passes are required
[explanation](https://leetcode.com/problems/search-in-rotated-sorted-array/discuss/14425/Concise-O(log-N)-Binary-search-solution)

```cpp
class Solution {
public:
    int search(int A[], int n, int target) {
        int lo=0,hi=n-1;
        // find the index of the smallest value using binary search.
        // Loop will terminate since mid < hi, and lo or hi will shrink by at least 1.
        // Proof by contradiction that mid < hi: if mid==hi, then lo==hi and loop would have been terminated.
        while(lo<hi){
            int mid=(lo+hi)/2;
            if(A[mid]>A[hi]) lo=mid+1;
            else hi=mid;
        }
        // lo==hi is the index of the smallest value and also the number of places rotated.
        int rot=lo;
        lo=0;hi=n-1;
        // The usual binary search and accounting for rotation.
        while(lo<=hi){
            int mid=(lo+hi)/2;
            int realmid=(mid+rot)%n;
            if(A[realmid]==target)return realmid;
            if(A[realmid]<target)lo=mid+1;
            else hi=mid-1;
        }
        return -1;
    }
};
``` 

## tags:
$binary-search$
