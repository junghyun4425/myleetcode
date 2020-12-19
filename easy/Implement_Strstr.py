# Problem Link: https://leetcode.com/problems/implement-strstr/

'''
문제 요약: 문자열 두개를 받고, 두번째 문자열이 첫번째 문자열에 속한다면 index를 반환하는 문제. 없다면 -1을 반환.
ask: "hello", "ll"
answer: output = 2

해석:
for문을 돌면서 두번째 문자열이 첫번째 문자열에 속해있는지 검사해서 문제를 해결.
'''

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        ans = -1
        h_len = len(haystack)
        n_len = len(needle)
        if n_len == 0:
            return 0
        for i in range(h_len):
            if i + n_len <= h_len and haystack[i:i+n_len] == needle:
                return i
        return ans