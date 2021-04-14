# Problem Link: https://leetcode.com/problems/fizz-buzz/

'''
문제 요약: 3의 배수는 "Fizz", 5의 배수는 "Buzz", 15의 배수는 "FizzBuzz", 나머지는 숫자의 문자형태로 나열하는 문제.
ask: n = 5
answer: ["1","2","Fizz","4","Buzz"]

해석:
15의 배수이면 Fizz와 Buzz가 합쳐져있기 때문에 string 합연산으로 쉽게 해결할 수 있음.
해쉬맵에 비교해야할 연산들을 담아두고, n까지 비교하면서 나누어떨어지는것이 있는지 확인.
해쉬맵 키에 나누어떨어지는것이 없다면 숫자를 넣어야하니 인덱스번호를 문자로 바꾼다음 추가하면 해결.
'''

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = []
        hm = {3: "Fizz", 5: "Buzz"}
        for i in range(1, n+1):
            s = ""
            for k in hm.keys():
                if i % k == 0:
                    s += hm[k]
            if s == "":
                s = str(i)
            ans.append(s)
        return ans