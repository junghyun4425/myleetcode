# Problem Link: https://leetcode.com/problems/bitwise-and-of-numbers-range/

'''
문제 요약: m, n 포함한 사이의 값들을 모두 AND 연산했을때 결과를 반환하는 문제.
ask: m=5, n=7
answer: 4 (5 & 6 & 7)

해석:
Brute Force로는 모든 사이값들을 and 연산하면 되지만 시간복잡도가 굉장히 비효율적.
그래서 AND연산의 특징 하나를 잘 살리면 문제를 굉장히 빠르게 해결 가능.
Flipped 원리를 알아야 하는데, 두개의 bit 값이 flipped (다른) 상태라면 and연산시 무조건 0이라는 점.

하나의 예시를 들면,
m = 10101
n = 10111
경우에서, 앞에 3자리 101은 Fixed 라서 m ~ n 사이에 변하지 않는 값. 따라서 뒷쪽 01 과 11 만 0으로 바꿔주면 모든값을 and 한 결과가 나옴.
뒤에서부터 한자리씩 지워가며 m == n 을 확인하고, 같다면 뒷자리 수를 지운만큼 0을 붙여주면 해결.
'''

class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        for i in range(32):
            if m == n:
                return m << i
            m >>= 1
            n >>= 1