### [queue-reconstruction-by-height](https://leetcode.com/problems/queue-reconstruction-by-height/)

## Approach 1 [greedy]

Time : O(n*n)
Space : O(n)

### explanation

sort the people by height and if height is same the sort by k(people infront)
fill the empty slots stating from shortest person
```
We put people in an array of length n. The number k means that we should put this person in the kth empty position from the beginning. The empty position mean that there will be higher or equal height person coming in here, so leave these positions out first. For everyone, we should first insert the lower h person. For the person who has same h we should first insert the person has larger k value. For everyone to put in, it takes O(n) time to find kth empty position, so it will take the O(n^2) time for all people.
E.g.
input: [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
sort: [[4,4], [5,2], [5,0], [6,1], [7,1], [7,0]]
step1: [[ , ], [ , ], [ , ], [ , ], [4,4], [ , ]]
step2: [[ , ], [ , ], [5,2], [ , ], [4,4], [ , ]]
step3: [[5,0], [ , ], [5,2], [ , ], [4,4], [ , ]]
step4: [[5,0], [ , ], [5,2], [6,1], [4,4], [ , ]]
step5: [[5,0], [ , ], [5,2], [6,1], [4,4], [7,1]]
step6: [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
```

```cpp
class Solution {
public:
    static bool comp(vector<int>& l,vector<int>& r){
        return (l[0] != r[0]) ? l[0] < r[0] : l[1] > r[1];
    }
    vector<vector<int>> reconstructQueue(vector<vector<int>>& people) {
        sort(people.begin(),people.end(),comp);
        int n = people.size();
        vector<vector<int>> ans(n,vector<int>(2,-1));
        for(auto person: people){
            int height = person[0];
            int pos = person[1];
            for(int i=0,slot=0;i<n;i++){
                if(ans[i][0] == -1){
                    if(slot == pos){
                        ans[i] = person;
                        break;
                    }
                    slot++;
                }
            }
        }
        return ans;
    }
};
``` 

```cpp
Input: people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
Output: [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]
Explanation:
Person 0 has height 5 with no other people taller or the same height in front.
Person 1 has height 7 with no other people taller or the same height in front.
Person 2 has height 5 with two persons taller or the same height in front, which is person 0 and 1.
Person 3 has height 6 with one person taller or the same height in front, which is person 1.
Person 4 has height 4 with four people taller or the same height in front, which are people 0, 1, 2, and 3.
Person 5 has height 7 with one person taller or the same height in front, which is person 1.
Hence [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]] is the reconstructed queue.
```

## Approach 2 [index-tree]

[explanation](https://leetcode.com/problems/queue-reconstruction-by-height/discuss/89342/O(nlogn)-Binary-Index-Tree-C%2B%2B-solution)

## tags:
$greedy$
$sort$
$index-tree$