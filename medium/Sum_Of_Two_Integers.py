# Problem Link: https://leetcode.com/problems/sum-of-two-integers/

'''
문제 요약: 두 숫자를 + 혹은 - 연산자를 사용하지 않고 더하는 문제.
ask: a = 3, b = 2
answer: 5

해석:
문제를 보자마자 비트연산자로 쉽게 해결이 가능하다고 생각했지만 다른의미로 굉장히 어려웠던 문제.
우선 해결방법을 먼저 설명하고 마주친 문제점을 설명하도록 함.
XOR 연산자로 두 수의 서로 다른 비트를 찾을 수 있고, AND 연산자로 carry를 찾을 수 있음.
즉, XOR한 결과에 carry << 1 한 결과를 또 XOR하고 다시 AND로 carry를 찾고 반복하면 됨.
carry가 0인 경우 더이상 XOR연산할 필요가 없기떄문에 반복문을 빠져나오면 결과가 나옴.

마주친 문제: python의 integer는 32bit로 고정되지 않음.
파이썬3에서는 arbitrary precision이라는 방법으로 integer의 크기를 동적으로 할당함. (overflow가 없다는 장점이 있음)
즉, 숫자의 크기에 따라 할당된 사이즈가 점점 커진다는것을 의미.
문제에서 요구하는 32bit integer를 만족하기 위해선 범위를 제한할 필요가 있었기에 mask로 32bit를 제한해줘야함.
하나 더, 양수와 음수의 범위까지 설정해줘야 하기때문에 생각보다 굉장히 복잡한 문제가 되어버림.
가장 큰 문제는 a혹은 b가 음수일때. 따라서 음수의 경우 mask로 사이즈를 제한해주는게 필수.
또한, 결과값이 positive_max를 넘는다면 음수가 결과기 때문에 32bit에 맞는 보수를 구해줌으로써 음수로 바꿈.
32bit가 넘는 값에 대해선 어차피 문제에서 integer 32bit 이상은 쓰이지 않기때문에 잘라내도 상관없음.
'''

class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0b11111111111111111111111111111111
        positive_max = 0b01111111111111111111111111111111
        while b != 0:
            ans = (a ^ b) & mask
            carry = ((a & b) << 1) & mask
            a = ans
            b = carry
        return a if a <= positive_max else ~(a ^ mask)