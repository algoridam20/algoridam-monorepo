### [generate-parentheses](https://leetcode.com/problems/generate-parentheses/)

## Approach 1 [recursion]

Time : O(catalan(n))
Space : O(catalan(n))

### explanation
```
similar to generating all binary search trees
solve(n) : 
    for(i : n):
        for(left: solve(i)):
            for(right: solve(n-i-1)):
                ans.push_back("(" + left + ")" + right)
```

```cpp
class Solution {
public:
    vector<string> generateParenthesis(int n) {
        if(n == 0){
            return {""};
        }
        vector<string> ans;
        for(int i=0;i<n;i++){
            vector<string> leftP = generateParenthesis(i);
            vector<string> rightP = generateParenthesis(n-1-i);
            for(auto left: leftP){
                for(auto right: rightP){
                    ans.push_back("(" + left + ")" + right);
                }
            }
        }
        return ans;
    }
};
``` 

```cpp
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
```

## Approach 2 [recursion]

Time : O(catalan(n))
Space : O(catalan(n))

### explanation

```cpp
class Solution {
public:
    vector<string> generateParenthesis(int n) {
        vector<string> ans;
        backtrack(ans,"",0,0,n);
        return ans;
        
    }
    void backtrack(vector<string>& ans,string curr,int open,int close,int max){
        if(curr.size() == 2*max){
            ans.push_back(curr);
            return;
        }
        if(open < max)
            backtrack(ans,curr+"(",open+1,close,max);
        if(close < open)
            backtrack(ans,curr+")",open,close+1,max);
    }
    
    
};
``` 

## tags:
$recursion$
$catalan$