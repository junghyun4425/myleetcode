# Problem Link: https://leetcode.com/problems/insert-interval/

'''
문제 요약: 숫자 리스트의 리스트에서 새로운 리스트 하나를 추가해 겹치는 부분을 합병시켜서 반환하는 문제.
ask: intervals = [[1,3],[6,9]], newInterval = [2,5]
answer: [[1,5],[6,9]]

해석:
이전에 풀었던 문제가 O(nlogn)의 시간복잡도를 가졌다면, 이번엔 O(n)까지 가능할 것으로 보임.
일단 이전에 풀었던 방법에 newInterval을 추가해서 해결했으며, 다음에 풀어보기.
'''

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []
        intervals.append(newInterval)
        intervals.sort()

        for interval in intervals:
            if not ans or ans[-1][1] < interval[0]:
                ans.append(interval)
            else:
                ans[-1][1] = max(ans[-1][1], interval[1])

        return ans