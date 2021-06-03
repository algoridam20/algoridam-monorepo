#[kth-largest-element-in-a-stream](https://leetcode.com/problems/kth-largest-element-in-a-stream)

## Approach 1 [min-heap]

Time : O(nlogk) to init and O(logk) to add
Space : O(k)

```cpp
class KthLargest {
public:
    int K;
    priority_queue<int, vector<int>, greater<int>> minHeap;
    KthLargest(int k, vector<int>& nums) {
        K = k;
        minHeap = priority_queue<int, vector<int>, greater<int>>();
        for(int num:nums){
            minHeap.push(num);
            if(minHeap.size() > K)
                 minHeap.pop();
        }
    }
    
    int add(int num) {
        minHeap.push(num);
        if(minHeap.size() > K)
            minHeap.pop();
        return minHeap.top();
    }
};

/**
 * Your KthLargest object will be instantiated and called as such:
 * KthLargest* obj = new KthLargest(k, nums);
 * int param_1 = obj->add(val);
 */
``` 

## tags:
$min-heap$
$stream$
$heap$