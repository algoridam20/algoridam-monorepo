### [insert-delete-getrandom-o1](https://leetcode.com/problems/insert-delete-getrandom-o1/)

## Approach 1 [hash-map]

Time : O(1)
Space : O(1)

### explanation

```
maintain 2 data structures
1. indexMap [HashMap]
2. randomSet [random access vector]

hash map is used to store the index of value stored in randomSet;
to insert in O(1)
    push value to the end of vector 
    and add its index to hashMap 

to remove in O(1)
    find the element be removed using its index from hashMap
    swap it with last element in vector
    update index of last element in hashMap
    delete element to be removed from hashMap and pop_back the vector

to getRandom in O(1) where all elements in set have same probability
    rand()%randomSet.size() guarantees to uniformly choose any index from 0 to size of randomSet
    so return randomSet[rand()%randomSet.size()]

```

```cpp
class RandomizedSet {
public:
    
    unordered_map<int,int> indexMap;
    vector<int> randomSet;
    int end;
    /** Initialize your data structure here. */
    RandomizedSet() {
        indexMap.clear();
        randomSet.clear();   
    }
    
    /** Inserts a value to the set. Returns true if the set did not already contain the specified element. */
    bool insert(int val) {
        if(indexMap.find(val) != indexMap.end()) return false;
        randomSet.push_back(val);
        indexMap[val] = randomSet.size()-1;
        return true;
    }
    
    /** Removes a value from the set. Returns true if the set contained the specified element. */
    bool remove(int val) {
        if(indexMap.find(val) == indexMap.end()) return false;
        int removeAtIndex = indexMap[val];
        int end = randomSet.size() - 1;
        indexMap.erase(val);
        if(removeAtIndex != end){
            indexMap[randomSet[end]] = removeAtIndex;
            swap(randomSet[removeAtIndex],randomSet[end]);
        }
        randomSet.pop_back();
        return true;
    }
    
    /** Get a random element from the set. */
    int getRandom() {
        if(end == -1) return -1;
        return randomSet[rand()%randomSet.size()];
    }
};

```cpp
Input
["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
[[], [1], [2], [2], [], [1], [2], []]
Output
[null, true, false, true, 2, true, false, 2]

Explanation
RandomizedSet randomizedSet = new RandomizedSet();
randomizedSet.insert(1); // Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomizedSet.remove(2); // Returns false as 2 does not exist in the set.
randomizedSet.insert(2); // Inserts 2 to the set, returns true. Set now contains [1,2].
randomizedSet.getRandom(); // getRandom() should return either 1 or 2 randomly.
randomizedSet.remove(1); // Removes 1 from the set, returns true. Set now contains [2].
randomizedSet.insert(2); // 2 was already in the set, so return false.
randomizedSet.getRandom(); // Since 2 is the only number in the set, getRandom() will always return 2.
```

## tags:
$hash-map$
$arrays$
$random$