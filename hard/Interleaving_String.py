# Problem Link: https://leetcode.com/problems/interleaving-string/

'''
문제 요약: s1과 s2를 interleadving 하면 s3가 되는지 확인하는 문제. (interleaving은 s1과 s2를 순서에 맞게 섞었을때의 결과)
ask: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
answer: True (만약 s3가 "aadbbbaccc" 였다면 순서가 하나 맞지 않아서 False)

해석:
재귀 연습겸 재귀함수로 먼저 풀어봄. base case는 세가지로 s1혹은 s2, s3 의 길이가 하나라도 0이 나오는 경우.
베이스를 만날떄까지 s1과 s2중에 s3의 첫글자를 만족하는게 있는지 확인 후 재귀함수를 호출. 하지만 역시 속도문제로 시간초과.
다음으로는 DP방식을 활용. 중복되는 쓸데없는 계산을 줄이기 위해 2차원 배열의 메모리를 할당.
점화식은,
dp[i][j] = True   if i > 1 and j > 1, dp[i][j-1] == True and s2[j-1] == s3[i+j-1] or dp[i-1][j] == True and s1[i-1] == s3[i+j-1]
           True   if i == 0 and j == 0
           True   if j == 0 and dp[i-1][0] == True and s1[i-1] == s3[i-1]
           True   if i == 0 and dp[0][j-1] == True and s2[j-1] == s3[j-1]
           False  otherwise
점화식 자체는 복잡해 보이지만 실상은 간단한편. i와 j가 0인 "", "" 인 상태면 True. i 혹은 j가 0일때는 이전값이 True인지 확인하고 s3와 같은 문자면 True.
그외엔 s1인 i열과, s2인 j열 두가지 모두를 비교해야 함. s1과 s2 둘중 하나라도 연속된 문자가 s3문자와 일치한다면 True를 기록.
여기서 주의할 점은 dp는 len + 1 사이즈 이기 때문에 s1,2,3를 슬라이싱 하기 위해서 1씩 빼줘야 함.

한가지 재밌는 것을 확인.
재귀함수 성능이 느린 이유는 수많은 중복된 계산을 지속적으로 하는데에 있다는 점. 하지만 만약 캐시를 사용하게되면 계산해놓은 값을 해쉬맵에 저장하기 때문에
문제없이 시간내에 빠른속도로 결과를 얻을 수 있음.
'''

# DP
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        s1_len, s2_len, s3_len = len(s1), len(s2), len(s3)
        if s3_len != s1_len + s2_len:
            return False
        dp = [[False] * (s2_len + 1) for _ in range(s1_len + 1)]
        dp[0][0] = True
        for i in range(1, s1_len + 1):
            dp[i][0] = dp[i - 1][0] and s1[i - 1] == s3[i - 1]
        for j in range(1, s2_len + 1):
            dp[0][j] = dp[0][j - 1] and s2[j - 1] == s3[j - 1]

        for i in range(1, s1_len + 1):
            for j in range(1, s2_len + 1):
                dp[i][j] = (dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]) or \
                           (dp[i][j - 1] and s2[j - 1] == s3[i + j - 1])
        return dp[-1][-1]

# Recursion with LRU Cache
'''
from functools import lru_cache
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        @lru_cache
        def recursion(s1, s2, s3):
            if not s1:
                return s2 == s3
            elif not s2:
                return s1 == s3
            elif not s3:
                return False

            if s1[0] == s3[0] and s2[0] == s3[0]:
                return recursion(s1[1:], s2, s3[1:]) or recursion(s1, s2[1:], s3[1:])
            elif s1[0] == s3[0]:
                return recursion(s1[1:], s2, s3[1:])
            elif s2[0] == s3[0]:
                return recursion(s1, s2[1:], s3[1:])
            return False
        return recursion(s1, s2, s3)
'''