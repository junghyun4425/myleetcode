# Problem Link: https://leetcode.com/problems/excel-sheet-column-title/

'''
문제 요약: 1 = A, 2 = B ... 26 = Z, 27 = AA .... 규칙이 있을때 매칭시키는 문제.
ask: 701
answer: "ZY"

해석:
크게 두가지 방법으로 고민했던 문제.
첫번째는 dict 에 매칭값을 저장해서 편하게 계산하는 방법.
두번째는 n값을 26으로 나눠가면서 문자를 더해가는 방법.
첫번째 경우는 굉장히 간편하게 구현할 수 있지만 메모리 효율이 떨어지기 때문에 두번째 방법으로 해결.
두번째에서 주의할 점은 0과 매칭되는 경우가 없다는 것. 따라서 나눈 나머지가 0일 경우 26으로 바꿔주고 n값을 1 감소시켜줘야 함.
그 외에는 아스키코드만 알고있다면 간단하게 해결되는 문제.
'''

class Solution:
    def convertToTitle(self, n: int) -> str:
        ans = ""
        while n > 0:
            remainder = n % 26
            n //= 26
            if remainder == 0:
                remainder = 26
                n -= 1
            ans = chr(ord('A') + (remainder - 1)) + ans
        return ans