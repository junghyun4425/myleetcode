# Problem Link: https://leetcode.com/problems/valid-perfect-square/

'''
문제 요약: 입력으로 오는 숫자가 완전한 제곱근의 숫자인지 확인하는 문제.
ask: 16
answer: True

해석:
제곱근을 loop로 푸는방법과 제곱을 활용해 해결하는 방법 두가지가 있음.
우선 loop로 풀어보면 i*i <= num 일때까지 수행되기 때문에 logn 의 시간복잡도를 가짐.
제곱을 활용하면 루프문을 돌지 않기때문에 상수 시간복잡도를 가짐.
따라서 성능이 뛰어난 제곱을 활용해 문제를 해결함.
'''

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # Using square
        return int(num ** 0.5) == num ** 0.5

        # Using loop
        '''
        i = 1
        while i*i <= num:
            if i*i == num:
                return True
            i += 1
        return False
        '''