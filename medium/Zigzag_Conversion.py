# Problem Link: https://leetcode.com/problems/zigzag-conversion/

'''
문제 요약: 문자열을 지그재그 순서로 재배열 지그재그 길이는 정수로 주어짐.
ask: s = "PAYPALISHIRING", numRows = 3
answer: "PAHNAPLSIIGYIR"

해석:
지그재그가 생각보다 쉬운 패턴은 아니라는 점에서 시간을 많이 낭비함. 처음엔 규칙을 찾아서 numRows * 2 - 2 패턴으로 왕복됨을 확인.
하지 식이 생각보다 복잡해서, 간단하게 trigger를 이용해 0 ~ numRows-1 까지 1씩 감가산 연산으로 동작하게 함.

Review
복습겸 이전에 풀었던 트리거를 활용한 방식으로 풀어봤고, 뭔가 패턴이 있을거 같아서 찾아봤지만 감이 안잡힘.
결국 어떤 패턴이 존재하는지 찾아봤고, 생각보다 많이 복잡한 식으로 이루어짐. 혹시나 나중에 관심이 생긴다면 패턴을 구해서 풀어보는것으로...
새로 풀어본 방식과 이전의 방식은 유사해서 따로 코드를 올리진 않음.
'''

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        zz_list = [[] for _ in range(numRows)]
        c_row, trigger = 0, False

        for c in s:
            zz_list[c_row].append(c)
            if c_row == 0 or c_row == (numRows - 1):
                trigger = False if trigger else True
            if trigger:
                c_row += 1
            else:
                c_row -= 1
        return ''.join([''.join(arr) for arr in zz_list])