### [reverse-nodes-in-k-group](https://leetcode.com/problems/reverse-nodes-in-k-group)

## Approach 1 [iterative]

Time : O(n)
Extra Space : O(1)

### explanation
```
look ahead if reversal is possible 
if yes , reverse and reattch links
```


```cpp
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* reverse(ListNode* head, int k){
        ListNode* prev = NULL;
        ListNode* curr = head;
        for(int i=0;i<k;i++){
            ListNode* temp = curr->next;
            curr->next = prev;
            prev = curr;
            curr = temp;
        }
        return prev;
    }
    ListNode* reverseKGroup(ListNode* head, int k) {
        if(k < 2 || head == NULL) return head;
        ListNode* newHead = head;
        ListNode* curr = head;
        ListNode* prevEnd = NULL;
        while(true){
            ListNode* newEnd = curr;
            ListNode* nextStart = curr;
            for(int i=0;i<k;i++){
                if(nextStart == NULL)
                    return newHead;
                nextStart = nextStart->next;
            }
            ListNode* newStart = reverse(newEnd,k);
            if(prevEnd == NULL){
                newHead = newStart;
            }else{
                prevEnd->next = newStart;
            }
            prevEnd = curr;
            newEnd->next = nextStart;
            curr = nextStart;
        }
        return newHead;
    }
};
``` 

```cpp
input: head = [1,2,3,4,5], k = 3
output: [3,2,1,4,5]
```

## Approach 2 [recursive]

Time : O(n)
Extra Space : O(n)

### explanation

```
the required function itself returns pointer, use that fact to design recursion

look ahead if reversal is possible 
if yes , reverse and re-attach links recursively
```

```cpp
class Solution {
public:
    ListNode* reverse(ListNode* head, int k){
        ListNode* prev = NULL;
        ListNode* curr = head;
        for(int i=0;i<k;i++){
            ListNode* temp = curr->next;
            curr->next = prev;
            prev = curr;
            curr = temp;
        }
        return prev;
    }
    ListNode* reverseKGroup(ListNode* head, int k) {
        int count = 0;
        ListNode* nextStart = head;
        while(nextStart != NULL && count < k){
            count++;
            nextStart = nextStart->next;
        }
        if(count == k){
            ListNode* newHead = reverse(head,k);
            head->next = reverseKGroup(nextStart,k);
            return newHead;
        }
        return head;
    }
};
``` 


## tags:
$linked-list$
$reverse$
$recursion$