# Problem Link: https://leetcode.com/problems/is-subsequence/

'''
문제 요약: s가 t의 subsequence를 만족하는지 확인하는 문제.
ask: s = "abc", t = "ahbgdc"
answer: True

해석:
subsequence를 만족하기 위한 조건으로,
1) 모든 s의 철자가 t에 존재해야 함.
2) s의 철자가 순서대로 t에 존재해야 함.
따라서 포인터 두개를 가지고 해결이 가능한 문제.
s의 idx를 의미하는 포인터와 t를 가리키는 포인터 두개를 비교해가며 진행하면 해결.
'''

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0: return True
        idx = 0
        for c in t:
            if c == s[idx]:
                idx += 1
            if idx == len(s):
                return True
        return False