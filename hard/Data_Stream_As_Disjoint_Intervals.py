# Problem Link: https://leetcode.com/problems/data-stream-as-disjoint-intervals/

'''
문제 요약: 숫자간 모든 interval을 배열로 알려주는 SummaryRange를 구현하는 문제.
ask:
["SummaryRanges", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals"]
[[], [1], [], [3], [], [7], [], [2], [], [6], []]
answer:
[null, null, [[1, 1]], null, [[1, 1], [3, 3]], null, [[1, 1], [3, 3], [7, 7]], null, [[1, 3], [7, 7]], null, [[1, 3], [6, 7]]]

해석:
First Try
첫번째 시도는 간단하게 addNum, getIntervals 두 함수를 각각 O(n) 의 시간복잡도를 가지게 설계함.
addNum은 Fast insertion sorting 방식으로 해결했으며, getIntervals는 정렬된 arr 기반으로 연속범위를 모두 찾아냄.
시간제한에 걸리진 않았지만 성능자체가 그리 좋은 편은 아님.

Second Try
O(n)에서 더 줄일수 있는 방법은 아무래도 O(logn)의 경우를 고려해야 함.
따라서 heap queue에 [start, end] 를 저장해둔 다음, 하나씩 빼서 쓰는 방법으로 시도함.
addNum 함수에서 힙에 저장하도록 구현. O(logn)
getIntervlas 함수에서 힙을 하나씩 다 pop하면서 range를 찾아냄.
힙을 다 빼내고, 새로만든 결과가 이미 정렬되어있기 때문에 이를 다시 힙에 저장하면 끝.
첫번째 시도에 비해 대충 8배 정도 빠른성능을 보임.
'''

# Second Try ( addNum -> O(logn) // getIntervals -> O(logn) )
class SummaryRanges:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.intervals = []
        self.vals = set()

    def addNum(self, val: int) -> None:
        if not val in self.vals:
            heappush(self.intervals, [val, val])
            self.vals.add(val)

    def getIntervals(self) -> List[List[int]]:
        res = []
        while self.intervals:
            interval = heappop(self.intervals)
            while self.intervals and interval[1]+1 == self.intervals[0][0]:
                interval[1] = self.intervals[0][1]
                heappop(self.intervals)
            res.append(interval)
        self.intervals = res
        return res

# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()


# First Try ( addNum -> O(n) // getIntervals -> O(n) )
'''
class SummaryRanges:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.arr = []

    def addNum(self, val: int) -> None:
        i = 0
        while i < len(self.arr):
            if self.arr[i] > val:
                self.arr = self.arr[:i] + [val] + self.arr[i:]
                return
            elif self.arr[i] == val:
                return
            i += 1
        self.arr.append(val)

    def getIntervals(self) -> List[List[int]]:
        ans = []
        start = end = self.arr[0]
        for i in range(1, len(self.arr)):
            if end+1 == self.arr[i]:
                end += 1
            else:
                ans.append([start, end])
                start = end = self.arr[i]
        ans.append([start, end])
        return ans
'''