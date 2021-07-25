### [brace-expansion](https://leetcode.com/problems/brace-expansion)

## Approach 1 [recursion]

Time : O(n^2)
Space : O(n^2)

### explanation
```
time complexity is polynomial = product of all choices.size()
```

```cpp
class Solution {
public:
    void recursion(int start,int end,string str,vector<string>& ans){
        if(start > end) return;
        string curr = "";
        vector<char> choices;
        bool inChoice = false;
        int newStart = 0;
        for(int i=start;i<=end;i++){
            if(isalpha(str[i])){
                if(!inChoice)
                    curr += str[i];
                else
                    choices.push_back(str[i]);
            }else if(str[i] == '{'){
                inChoice = true;
                if(ans.size() == 0 && curr != ""){
                    ans.push_back(curr);
                }else if(curr != ""){
                    for(int j=0;j<ans.size();j++){
                        ans[j] = ans[j] + curr;
                    }
                }
            }else if(str[i] == '}'){
                sort(choices.begin(),choices.end());
                vector<string> newAns;
                if(ans.size() == 0){
                    for(auto choice:choices){
                        newAns.push_back(string (1,choice));
                    }
                }
                for(int j=0;j<ans.size();j++){
                    for(auto choice:choices){
                        newAns.push_back(ans[j] + choice);
                    }
                }
                ans = newAns;
                recursion(i+1,end,str,ans);
                return;
            }
        }
        if(ans.size() == 0 && curr != ""){
            ans.push_back(curr);
        }else if(curr != ""){
            for(int i=0;i<ans.size();i++){
                ans[i] = ans[i] + curr;
            }
        }
        return;
    }
    vector<string> expand(string s) {
        vector<string> ans;
        recursion(0,s.size()-1,s,ans);
        return ans;
    }
};
``` 

```cpp
input: s = "{a,b}c{d,e}f"
output: ["acdf","acef","bcdf","bcef"]
```


## tags:
$parsing$
$recursion$