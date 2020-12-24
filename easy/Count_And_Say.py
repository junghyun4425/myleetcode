# Problem Link: https://leetcode.com/problems/count-and-say/

'''
문제 요약: 주어진 숫자만큼 Count_And_Say 규칙을 재귀적으로 만들어서 문자열로 반환하는 문제.
Count_And_Say 규칙: n = 1 이면 "1"을 반환. n = 2 부턴 num,count를 문자로 반환. ex) "1" 은 1이 1개 이므로 "11" 반환.
ask: n = 4
answer: "1211"

해석:
문제를 생전 처음보는 방식이라 당황했지만, 이해하고 나면 굉장히 쉬운 문제. 재귀방식으로 간단하게 풀었으며,
다른 방법으로는 정규표현식을 활용하는 방법도 생각해 볼 수 있음.
'''

class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"

        s = self.countAndSay(n - 1)

        s_len = len(s)
        cnt, ans = 1, ''
        for i in range(1, s_len + 1):
            if i < s_len and (s[i] == s[i - 1]):
                cnt += 1
            else:
                ans += str(cnt) + str(s[i - 1])
                cnt = 1
        return ans