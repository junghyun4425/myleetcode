# Problem Link: https://leetcode.com/problems/find-median-from-data-stream/

'''
문제 요약: median값을 출력하는 class를 구현하는 문제.
ask:
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
answer:
[null, null, null, 1.5, null, 2.0]

해석:
쉬워보여서 금방 해결할 것 같았는데 시간제한이 굉장히 난이도 있는 문제. O(n) 시간복잡도로는 시간통과가 불가능.
따라서 방법은 오직 O(logn)을 만족해야만 가능.
따라서 Binary Search 혹은 Tree과 같이 logarithmic case의 형태로 탐색하게 만들어야 해결이 가능.
여기서 선택한 방법으로 heap을 두개로 관리하는 방법.
하나는 max_heap으로 정렬된 배열의 왼쪽을, 다른 하나는 min_heap으로 오른쪽을 가지게 함.
이를 위해서 몇가지 알아둬야할 점이 있는데,
min_heap은 max_heap으로부터 빠져나온 가장 큰값을 저장해야 정렬된 효과를 가짐.
max_heap 길이와 min_heap의 길이가 같을때는 max_heap에 넣어줘서 둘의 길이를 항상 일정하게 유지하거나 max_heap이 1크게 유지시켜줌.
구현 자체는 쉽지만 아이디어를 생각하기까지 굉장히 오래걸림.
'''

import heapq
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.max_heap = []
        self.min_heap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.max_heap, -num)
        tmp = heapq.heappop(self.max_heap)
        heapq.heappush(self.min_heap, -tmp)
        if len(self.max_heap) < len(self.min_heap):
            tmp = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -tmp)

    def findMedian(self) -> float:
        if len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        return (-self.max_heap[0] + self.min_heap[0]) * 0.5

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()