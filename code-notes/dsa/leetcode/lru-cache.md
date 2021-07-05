### [lru-cache](https://leetcode.com/problems/lru-cache/)

## Approach 1 [doubly-linked-list,hash-map]

Time : O(1)
Space : O(capacity)

### explanation
```
idea is to keep the address of key in a hash map ( AddressMap );
when key is get or set , move the key to top of the list.
and when setting a key:value pair if the size of list grows more than capacity pop_back();
```

```cpp
class LRUCache {
public:
    unordered_map<int,list<int>::iterator> addressMap;
    list<int> keys;
    unordered_map<int,int> cache;
    int capacity;
    
    LRUCache(int c) {
        capacity = c;
        addressMap.clear();
        cache.clear();
        keys.clear();
    }
    
    int get(int key) {
        if(cache.find(key) == cache.end())return -1;    
        update(key);       
        return cache[key];
    }
    
    void put(int key, int value) {
        if(cache.find(key) == cache.end()){
            keys.push_front(key);
            list<int>::iterator address = keys.begin();
            addressMap[key] = address;
        }else
            update(key);
        cache[key] = value;
        if(keys.size() > capacity){
            int deleteKey = *(--keys.end());
            keys.pop_back();
            cache.erase(deleteKey);
            addressMap.erase(deleteKey);
        }
    }
    void update(int key){
        list<int>::iterator address = addressMap[key];
        keys.erase(address);
        keys.push_front(key);
        addressMap[key] = keys.begin(); 
    }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */
``` 

```cpp
Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4
```

## tags:
$list$
$hash-map$
$doubly-linked-list$