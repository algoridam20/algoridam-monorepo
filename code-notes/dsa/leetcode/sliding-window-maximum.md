### [sliding-window-maximum](https://leetcode.com/problems/sliding-window-maximum/)


## Approach 1 [monotonic-queue]

Time : O(n)
Space : O(n)

### explanation
```
1. create a deque 
2. incoming (when window is slided by one step) elements are push_back into to he dqueue
3. outgoing elements can only be at the top of the dqueue , and can be removed if present
4. the idea is to maintain a monotonically increasing dqueue
5. so when elements are inserted into the dqueue 
    make sure to remove all the elements from the back (of the queue)
    that are smaller than incoming element
```

```cpp
class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        vector<int> ans;
        int n = nums.size();
        if(k>n) return ans;
        deque<int> queue;
        for(int i=0;i<k;i++){
            int in = nums[i];
            while(queue.size() > 0 && queue.back() < in)
                queue.pop_back();
            queue.push_back(in);
        }
        ans.push_back(queue.front());
        for(int i=1;i<=n-k;i++){
            int out = nums[i-1];
            int in = nums[i+k-1];
            while(queue.size() > 0 && queue.back() < in)
                queue.pop_back();
            if(queue.size() > 0 && queue.front() == out)
                queue.pop_front();
            queue.push_back(in);
            ans.push_back(queue.front());            
        }
        return ans;
    }
};
``` 

```cpp
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

```

## Approach 2 [priority-queue,hash-map]

Time : O(nlogk)
Space : O(n)

### explanation
```
1. maintain an hash map to check if the element is in sliding window
2. push the incoming element into a maxHeap
3. add top of the heap to ans if it is present in the hashmap
    else pop top
4. for optimization clear priority queue when incoming element is greater than priority queue top
```


```cpp
class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        vector<int> ans;
        int n = nums.size();
        if(k>n) return ans;
        priority_queue<int> PQ;
        unordered_map<int,int> M;
        for(int i=0;i<k;i++){
            M[nums[i]]++;
            PQ.push(nums[i]);
        }
        ans.push_back(PQ.top());
        for(int i=1;i<=n-k;i++){
            int out = nums[i-1];
            int in = nums[i+k-1];
            M[out]--;
            M[in]++;
            if(PQ.top() < in)
                PQ = priority_queue<int>();
            else{
                while(!PQ.empty() && M[PQ.top()] <= 0)
                    PQ.pop();
            }
            PQ.push(in);
            ans.push_back(PQ.top());            
        }
        return ans;
    }
``` 


## Approach 3 [multi-set]

Time : O(nlogk)
Space : O(n)

### explanation
```
1. insert incoming element into a multiset 
2. remove outgoing element from the multiset 
3. and add last element of the multiset into ans as it is the largest element in the multiset
```

```cpp
class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        vector<int> ans;
        int n = nums.size();
        if(k>n) return ans;
        multiset <int> S;
        for(int i=0;i<k;i++){
            S.insert(nums[i]);
        }
        ans.push_back(*(--S.end()));
        for(int i=1;i<=n-k;i++){
            int out = nums[i-1];
            int in = nums[i+k-1];
            S.insert(in);
            S.erase(S.find(out));
            ans.push_back(*(--S.end()));         
        }
        return ans;
    }
};
``` 

## tags:
$priority-queue$
$hash-map$
$dqueue$
$multi-set$