# Problem Link: https://leetcode.com/problems/excel-sheet-column-number/

'''
문제 요약: 1 = A, 2 = B ... 26 = Z, 27 = AA .... 규칙이 있을때 매칭시키는 문제.
ask: "ZY"
answer: 701

해석:
아스키 코드값으로 바꿔서 계산하면 간단히 풀 수 있는 문제.
문자열을 뒤에서부터 26의 제곱승을 아스키코드값의 차이만큼 곱해주면 코드변환의 결과가 나옴.
'''

class Solution:
    def titleToNumber(self, s: str) -> int:
        ans = pos = 0
        for c in s[::-1]:
            ans += (26 ** pos) * (ord(c) - ord('A') + 1)
            pos += 1
        return ans