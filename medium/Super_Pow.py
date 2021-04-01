# Problem Link: https://leetcode.com/problems/super-pow/

'''
문제 요약: a 의 b 제곱승의 결과를 1337 로 나눈 나머지를 구하는 문제. (b는 숫자로 이루어진 배열로 들어옴)
ask: a = 2147483647, b = [2,0,0]
answer: 1198

해석:
문제를 보자마자 어떤 수학공식에 의해 저 계산을 피하고 알수있는 방법이 있다는걸 직관적으로 알게됨.
제곱승을 계산하지 않고도 mod값을 알수 있는 방법을 고민해봤지만 알아내긴 어려워서 결국 인터넷을 찾아보게 됨.
결론부터 말하자면 오일러공식과 Fermat's Theorem을 통해 해결가능함.
Fermat이론에 의해 phi함수를 구할수 있음. 이는 a가 어떤 exp값에 의해 나누어떨어지지 않을때 1을 뺀 값이 phi의 결과.
phi(1337) = phi(7) * phi(191) = 7-1 * 191-1 = 1140 (7과 191은 prime number 이므로 가능함)
그리고 오일러 공식을 통해,
Goal = (a ^ exp) mod 1337
     = a ^ (exp mod phi(1337)) mod 1337
     = a ^ (exp mod 1140) mod 1337
물론 공식이 아니라 내가 생각해내지 못한 획기적인 방법이 있으리라 생각됨.
제곱근을 어떤식으로 쪼개서 활용하면 될거같긴 한데 다음에 시간이 많다면 연구해보는것도 좋을 듯.
'''

class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        return pow(a % 1337, int(''.join(map(str, b))) % 1140) % 1337