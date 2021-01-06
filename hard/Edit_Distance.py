# Problem Link: https://leetcode.com/problems/edit-distance/

'''
문제 요약: 단어 2개를 단어1 에서 단어2 로 바꾸는데 드는 최소 비용을 반환하는 문제. (비용은 각각 char를 replace, remove, insert 하는데 1씩)
ask: word1 = "horse", word2 = "ros"
answer: 3 (horse -> rorse -> rors -> ros)

해석:
처음은 문제의 예시만 보고 단어를 어떻게 최소로 바꿀수 있는지만 고민. (horse에서 ros로 가는 최소비용이 한두개가 아니기 때문에 말도안되는 느린 속도를 예상)
하지만 이또한 쉽지 않았고, 여러 방법을 생각해봤으나 잘 안풀림...
그러다 문제를 보고 distance 라는 단어에 하나를 깨우침. 단어를 바꾸려고 할 필요없이 그저 두개의 단어간 차이점만 계산하면 되는문제.
그제서야 DP로 문제푸는 방법을 생각해내고 생각보다 어렵지않게 풀림.
점화식은,
dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])   / otherwise
         = dp[i-1][j-1]                                / if word1[i] == word2[j]
i = word1's range (word1[:i])
j = word2's range (word2[:j])
'''

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        w1_len, w2_len = len(word1), len(word2)
        dp = [[0] * (w2_len + 1) for _ in range(w1_len + 1)]
        for i in range(w1_len + 1):
            dp[i][0] = i
        for j in range(w2_len + 1):
            dp[0][j] = j

        for i in range(1, w1_len + 1):
            for j in range(1, w2_len + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
        return dp[-1][-1]