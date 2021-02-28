# Problem Link: https://leetcode.com/problems/reverse-bits/

'''
문제 요약: 입력ㅇ으로 들어오는 바이너리값의 역순을 리턴하는 문제(unsigned int 라 가정)
ask: 00000010100101000001111010011100
answer: 964176192 (00111001011110000010100101000000)

해석:
비트를 하나씩 읽되, 반대로 계산해야 하기 때문에 shift연산을 31번부터 0번까지 한 결과를 더해주면 됨.
한비트씩 역순으로 값이 계산되기 때문에 정답과 일치.
'''

class Solution:
    def reverseBits(self, n: int) -> int:
        ans, pos = 0, 31
        while n:
            ans += (n&1) << pos
            n = n>>1
            pos -= 1
        return ans