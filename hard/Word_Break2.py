# Problem Link: https://leetcode.com/problems/word-break-ii/

'''
문제 요약: 문자열 s가 wordDict에 나열된 문자들로부터 만들어 지는 모든 경우를 반환하는 문제.
ask: s = "catsanddog", wordDict = ["cats", "dog", "sand", "and", "cat"]
answer:
[
  "cats and dog",
  "cat sand dog"
]

해석:
이전과 Word_Break 문제와 마찬가지로 DP방식을 사용하지만 전혀 다른 방법으로 구현해야 함.
이전에는 s의 길이에 대응하는 문자가 있다면 True를 저장하는 dp를 사용했다면, 이번엔 글자자체에 존재하는 모든 나눌수 있는 방법을 저장해야함.
이를 위해 dp를 해쉬맵과 유사한 dictionary를 사용. key값은 string의 일부분을, value값은 string에서 만들수 있는 모든 경우를 저장.
모두 문자라 점화식을 정확히 세우기 애매하지만 수도코드 같은 느낌으로 세워보자면,

dp[s] = {s: [dp[w1],dp[w2],...}     if (w1 + w2) == s, w is in wordDict

중복계산을 피하고, 경우의 수도 모두 저장하기때문에 Backtracking 방식으로 뒤로 가면서 문자들을 조합하기만 하면 끝.
'''

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordSet = set(wordDict)
        dp = {}
        def backtracking(s):
            ans = []
            if s in dp: return dp[s]
            for w in wordSet:
                w_len = len(w)
                if s[:w_len] == w:
                    if w_len == len(s):
                        ans.append(w)
                    else:
                        before_words = backtracking(s[w_len:])
                        for w2 in before_words:
                            ans.append(w + " " + w2)
            dp[s] = ans
            return ans
        return backtracking(s)