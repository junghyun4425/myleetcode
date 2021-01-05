# Problem Link: https://leetcode.com/problems/sqrtx/

'''
문제 요약: 입력값의 제곱근을 찾는 문제. (단, 소수는 모두 버림하고 정수만 반환)
ask: 8
answer: 2

해석:
난이도가 쉬움이기 때문에 그냥 return int(x ** 0.5) 를 하면 끝낼 수 있다고 판단.
아무리 쉬움이라도 제출자의 의도가 있으리라 생각되기에 그에 맞춰 문제를 다시 풀기로 함. (처음에는 단순히 while문으로 제곱근을 순차적으로 찾는 방식으로 구함)
문제는 속도가 매우 낮았기 때문에, 다음으로 대처할 수 있는 바이너리 서치로 수행.
역시 속도가 수십배는 빨라졌기에, 아무래도 이걸 목적으로 문제를 내지 않았나 하는 생각.
'''

class Solution:
    def mySqrt(self, x: int) -> int:
        l, h = 1, x
        m = (l + h) // 2
        while l*l <= x:
            if m * m <= x and (m+1)*(m+1) > x:
                return m
            if m * m > x:
                h = m - 1
            else:
                l = m + 1
            m = (l + h) // 2
        return 0