# Problem Link: https://leetcode.com/problems/climbing-stairs/

'''
문제 요약: n개의 계단을 오르는 방법의 가지 수를 반환하는 문제 (단, 한번에 1, 2칸 까지 밖에 못감)
ask: n = 3
answer: 3 (1 + 1 + 1, 1 + 2, 2 + 1 총 3가지 경우)

해석:
문제를 보자마자 바로 재귀로 간단하게 풀어봤지만 역시나 시간초과.
그래서 DP로 풀어봤는데 뭔가 피보나치 스러운 결과를 보게 됨.
다시 피보나치 방식과 같게 풀었더니 정답...

Review
피보나치보다 더 효율좋은 방법을 찾지 못했기에, 단순히 연습삼아 recursion으로 memoization 방식으로 풀어봄.
거의 해본적 없는 방법이라 굉장히 생소했는데, m[i]를 저장하고 언제 쓰는지 파악하질 못했음.
단순히 생각해봤을때 마지막까지 가고, 마지막값에 0이 아닌 1이 들어갔다면 앞으론 계속 m[i]만 리턴하면 됨.
따라서 효율적인 방법이 따로 있을지 모르겠지만 일단 이런식으로 해결.
문제는 O(n)의 시간복잡도를 가져도 Time Limit에 걸린다는 점... 그냥 연습삼아 다른방법으로 해본거에 의미를 두는 복습.
'''

# Fibonacci, O(logn)
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

# Recursion with Memoization (O(n) time complexity but time limit exceeded)
'''
class Solution:
    def climbStairs(self, n: int) -> int:
        m = [0] * (n+1)
        def recursion(i):
            if i > n:
                return 0
            if i == n:
                return 1
            if m[0] > 0:
                return m[i]
            m[i] = recursion(i+1) + recursion(i+2)
            return m[i]
        return recursion(0)
'''