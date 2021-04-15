# Problem Link: https://leetcode.com/problems/add-strings/

'''
문제 요약: 숫자로만 구성된 문자열 두개를 더하는 문제. (숫자와 문자를 서로 바꾸는 내장함수를 사용하지 않기)
ask: num1 = "11", num2 = "123"
answer: "134"

해석:
뒷자리 숫자 부터 하나씩 더해가면서 배열에 숫자들을 추가해주면 됨.
올림을 의미하는 carry를 통해 올려주는 값이 있는지 체크하고, 아스키코드를 이용해 문자열을 숫자로 바꿔줌.
마지막에 carry만 확인해주고 나머지는 한자리수 씩 계산해나가면 해결.
'''

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        ans = []
        carry = 0
        n1, n2 = len(num1) - 1, len(num2) - 1
        while n1 >= 0 or n2 >= 0:
            i = ord(num1[n1]) - ord('0') if n1 >= 0 else 0
            j = ord(num2[n2]) - ord('0') if n2 >= 0 else 0
            v = (i + j + carry) % 10
            carry = (i + j + carry) // 10
            ans.append(v)
            n1 -= 1
            n2 -= 1
        if carry:
            ans.append(carry)
        return ''.join(str(n) for n in ans[::-1])