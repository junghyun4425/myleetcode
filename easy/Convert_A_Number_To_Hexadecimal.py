# Problem Link: https://leetcode.com/problems/convert-a-number-to-hexadecimal/

'''
문제 요약: 10진수 숫자가 들어오면 16진수로 바꾸는 문제.
ask: 26
answer: "1a"

해석:
파이썬 내장함수를 사용하지 않아야 하기 때문에 비트연산으로 해결하기로 결정.
우선 파이썬은 숫자의 크기 제한이 없기때문에 32bit 단위로 끊어준 다음 수행해야 함.
그리고 16진수를 구성하는 4bit씩 끊어서 치환해주면 해결.
뒤에서부터 추가했기 때문에 역순으로 바꿔줘야 하는점과, 0은 "0"으로 바로 리턴해줘야 한다는점만 주의.
'''

class Solution:
    def toHex(self, num: int) -> str:
        if num == 0: return "0"
        ans = []
        hex_val = "0123456789abcdef"
        hex_mask, num = 0xf, num & 0xffffffff
        while num != 0:
            ans.append(hex_val[num & hex_mask])
            num >>= 4
        return "".join(ans[::-1])