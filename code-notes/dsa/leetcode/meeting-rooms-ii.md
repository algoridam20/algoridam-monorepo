### [meeting-rooms-ii](https://leetcode.com/problems/meeting-rooms-ii/)

## Question
```
Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], 
return the minimum number of conference rooms required.
```

## Approach 1 [greedy,sort]

Time : O(nlogn)
Space : O(sort)

### explanation
```
Intuition:
    if we look at meetings in order of their start time, 
        for a new meeting 
        we will look for available room , 
        (room is available if one of meeting is over, meeting with lowest end time is the one that can free one room)
        if( current meeting start time > lowest end time of previous meetings)
            we can take the freed up room
        else
            we can allocate new room

min Heap is good data structure to keep track of previous meetings with lowest end time.


Algorithm

1. Sort the given meetings by their start time.

2. Initialize a new min-heap and add the first meeting's ending time to the heap. We simply need to keep track of the ending times as that tells us when a meeting room will get free.

3. For every meeting room check if the minimum element of the heap i.e. the room at the top of the heap is free or not.

4. If the room is free, then we extract the topmost element and add it back with the ending time of the current meeting we are processing.

5. If not, then we allocate a new room and add it to the heap.
After processing all the meetings, the size of the heap will tell us the number of rooms allocated. This will be the minimum number of rooms needed to accommodate all the meetings.

```

```cpp
class Solution {
public:
    static bool comp(vector<int>& left,vector<int>& right){
        return left[0] < right[0];
    }
    int minMeetingRooms(vector<vector<int>>& intervals) {
        int ans = 0;
        sort(intervals.begin(),intervals.end(),comp);
        priority_queue<int, vector<int>, greater<int>> minHeap;
        minHeap.push(intervals[0][1]);
        int n = intervals.size();
        for(int i=1;i<n;i++){
            int currStart = intervals[i][0];
            int currEnd = intervals[i][1];
            if(currStart >= minHeap.top()){
                minHeap.pop();
            }
            minHeap.push(currEnd);
        }
        return minHeap.size();
    }
};
``` 

```cpp
Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2
```

## Approach 2 [sort,greedy,two-pointer]

Time : O(nlogn)
Space : O(n)

### explanation
```
Algorithm

1. Separate out the start times and the end times in their separate arrays.

2. Sort the start times and the end times separately. Note that this will mess up the original correspondence of start times and end times. They will be treated individually now.

3. We consider two pointers: s_ptr and e_ptr which refer to start pointer and end pointer. The start pointer simply iterates over all the meetings and the end pointer helps us track if a meeting has ended and if we can reuse a room.

4. When considering a specific meeting pointed to by s_ptr, we check if this start timing is greater than the meeting pointed to by e_ptr. If this is the case then that would mean some meeting has ended by the time the meeting at s_ptr had to start. So we can reuse one of the rooms. Otherwise, we have to allocate a new room.

5. If a meeting has indeed ended i.e. if start[s_ptr] >= end[e_ptr], then we increment e_ptr.

Repeat this process until s_ptr processes all of the meetings.

Let us not look at the implementation for this algorithm.
```


```java
class Solution {
    public int minMeetingRooms(int[][] intervals) {
        
    // Check for the base case. If there are no intervals, return 0
    if (intervals.length == 0) {
      return 0;
    }

    Integer[] start = new Integer[intervals.length];
    Integer[] end = new Integer[intervals.length];

    for (int i = 0; i < intervals.length; i++) {
      start[i] = intervals[i][0];
      end[i] = intervals[i][1];
    }

    // Sort the intervals by end time
    Arrays.sort(
        end,
        new Comparator<Integer>() {
          public int compare(Integer a, Integer b) {
            return a - b;
          }
        });

    // Sort the intervals by start time
    Arrays.sort(
        start,
        new Comparator<Integer>() {
          public int compare(Integer a, Integer b) {
            return a - b;
          }
        });

    // The two pointers in the algorithm: e_ptr and s_ptr.
    int startPointer = 0, endPointer = 0;

    // Variables to keep track of maximum number of rooms used.
    int usedRooms = 0;

    // Iterate over intervals.
    while (startPointer < intervals.length) {

      // If there is a meeting that has ended by the time the meeting at `start_pointer` starts
      if (start[startPointer] >= end[endPointer]) {
        usedRooms -= 1;
        endPointer += 1;
      }

      // We do this irrespective of whether a room frees up or not.
      // If a room got free, then this used_rooms += 1 wouldn't have any effect. used_rooms would
      // remain the same in that case. If no room was free, then this would increase used_rooms
      usedRooms += 1;
      startPointer += 1;

    }

    return usedRooms;
  }
}
```

## Approach 3 [hash-map]

Time : O(nlogn)
Space : O(n)

### explanation
```
at every instance if meeting starts new room is added
and if meeting ends room is released

max value total rooms can reach is minimum number of rooms required to conduct all meetings
```


```cpp
class Solution {
public:
    int minMeetingRooms(vector<vector<int>>& intervals) {
      int totalRooms=0,ans=0;
      map<int,int> m;
      for(int i=0;i<intervals.size();i++){
          m[intervals[i][0]]++;
          m[intervals[i][1]]--;
      }
     for(auto it:m){
          totalRooms+=it->second;
          ans=max(ans,totalRooms);
      }
      return ans;
    }
};
```

## tags:
$sort$
$greedy$
$two-pointer$