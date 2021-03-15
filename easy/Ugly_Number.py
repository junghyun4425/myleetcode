# Problem Link: https://leetcode.com/problems/ugly-number/

'''
문제 요약: Ugly Number를 확인하는 문제. (2,3,5 로만 곱해진 값을 의미)
ask: 14
answer: False

해석:
2,3,5 로 나눌수 있을때까지 모두 나눠서 남은 값이 1이면 Ugly, 아니면 False를 반환하는 식으로 해결.
'''

class Solution:
    def isUgly(self, n: int) -> bool:
        if n < 1:
            return False
        for i in (5,3,2):
            while n % i == 0:
                n //= i
        return True if n == 1 else False