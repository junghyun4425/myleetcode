# Problem Link: https://leetcode.com/problems/add-binary/

'''
문제 요약: 이진수를 문자열로 두개 받아서 둘을 더한값을 반환하는 문제.
ask: a = "101", b = "1"
answer: "110"

해석:
int(a, 2) 와같이 이진수로 바꾸고 계산해서 반환하는 간단한 방법은 아마 의도하는바는 아니라 생각.
a와 b를 더한다음 str로 변환시켜서 이진수를 만들기로 결정.
이진수 이진수를 더하면 최댓값이 2이며, 이전의 자리에서 올림이 있는지 없는지 판단하며 계산.
'''

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ans = ''
        dec = str(int(a) + int(b))
        lift = False
        for i in dec[-1::-1]:
            if i == '0' or (i == '1' and not lift):
                ans += '1' if lift else i
                lift = False
            else:
                ans += '1' if lift and i == '2' else '0'
                lift = True
        if lift:
            ans += '1'
        return ans[-1::-1]