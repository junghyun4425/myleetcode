# Problem Link: https://leetcode.com/problems/count-numbers-with-unique-digits/

'''
문제 요약: n이 입력으로 들어올때 0 <= x < 10^n 사이에 존재하는 유니크값의 개수를 반환하는 문제.
ask: 2
answer: 91 (11, 22, 33, ... , 99 를 제외한 모든 수)

해석:
보통 이런문제는 하나씩 하는걸로 시간이 부족하기 때문에 어떤 규칙을 찾아야 함.
처음에는 유니크하지 않은 수의 패턴을 찾으려 했는데 생각한것보다 더 복잡해서 어딘가의 예외로 막힘.
반대로 현재 숫자를 계산한 것으로 패턴을 찾아보니 패턴이 쉽게 보임.
1 -> 10 -> 91 개인데, 1에서 시작해서 9를 곱하고 이전결과들을 더하면 다음 결과가 나오는것을 확인함.
이후에는 8, 7, ... 1씩 감소하면서 곱해가면 됨.
이 방식대로 하면 굉장히 간단하게 해결이 가능.
'''

class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        prev, ans = 0, 1
        for i in range(1, n+1):
            prev += ans
            ans = ans*(10-i) + prev
        return ans