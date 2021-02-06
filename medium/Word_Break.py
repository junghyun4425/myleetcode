# Problem Link: https://leetcode.com/problems/word-break/

'''
문제 요약: 문자열 s가 wordDict에 나열된 문자들로부터 만들어 질 수 있는지 확인하는 문제.
ask: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
answer: False

해석:
간단한 재귀함수로 풀려면 시간이 걸릴거라 예상했기 때문에 바로 불필요한 연산을 줄여줄 수 있는 DP방식으로 구현.
아직 DP에 익숙하지 않다고 느꼈는데, 그 이유는 끝점(i)만 가지고 문제를 해결하려다 시간을 엄청 날렸다는 점...
사실 O(n)으로 풀수 있지 않을까 하는 희망에 많은 시간을 허비했지만 아무리 생각해도 해결점을 찾지 못함.
나중에서야 시작점(j)를 넣으면 쉽게 풀린다는걸 깨달았지만 아직 DP는 부족한것 같으므로 연습을 더 해야함.
점화식을 간단히 표현하자면,
dp[i] = True        if dp[j] == True, s[j:i] in wordDict (j < i)
      = False       otherwise
'''

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        s_len = len(s)
        dp = [False] * (s_len+1)
        dp[0] = True
        wordSet = set(wordDict)
        for i in range(s_len+1):
            for j in range(i):
                if dp[j] and s[j:i] in wordSet:
                    dp[i] = True
                    break
        return dp[-1]