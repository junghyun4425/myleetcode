# Problem Link: https://leetcode.com/problems/power-of-four/

'''
문제 요약: n이 4의 제곱승인지 확인하는 문제.
ask: n = 16
answer: True

해석:
이전의 문제인 Power of Three 와 같은 문제.
Follow up 으로 loop를 쓰지 않게 하는것을 보니 수학적으로 접근해야하는 문제.
따라서 log_4(n) = log_10(n) / log_10(4) 의 결과가 0이 되는지 혹은 소수점이 남아있는지 체크하면 간단히 해결됨.
'''

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0: return False
        return (log(n) / log(4)) % 1 == 0