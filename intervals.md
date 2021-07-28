+ [Insert Interval](#insert-interval)
+ [Merge Intervals](#merge-intervals)
+ [Non-overlapping Intervals](#non-overlapping-intervals)

[comment]: <> (Stop)

## Insert Interval

https://leetcode.com/problems/insert-interval/

``` python
def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    before,overlapping,after=[],[],[]
    merged=newInterval
    for interval in intervals:
        if interval[1]<newInterval[0]:
            before.append(interval)
        elif newInterval[1]<interval[0]:
            after.append(interval)
        else:
            overlapping.append(interval)
    if overlapping:
        merged[0]=min(newInterval[0],overlapping[0][0])
        merged[1]=max(newInterval[1],overlapping[-1][1])
    return before+[merged]+after
```
## Merge Intervals

https://leetcode.com/problems/merge-intervals/

``` python
def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort(key=lambda x:x[0])
    merged =[]
    if intervals:
        merged.append(intervals[0])
    else:
        return merged
    for interval in intervals[1:]:
        if interval[0]<= merged[-1][1]:
            merged[-1]=[merged[-1][0],max(interval[1],merged[-1][1])]
        else:
            merged.append(interval)
    return merged
```
## Non-overlapping Intervals

https://leetcode.com/problems/non-overlapping-intervals/

``` python
def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
    if not intervals:
        return 0
    removed = 0
    intervals.sort(key=lambda x:x[1])
    previous_right=intervals[0][1]
    for interval in intervals[1:]:
        if interval[0]<previous_right:
            removed+=1
        else:
            previous_right=interval[1]
    return removed
```