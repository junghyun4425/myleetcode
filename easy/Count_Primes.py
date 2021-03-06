# Problem Link: https://leetcode.com/problems/count-primes/

'''
문제 요약: n이 주어졌을때 n미만의 숫자에 소수 개수를 구하는 문제.
ask: 10
answer: 4 (2,3,5,7)

해석:
이 문제가 easy라는게 의심이 갈 정도로 힘들었던 문제. 일단 Brute Force방식으로 해결하려하면 Time Limit Exceeded.
따라서 추가적으로 메모리를 써서 속도를 늘리는법을 생각해봄.
0과 1은 소수가 아니기에 넘어가고, 2부터 n이하의 숫자에 2의 배수를 제거해줌.
그리고 3의 배수도 제거하면 10 이하에는 5,7 이 남음.
여기서 주의해야할 점은 2,3제거한다고 모든 수가 소수가 되는게 아니라, 5와 7에 대해서도 5*5 7*7 은 소수가 아님.
따라서 n의 제곱근 만큼만 제거법을 시행해 주면 소수를 제외한 모든 숫자가 제거될것임.
'''

class Solution:
    def countPrimes(self, n: int) -> int:
        prime = [True] * n
        for i in range(2, int(n**0.5)+1):
            if prime[i]:
                j = 2
                while j*i < n:
                    prime[j*i] = False
                    j += 1
        cnt = 0
        for i in range(2, n):
            cnt += 1 if prime[i] else 0
        return cnt