# Problem Link: https://leetcode.com/problems/non-overlapping-intervals/

'''
문제 요약: 입력으로 들어오는 간격 중 겹치는 부분을 제거할떄 최소로 지우는 개수를 구하는 문제.
ask: intervals = [[1,2],[2,3],[3,4],[1,3]]
answer: 1 ([1,3] 하나만 지우면 겹치는 구간이 없어짐)

해석:
이와 유사한 문제를 그리디 알고리즘으로 풀었던 기억이 있어서 쉽게 해결했던 문제.
중복없이 가장 길게 만들수 있는 경우를 찾기위해 interval 앞자리로 먼저 정렬을 수행.
정렬된채로 하나씩 end를 비교하며, 기존의 end point보다 오른쪽의 start 부분이 더 크다면 overlap 된 상태.
따라서 중복도를 하나 증가시켜 주고, 둘중 더 작은 end값을 현재 end로 바꿔줌.
이런식으로 작은 값의 end point를 바꿔줘서 그리디하게 해결이 가능. (물론 DP도 가능하나 이 문제에선 그리디 알고리즘이 효율적)
'''

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        ans = 0
        end = intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][0] < end:
                ans += 1
                end = min(end, intervals[i][1])
            else:
                end = intervals[i][1]
        return ans