# Problem Link: https://leetcode.com/problems/single-number-ii/

'''
문제 요약: 값이 세개씩 존재하는 숫자배열에 하나만 존재하는 값을 찾아 반환하는 문제. (단, 추가 메모리x, linear time complexity)
ask: [2,1,1,2,1,3,2]
answer: 3

해석:
우선 추가 메모리를 못쓰고 배열에 대해 Linear 한 속도를 가져야 하기때문에 대놓고 비트연산자 문제.
처음에는 각 배열의 값에 bit 자리수를 더해 3으로 나눈 나머지가 1인지 혹은 0인지로 값을 찾으려 했음.
물론 예시는 통과했지만, 음수가 나올때는 값을 못찾는 단점을 발견함. 그래서 비트 연산자들로 해결하려고 시도.
& | ~ ^ 와 같은 비트연산자로 같은 값이 3개가 나올때 0이 되는 로직을 찾아야 함.

값들을 담을 변수 first, second 를 활용.
먼저 값 x가 첫번째로 들어온 경우, first 에 담기게 해야함.
first = first ^ x = x    ->    이렇게 되면 x가 담김.
x가 두번째로 들어온 경우, second 에 담기게 해야하고 first에서 제거해야함.
second = second ^ x = x
first = first ^ x = 0
x가 세번째로 들어온 경우, first, second 둘다 제거해야함.
second = second ^ x = x

문제는 몇번째 들어왔는지 모른다는 점. 그렇기 때문에 저 계산에 first와 second를 서로 넣어줌으로써 몇번째 비교했는지 서로 알려줘야 함.
first의 경우, second에 x가 있다면 세번째의 경우이므로 0이 되고, 없다면 x가 되어야 함. 따라서,
first = (first ^ x) & ~second
        ---> x가 처음인 경우, (x^0) & (~0) = x // x가 두번째인 경우, (x^x) & (~0) = 0
second = (second ^ x) & ~first
        ---> x가 처음인 경우, (0^x) & (~x) = 0 // x가 두번째인 경우, (0^x) & (~0) = x
모든 숫자에 적용시키면 나머지 하나만 남는 값은 first에 저장되어 있으니 이걸 반환하면 끝.
'''

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        first, second = 0, 0
        for n in nums:
            first = (first^n) & (~second)
            second = (second^n) & (~first)
        return first