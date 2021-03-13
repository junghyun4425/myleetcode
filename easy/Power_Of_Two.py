# Problem Link: https://leetcode.com/problems/power-of-two/

'''
문제 요약: 2의 제곱승이 되는지 확인하는 문제. (제약조건으로 for loop 없이 해결)
ask: 5
answer: False

해석:
제역조건이 없어도 문제를 통과하는데 문제없기 때문에 easy로 잡은것 같음.
제약조건 떄문에 easy보다는 난이도가 살짝 올라간다고 생각. 이를 해결하기 위해선 bitwise를 깊게 이해하고 있어야 함.
한가지 bit연산의 원리를 이해해야 할게 있는데 x의 음수 -x는 bit연산에서 x의 보수에 1bit를 더한 결과와 같음.
증명하자면,
x + (-x) = 0000
x + (-x) = 1111 0000 (bit자리수 앞은 어떤 숫자던지 잘라내는 컴퓨터의 특성 때문)
x + (-x) = 1111 + 0001 (저 둘을 더하면 0000 과 같기 때문에 식이 성립함)
x + (-x) = x + complement(x) + 0001
-x = complement(x) + 0001
여기서 한가지 더 알아둬야 하는것은 보수에 0001을 더한값이 -x기 때문에 2의 제곱수는 x와 같음.
16을 예로들면,
x = 10000
-x = 01111 + 00001 = 10000
따라서 x & -x == x 이면 2의 제곱수가 됨.
주의해야할 점은 0인 경우도 위의 경우에 해당되기 때문에 따로 조건문으로 걸러야 함.
'''

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0: return False
        return n & (-n) == n