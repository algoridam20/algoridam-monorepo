### [top-k-frequent-elements](https://leetcode.com/problems/top-k-frequent-elements/)

## Approach 1 [min-heap]

Time : O(Kmax logk)
Space : O(KMax)

### explanation
```
1.create count map
2.push it into minHeap making sure size of minHeap does not exceed k
3.convert minHeap to ans vector
```

```cpp
Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int,int> countMap;
        priority_queue<pair<int,int>,vector<pair<int,int>>, greater<pair<int,int>>> minHeap;
        for(auto num: nums){
            countMap[num]++;
        }
        for(auto it:countMap){
            minHeap.push({it.second,it.first});
            if(minHeap.size() > k)
                minHeap.pop();
        }
        
        vector<int> ans;
        while(!minHeap.empty()){
            ans.push_back(minHeap.top().second);
            minHeap.pop();
        }
        return ans;
    }
};
``` 

```cpp
[1,1,1,2,2,3]
2

output = [2,1]
```

## Approach 2 [sort]

Time : O(Kmax logKmax)
Space : O(Kmax)

### explanation
```
1.create count map
2.push it into a count vector and sort
3.convert count vector to ans vector
```

```cpp
class Solution {
public:
    static bool comp(pair<int,int> left,pair<int,int> right){
        return left.second > right.second;
    }
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int,int> countMap;
        for(auto num: nums){
            countMap[num]++;
        }
        vector<pair<int,int>> countVector;
        for(auto it:countMap){
            countVector.push_back({it.first,it.second});
        }
        sort(countVector.begin(),countVector.end(),comp);
        vector<int> ans;
        for(int i=0;i<k;i++){
            ans.push_back(countVector[i].first);
        }
        return ans;
    }
};
``` 

```cpp
[1,1,1,2,2,3]
2

output = [2,1]
```


## tags:
$min-heap$
$sort$