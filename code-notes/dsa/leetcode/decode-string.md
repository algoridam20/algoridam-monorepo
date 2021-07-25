### [decode-string](https://leetcode.com/problems/decode-string/)

## Approach 1 [stack,string]

Time : O(n)
Space : O(n)

### explanation

```
self-explanatory
tips: 
    accumulate number till '[' is encountered
    accumulate string if possible at the top of the stack

```

```cpp
class Solution {
public:
    
    string repeat(string str,int n){
        string ans = "";
        for(int i=0;i<n;i++)
            ans = ans + str;
        return ans;
    }
    string decodeString(string s) {
        
        stack<string> st;
        string num = "";
        for(auto c: s){
            string top = "";
            if(isalpha(c)){
                top = "";
                if(!st.empty() && isalpha(st.top()[0])){
                    top = st.top();
                    st.pop();
                }
                st.push(top + c);
            }else if(c == ']'){
                top = st.top();st.pop();
                int times = stoi(st.top());st.pop();
                top = repeat(top,times);
                if(!st.empty() && isalpha(st.top()[0])){
                    top = st.top() + top;
                    st.pop();
                }
                st.push(top);
            }else if(isdigit(c)){
                num = num + c;
            }else{
                st.push(num);
                num = "";
            }
        }
        if(st.empty())
            return "";
        return st.top();
    }
};
``` 

```cpp
input: s = "3[a2[c]]"

output: "accaccacc"
```

## tags:
$stack$
$string$
$parsing$