# Problem Link: https://leetcode.com/problems/ugly-number-ii/

'''
문제 요약: n번째 Ugly Number를 찾는 문제. (Ugly Number: 2,3,5 prime number 만으로 이루어진 값들)
ask: 10
answer: 12 (1, 2, 3, 4, 5, 6, 8, 9, 10, 12)

해석:
medium 문제 치고 난이도가 hard와 비슷한 느낌을 받은 문제. 2^n * 3^m * 5*l 식과 같이 기본을 활용할 생각없이 마구 풀었었음.
기초적인 원리를 다시 처음부터 보면, 1에서 시작해 2,3,5 로 갈림. 여기서 또 각자 2,3,5 를 곱한 트리형태의 모습을 예상할 수 있음.
여기서 주의할점은 중복 계산이 존재한다는 것. 6 = 2 * 3 = 3 * 2 와 같이 두번 계산되면 낭비.
따라서 DP방식을 활용함.
dp[i] = min(dp[pos_2] * 2, dp[pos_3] * 3, dp[pos_5] * 5)
여기서 pos이 의미하는 바는 2혹은 3혹은 5가 각각 몇번 곱셈에 참여했는지를 의미함.
dp를 통해 저장해뒀던 값들과 2 혹은 3 혹은 5를 곱해줌으로써 트리의 모든 경로를 그리고, 가장 작은값을 찾아 다음 dp[i]에 보관.
만약 값이 중복된다면 pos 을 동시에 증가시켜주면서 중복을 제거.
'''

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [1] * n
        pos = [0, 0, 0]
        for i in range(1, n):
            dp[i] = min(dp[pos[0]]*2, dp[pos[1]]*3, dp[pos[2]]*5)
            pos[0] += 1 if dp[i] % 2 == 0 else 0
            pos[1] += 1 if dp[i] % 3 == 0 else 0
            pos[2] += 1 if dp[i] % 5 == 0 else 0
        return dp[-1]