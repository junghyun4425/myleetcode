# Problem Link: https://leetcode.com/problems/happy-number/

'''
문제 요약: 숫자를 각 자리수의 제곱한 값의 합이 1이 되면 Happy number. 해피넘버인지 아닌지 판단하는 문제.
ask: 19
answer: True (19 -> 82 -> 68 -> 100 -> 1)

해석:
입력으로 들어오는 수를 문자로 바꾼다음 한자리수씩 제곱해서 더하게 됨. (10으로 나눈 나머지를 제곱하는 방법도 있음)
중요한점은 1이 나오지 않을경우 cycle이 생성될 수 있다는 점.
따라서 set을 통해 사이클이 발생할 경우 False를 반환하고 종료하도록 함.
'''

class Solution:
    def isHappy(self, n: int) -> bool:
        s = set([n])
        while n != 1:
            total = 0
            for i in str(n):
                total += int(i) ** 2
            if total in s:
                return False
            s.add(total)
            n = total
        return True