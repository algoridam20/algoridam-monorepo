### [3sum](https://leetcode.com/problems/3sum/)

## Approach 1 [two-pointer]

Time : O(n*n)
Space : O(1)

### explanation
```
1. sort the array
2. run 2sum on the array where -1*target is unique -ve elements form given array
3. while running two sum when target is found 
    move start and end pointers to such that repeated elements are avoided and
    continue searching till start > end
    
```

```cpp
class Solution {
public:
    
    vector<vector<int>> ANS;
    void twoSum(vector<int>& nums,int x,int start,int end){
        while(start < end){
            int y = nums[start];
            int z = nums[end];
            if(y+z == x){
                vector<int> triplet = {-1*x,y,z};
                ANS.push_back(triplet);
                while(start < end && nums[start] == y ) start++;
                while(start < end && nums[end] == z ) end--;
            }else if(y+z < x)
                start++;
            else
                end--;
        }
    }
    vector<vector<int>> threeSum(vector<int>& nums) {
        int n = nums.size();
        ANS.clear();
        sort(nums.begin(),nums.end());
        for(int i=0;i<n-1;i++){
            if(nums[i] > 0)
                break;
            if(i == 0 || nums[i] != nums[i-1])
                twoSum(nums,-1*nums[i],i+1,n-1);
        }
        return ANS;
    }
};
``` 

```cpp
input = [-1,0,-2,4,1,0,-1,2,3,2,-1,-4]

output = [[-4,0,4],[-4,1,3],[-4,2,2],[-2,-1,3],[-2,0,2],[-1,-1,2],[-1,0,1]]
```

## tags:
$two-pointer$