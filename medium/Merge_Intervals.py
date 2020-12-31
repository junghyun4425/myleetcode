# Problem Link: https://leetcode.com/problems/merge-intervals/

'''
문제 요약: 숫자 리스트의 리스트에서 겹치는 부분을 합병시켜서 반환하는 문제.
ask: [[1,3],[2,6],[8,10],[15,18]]
answer: [[1,6],[8,10],[15,18]]

해석:
First Try 때는 순서대로 겹치는 부분이 없을때까지 가서 합치는 방식으로 해결.
여러 변수들 (ex, [[1,4],[0,0]] 정렬로 해결, [0,4],[0,2] max로 해결) 이 있어서 생각지도 못하게 코드가 점점 더러워짐.
따라서 다른방법으로 시도를 해보려고 함.

Second Try 는 첫 시도와 비슷한 방법으로 쓰되, 코드를 간결하게 만들 방법을 연구함.
처음엔 while 문에 cur을 통해서 시도를 했지만, 쓸데없는 중복만 있을뿐 intervals를 for문 수행하는 것과 다를바가 없음.
ans를 활용하면 이전것을 확인할 수 있기 때문에 while문과 cur 제거하고 더 간결하게 해결.
'''

# Second Try
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        intervals.sort()

        for interval in intervals:
            if not ans or ans[-1][1] < interval[0]:
                ans.append(interval)
            else:
                ans[-1][1] = max(ans[-1][1], interval[1])

        return ans

# First Try
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        i_len = len(intervals)
        ans = []
        cur = 0
        intervals.sort()
        while cur < i_len:
            overlap = intervals[cur]
            for i in range(cur, i_len):
                if intervals[i][0] <= overlap[1]:
                    overlap[0] = min(overlap[0], intervals[i][0])
                    overlap[1] = max(overlap[1], intervals[i][1])
                else:
                    ans.append(overlap)
                    break
                if i == i_len - 1:
                    ans.append(overlap)
                cur += 1
        return ans