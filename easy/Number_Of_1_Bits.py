# Problem Link: https://leetcode.com/problems/number-of-1-bits/

'''
문제 요약: 입력으로 들어오는 바이너리 숫자 1의 개수를 반환하는 문제. (unsigned int, 32bits)
ask: 11111111111111111111111111111101
answer: 31

해석:
비트연산으로 값 n이 0이 될때까지 쉬프트연산으로 1의 개수를 세면 해결.
n & 1 혹은 n | 0 값이 1이 되는 경우만 cnt를 올려줌.
'''

class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt = 0
        while n != 0:
            if n & 1:
                cnt += 1
            n = n >> 1
        return cnt