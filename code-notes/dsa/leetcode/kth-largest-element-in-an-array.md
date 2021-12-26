### [kth-largest-element-in-an-array](sl)

## Approach 1 [min-heap]

### implementation 1 [priority_queue]
Time : O(nlogk)
Space : O(k)

We can maintain the largest k elements in a heap with the smallest among them at the top

```cpp
class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        priority_queue<int, vector<int>, greater<int>> minHeap;
        for (int num : nums) {
            minHeap.push(num);
            if (minHeap.size() > k) {
                minHeap.pop();
            }
        }
        return minHeap.top();
    }
};
``` 

### implementation 2 [multi-set] 

### caution while deleting , use set.erase(iterator) instead of set.earse(value)

```cpp
class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        multiset<int> minHeap;
        for(auto num:nums){
            minHeap.insert(num); 
            if(minHeap.size() > k)
                minHeap.erase(minHeap.begin());
                //minHeap.erase(*(minHeap.begin())) is incorrect 
                //as it will delete all occurance of smallest value.
        }
        return *(minHeap.begin());
    }
};
```

```cpp
nums = [3,2,3,1,2,4,5,5,6]
k = 4

minHeap Snapshots
3 
2 3 
2 3 3 
1 2 3 3 
2 2 3 3 
2 3 3 4 
3 3 4 5 
3 4 5 5 
4 5 5 6 

Output
4
```

## Approach 2 [quick-sort-partition,divide-and-conqure]

Time : O(n*n) worst case , O(n) amortized if using random pivot every time.
Space : O(1)

```cpp
like binary search reduce the smaple space as we go.

1. using quick sort partiton like algo , partition all the elements >= to nums[right] and return pivot index.
2. if partiton index is grater than k-1 reduce the smaple space by moving the right pointer to pivot - 1;
else move left pointer to pivot + 1.
3. repeat untill pivot == k - 1. 

return nums[k-1];
```

```cpp
class Solution {
public:
    
    int quickSortPartition(vector<int>& nums,int left,int right){
        if(left >= right) return left;
        int newRight = rand()%(right-left+1) + left;
        swap(nums[right],nums[newRight]);
        
        int slow = left;
        for(int fast=left;fast<right;fast++){
            if(nums[fast] >= nums[right]){
                swap(nums[slow],nums[fast]);
                slow++;
            }
        }
        
        swap(nums[slow],nums[right]);
        return slow;
    }
    
    
    int findKthLargest(vector<int>& nums, int k) {
        int left = 0;
        int right = nums.size()-1;
        while(true){
            int pivot = quickSortPartition(nums,left,right);
            if(pivot == k-1)
                return nums[pivot];
            else if(pivot > k-1)
                right = pivot - 1;
            else
                left = pivot + 1;
        }
        return -1;
    }
};
```

## tags:
$min-heap$
$heap$
$multi-set$
$quick-sort$