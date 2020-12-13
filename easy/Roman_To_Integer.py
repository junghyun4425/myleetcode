# Problem Link: https://leetcode.com/problems/roman-to-integer/

'''
문제 요약: 문자열 로마숫자를 받아 정수로 바꿔주는 문제.
ask: VIII
answer: 8

해석:
9와 4 같은 까다로운 부분을 숫자로 바꿔줘야 할 때가 있기 때문에 pre_val 값으로 이전의 값을 저장한 다음 비교해서 값을 구함.
간단한 해시맵을 활용하여 깔끔하게 구현.
'''

class Solution:
    def romanToInt(self, s: str) -> int:
        m = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        pre_val = m[s[0]]
        ans = pre_val

        for c in s[1:]:
            val = m[c]
            if pre_val >= val:
                ans += val
            else:
                ans += val - (2 * pre_val)
            pre_val = val
        return ans