### [palindromic-substrings](https://leetcode.com/problems/palindromic-substrings/)

## Approach 1 [two-pointer]

Time : O(n*n)
Space : O(n)

### explanation
for all elements in string:
    growPalindrome using current char as center,for odd size palindromes
    growPalindrome using [current and prev] char as center, for even size palindromes

```cpp
class Solution {
public:

    void growPalindrome(string s,int left,int right,int& ans,int& n){
        while(left >=0 && right <n && s[left] == s[right]){
            ans++;
            left--;
            right++;
        }
    }
    int countSubstrings(string s) {
        int n = s.size();
        int ans = 1;
        for(int mid=1;mid<n;mid++){
            growPalindrome(s,mid,mid,ans,n);
            growPalindrome(s,mid-1,mid,ans,n);
        }
        return ans;
    }
};
``` 

```cpp
Input: s = "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
```

## Approach 2 [dp]

Time : O(n*n)
Space : O(n*n)

### explanation
```
base case
dp[0] = vector<int>(n,1);
dp[1] = vector<int>(n,1);

dp:

if(s[i] == s[i-l+1] && dp[l-2][i-1] == 1){
    dp[l][i] = 1;
    ans++;
}
else
    dp[l][i] = 0;
```

```cpp
class Solution {
public:
    int countSubstrings(string s) {
        int n = s.size();
        int ans = n;
        vector<vector<int>> dp(n+1,vector<int>(n,0));
        dp[0] = vector<int>(n,1);
        dp[1] = vector<int>(n,1);
        for(int l=2;l<=n;l++){
            int j = l - 1;
            for(int i=j;i<n;i++){
                if(s[i] == s[i-l+1] && dp[l-2][i-1] == 1){
                    dp[l][i] = 1;
                    ans++;
                }
                else
                    dp[l][i] = 0;
                    
            }
        }
        return ans;
    }
};
``` 


## tags:
$two-pointer$
$dp$