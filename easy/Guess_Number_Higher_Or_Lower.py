# Problem Link: https://leetcode.com/problems/guess-number-higher-or-lower/

'''
문제 요약: 지정된 숫자를 맞추는 게임으로, 제시한 숫자보다 크면 1을 작으면 -1을 같으면 0을 반환함.
ask: n = 10, pick = 6
answer: 6

해석:
난이도가 낮은만큼 간단한 방법으로 쉽게 풀리는 문제.
최소값 1부터 최대값 2**31 - 1 둘을 가지고 바이너리서치를 수행하면 쉽게 해결이 됨.
guess() 라는 API가 제공되므로 이를 통해 추정값이 목표값보다 큰지 작은지 확인후 탐색하면 끝.
'''

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l, r = 1, 2**31 - 1
        while l <= r:
            m = (l+r) // 2
            res = guess(m)
            if res < 0:
                r = m - 1
            elif res > 0:
                l = m + 1
            else:
                return m
        return -1