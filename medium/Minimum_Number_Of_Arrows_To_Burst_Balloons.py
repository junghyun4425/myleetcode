# Problem Link: https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

'''
문제 요약: 풍선의 y축 위치는 동일하고 왼쪽과 오른쪽 위치를 담은 배열이 입력으로 들어올때, 몇번의 화살을 쏴야 모든 풍선을 터트릴수 있는지 묻는 문제.
ask: points = [[10,16],[2,8],[1,6],[7,12]]
answer: 2

해석:
화살이 하나의 풍선안에 들어갔을때, 다른풍선의 위치가 겹친다면 한번에 터트릴 수 있음.
따라서 겹치는 부분을 최대화해서 한번에 터트리고 다음에 또 터트리는 방식.
이를 효율적으로 구현하기 위해서 그리디방식을 사용.
우선 end 를 기준으로 정렬하고 이전 풍선의 end포인트, 비교할 풍선의 start포인트 위치를 파악함.
만약 이전 풍선의 end포인트가 크거나 같다면 비교할 풍선이 겹쳐있는 상태이므로 그냥 넘어감.
그 반대의 경우에는 화살을 한번 더 던져야 하기 때문에 개수를 증가하는 방식으로 구현함.
'''

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[1])
        ans = 1
        prev = points[0][1]
        for s, e in points:
            if prev >= s:
                continue
            prev = e
            ans += 1
        return ans