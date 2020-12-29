# Problem Link: https://leetcode.com/problems/multiply-strings/

'''
문제 요약: 두개의 숫자로 이뤄진 문자열 두개를 곱한 결과를 반환 (단, str -> Int 직접적으로 사용 불가능, BigInteger 내장함수x)
ask: "123", "456"
answer: "56088"

해석:
숫자로 이뤄진 문자열을 다이렉트로 바꿀 수 없기 때문에 아스키코드를 활용해 숫자로 바꿔서 변환.
아스키로 숫자를 받아온다음, 자리수에 맞게 10을 곱해주어 값을 구하고 반환.
'''

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        def get_int(n):
            n_len = len(n)
            ans = 0
            for i, n_str in enumerate(n):
                n_int = ord(n_str) - ord("0")
                ans += n_int * (10 ** (n_len - i - 1))
            return ans
        return str(get_int(num1) * get_int(num2))