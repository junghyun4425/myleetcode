# Problem Link: https://leetcode.com/problems/water-and-jug-problem/

'''
문제 요약: 일정 사이즈 컵 두개를 사용해 타겟의 양을 채울수 있는지 확인하는 문제. (물을 최대용량까지만 채우고 옮기고 버리고 할수있음)
ask: jug1Capacity = 3, jug2Capacity = 5, targetCapacity = 4
answer: True

해석:
워낙 유명한 문제라서 문제 설명을 대충했지만, 좀더 자세히 설명하자면 물을 특정 양으로 만들수 있냐는 문제.
채우거나 비울때는 무조건 최대용량만. 옮길때는 목표컵에 최대치 까지만 옮길수 있다는 제약이 있음.
이 문제를 푸는 가장 유명한 방법은 최대공약수로 target값을 찾아내는 간단한 방법이 있지만, 프로그래머로서 수학적 지식을 몰랐을때 해결하는 방법으로 해결함.
모든 경우의 수를 queue에 대입하는 BFS방식으로 해결.
즉, visited에 컵 두개의 상황을 기록해서 사이클이 돌지 않게 하고, 타겟값이 나올때까지 BFS로 수행되게 함.
'''

class Solution:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        if jug1Capacity + jug2Capacity < targetCapacity:
            return False
        if jug1Capacity % 2 == 0 and jug2Capacity % 2 == 0 and targetCapacity % 2 != 0:
            return False
        if jug1Capacity + jug2Capacity == targetCapacity:
            return True
        visited = set()
        queue = deque([(0, 0)])
        while queue:
            cur = queue.popleft()
            if cur[0] + cur[1] == targetCapacity:
                return True
            if cur in visited:
                continue

            # Case 1 -> Fill jug1
            queue.append((jug1Capacity, cur[1]))

            # Case 2 -> Fill jug2
            queue.append((cur[0], jug2Capacity))

            # Case 3 -> From jug1 to jug2
            jug1 = max(cur[0] - (jug2Capacity - cur[1]), 0)
            jug2 = min(jug2Capacity, cur[0] + cur[1])
            queue.append((jug1, jug2))

            # Case 4 -> From jug2 to jug1
            jug2 = max(cur[1] - (jug1Capacity - cur[0]), 0)
            jug1 = min(jug1Capacity, cur[0] + cur[1])
            queue.append((jug1, jug2))

            # Case 5 -> Empty jug1
            queue.append((0, cur[1]))

            # Case 6 -> Empty jug2
            queue.append((cur[0], 0))

            visited.add(cur)
        return False