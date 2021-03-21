# Problem Link: https://leetcode.com/problems/power-of-three/

'''
문제 요약: 3의 제곱승인지 확인하는 문제.
ask: 27
answer: True

해석:
Follow-up 으로 loop를 사용하지 않고 하는 방법이 있다고 해서, 이쪽으로 시도를 해봄.
일단 loop를 돌면 시간복잡도는 O(log_3N) 으로 느린속도를 가지는편은 아님.
loop를 사용하지 않고 하는방법은 내가 생각했을때 두가지로, bit연산 혹은 수학이론을 적용.
처음엔 bit연산으로 시도해보려 했으나 특정 규칙도 없고 뭘 해봐도 해결이 어려움.
따라서 수학적 방법으로 접근을 시도했으며, log_3N을 바꾸는 방법을 통해 해결함.
입력값 n이 log3n 인 경우 정수값이 됨. 이는,
log3(n) = log10(n) / log10(3)
로 표현이 가능하므로, math를 활용해 값을 구한다음 소수점이 없는지 확인하면 해결.
'''

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0: return False
        return (math.log10(n) / math.log10(3)) % 1 == 0