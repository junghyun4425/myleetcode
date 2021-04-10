# Problem Link: https://leetcode.com/problems/integer-replacement/

'''
문제 요약: n이 짝수면 나누기 2, n이 홀수면 +1 혹은 -1 해서 결과가 1이되는 최단경로의 길이를 구하는 문제.
ask: n = 8
answer: 3 (8 -> 4 -> 2 -> 1)

해석:
n이 짝수일땐 별 문제 없지만 홀수일때는 +1과 -1로 분기점이 생김.
이런 부분을 커버하면서 최단경로를 찾는 방법은 BFS를 활용하면 됨. (DFS는 최소길이를 보장하지 않기에 BFS를 활용)
따라서 queue를 활용해 가장 적은 depth를 가질때 결과가 1이 나오는 길이를 반환해 해결.
'''

class Solution:
    def integerReplacement(self, n: int) -> int:
        min_len = -1
        queue = deque([n])
        while True:
            min_len += 1
            q_len = len(queue)
            while q_len > 0:
                num = queue.popleft()
                q_len -= 1
                if num == 1:
                    return min_len
                if num % 2 == 0:
                    queue.append(num//2)
                else:
                    queue.append(num-1)
                    queue.append(num+1)