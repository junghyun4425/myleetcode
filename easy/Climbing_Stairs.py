# Problem Link: https://leetcode.com/problems/climbing-stairs/

'''
문제 요약: n개의 계단을 오르는 방법의 가지 수를 반환하는 문제 (단, 한번에 1, 2칸 까지 밖에 못감)
ask: n = 3
answer: 3 (1 + 1 + 1, 1 + 2, 2 + 1 총 3가지 경우)

해석:
문제를 보자마자 바로 재귀로 간단하게 풀어봤지만 역시나 시간초과.
그래서 DP로 풀어봤는데 뭔가 피보나치 스러운 결과를 보게 됨.
다시 피보나치 방식과 같게 풀었더니 정답...
'''

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        fir, sec = 1,2
        for i in range(3, n+1):
            tmp = fir + sec
            fir = sec
            sec = tmp
        return sec