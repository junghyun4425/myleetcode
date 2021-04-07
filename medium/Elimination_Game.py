# Problem Link: https://leetcode.com/problems/elimination-game/

'''
문제 요약: 처음은 왼쪽에서 시작해서 한칸씩 띄워가며 제거, 다음은 오른쪽 반복해서 지워갈떄 하나 남은 숫자를 출력하는 문제.
ask: n = 9
answer: 6
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
arr = [2, 4, 6, 8]
arr = [2, 6]
arr = [6]

해석:
패턴을 찾으면 O(logn)에 해결이 가능한 문제. n을 바꿔가며 몇가지 변수를 두고 테스트 해봄.
먼저 direction이 있을테고, 시작지점 ans, interval, 현재 남은개수 n을 활용해 패턴을 찾음.
n = 40 인경우를 예로들면,
ans     direction       interval        n
1       1               1               40      (처음 1은 제거되며, n값은 반으로 줄어듦)
2       -1              2               20      (방향이 반대이며, 짝수이기 때문에 ans는 그대로 유지가 되어야 함)
2       1               4               10      (정방향이기 때문에 2는 지워지고, 다음으로 올 ans숫자는 2+4 = 6)
6       -1              8               5       (반대방향에 n이 홀수기 때문에 ans는 다음값으로 바뀌어야 함)
14      1               16              2       (오른쪽 방향이기 때문에 ans를 지우고 다음것으로 바꿔야함)
30      -1              32              1       (n == 1 이므로 loop 빠져나오기)
패턴 찾는데 오래걸렸지만 구현자체는 굉장히 심플했던 문제.
'''

class Solution:
    def lastRemaining(self, n: int) -> int:
        ans, direction, interval = 1, 1, 1
        while n > 1:
            if (direction == -1 and n % 2 == 1) or direction == 1:
                ans += interval
            n //= 2
            interval *= 2
            direction *= -1
        return ans