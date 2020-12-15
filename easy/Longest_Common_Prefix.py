# Problem Link: https://leetcode.com/problems/longest-common-prefix/

'''
문제 요약: 문자열 리스트를 받아서 공통된 prefix 찾는 문제.
ask: ["flowers", "flow", "flight"]
answer: "fl"

해석:
가장 짧은 길이의 문자열을 찾아 길이를 구한 다음, 모든 문자열에서 공통된 문자를 하나씩 찾아가는 방식으로 해결.
'''


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ''
        s_len = len(strs)
        if s_len == 0:
            return ans
        s_min = min(map(len, strs))

        for i in range(s_min):
            c = strs[0][i]
            for j in range(1, s_len):
                if strs[j][i] == c:
                    continue
                else:
                    return ans
            ans += c
        return ans