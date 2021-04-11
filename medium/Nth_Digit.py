# Problem Link: https://leetcode.com/problems/nth-digit/

'''
문제 요약: 1 2 3 .. 무한히 순차적으로 진행되는 문자열중에서 n번째 digit을 찾는 문제.
ask: n = 11
answer: 0 (10의 일부분으로 0이라는 digit값을 반환해야 함)

해석:
가장 먼저 알아봐야 할 것이 몇번째 자리수부터 시작하는지를 파악하는것.
1   ~ 9      : 9개 * 1 (첫번째 자리수의 maximum값)
10  ~ 99     : 90개 * 2
100 ~ 999    : 900개 * 3
즉, 몇번째 자리수인지 알아내고, 그만큼 n을 뺴주면 됨.

예를들어서, n = 231 이라는 값이 왔다면,
231 - 9
222 - 180
42 < 2700   까지 진행되면 3자리수부터 시작한다는것을 알수있음.
즉, 100부터 42까지 카운팅 해주면 됨.

카운팅은 42를 길이(자리수)로 나눈다음 몫을 덧셈한 위치가 결과, 만약 나머지가 0인 경우라면 몫을 1 빼준것에 마지막 위치를 의미함.
따라서 몫과 나머지를 구해 최종적으로 digit의 위치를 파악해내면 해결.
'''

class Solution:
    def findNthDigit(self, n: int) -> int:
        l = 1
        p = 9
        while n > p * l:
            n -= p * l
            l += 1
            p *= 10
        start = 10 ** (l-1)
        d, m = divmod(n, l)
        if m == 0:
            return int(str(start + d - 1)[-1])
        return int(str(start + d)[m-1])