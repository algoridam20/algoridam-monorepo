### [time-based-key-value-store](https://leetcode.com/problems/time-based-key-value-store/)

## Approach 1 [hash-map,binary-search]

Time : O(nlogn)
Space : O(n)

### explanation

```
as same key can have multiple values
and set timestamps are always in increasing order
we can use binary search to find the max timestamp and its values that are <= get_timestamp
```

```cpp
auto _fast_ = []() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    return nullptr;
} ();

class TimeMap {
public:
    int binarySearch(vector<pair<int,string>>& values,int x){
        int start = 0;
        int end = values.size()-1;
        while(start <= end){
            int mid = start + (end-start)/2;
            if(values[mid].first <= x && ((mid+1 <= end && values[mid+1].first > x) || mid == end))
                return mid;
            if(values[mid].first > x)
                end = mid - 1;
            else 
                start = mid + 1;
        }
        return -1;
    }
    /** Initialize your data structure here. */
    unordered_map<string,vector<pair<int,string>>> timeMap;
    TimeMap() {
        timeMap.clear();
    }
    
    void set(string key, string value, int timestamp) {
        timeMap[key].push_back({timestamp,value});
    }
    
    string get(string key, int timestamp) {
        int index = binarySearch(timeMap[key],timestamp);
        return (index != -1) ? timeMap[key][index].second : "";
    }
    
};

/**
 * Your TimeMap object will be instantiated and called as such:
 * TimeMap* obj = new TimeMap();
 * obj->set(key,value,timestamp);
 * string param_2 = obj->get(key,timestamp);
 */
``` 

```cpp
Input
["TimeMap", "set", "get", "get", "set", "get", "get"]
[[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]
Output
[null, null, "bar", "bar", null, "bar2", "bar2"]

Explanation
TimeMap timeMap = new TimeMap();
timeMap.set("foo", "bar", 1);  // store the key "foo" and value "bar" along with timestamp = 1.
timeMap.get("foo", 1);         // return "bar"
timeMap.get("foo", 3);         // return "bar", since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 is "bar".
timeMap.set("foo", "bar2", 4); // store the key "foo" and value "ba2r" along with timestamp = 4.
timeMap.get("foo", 4);         // return "bar2"
timeMap.get("foo", 5);         // return "bar2"
```

## tags:
$binary-search$
$hash-map$