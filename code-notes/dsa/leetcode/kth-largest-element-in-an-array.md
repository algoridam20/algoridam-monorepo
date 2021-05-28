### [kth-largest-element-in-an-array](https://leetcode.com/problems/kth-largest-element-in-an-array)

## Approach 1 [min-heap]

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

##[Other approaches](https://leetcode.com/problems/kth-largest-element-in-an-array/discuss/60309/C%2B%2B-STL-partition-and-heapsort)

## tags:
$min-heap$
$heap$
$multi-set$