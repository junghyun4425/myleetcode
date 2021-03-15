# Problem Link: https://leetcode.com/problems/add-digits/

'''
문제 요약: 숫자의 자리수마다 합을 구하고 한자리수가 될때까지 연산하는 문제.
ask: 38
answer: 2 ( 3+8=11, 1+1=2 )

해석:
숫자를 10으로 나누면서 나머지들을 더하면 자리수마다 합을구한 결과가 나옴.
이 결과가 한자리수일때까지 반복함.

재밌는 사실은 O(1) 에 푸는 방법이 있는데, 수학적 접근이 필요함. mod 9 의 결과로 정답을 한번에 찾아내며 증명은 solution에 있음.
'''

class Solution:
    def addDigits(self, num: int) -> int:
        ans = 0
        while num > 0:
            ans += num % 10
            num //= 10
            if num == 0 and ans > 9:
                num = ans
                ans = 0
        return ans