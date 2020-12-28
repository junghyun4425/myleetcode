# Problem Link: https://leetcode.com/problems/powx-n/

'''
문제 요약: 제곱의 결과를 반환하는 문제. (따로 조건은 없으나 속도제한으로 O(logn))
ask: x = 2.10000 n = 3
answer: 9.26100

해석: 쉽게 푼 방법으로는 역시나 O(n) 시간복잡도를 생각해 볼 수 있는데, 역시나 시간초과로 실패.
그렇다는 말은 O(logn)까지 속도를 줄여야 함. 좀 더 고민해봐야함.
'''

class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans = 1
        minus = False
        if n < 0:
            n = abs(n)
            minus = True
        elif n == 0:
            return ans
        for i in range(n):
            ans *= x

        return ans if not minus else 1 / ans