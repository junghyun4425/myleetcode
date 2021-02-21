# Problem Link: https://leetcode.com/problems/largest-number/

'''
문제 요약: 숫자 배열이 들어올때, 가장 큰값으로 만들 수 있는 조합을 str 형태로 반환하는 문제.
ask: [3,30,34,5,9]
answer: "9534330"

해석:
언뜻 보면 내림차순 정렬해서 str으로 붙여주면 될거같지만 한가지 틀린점이 있음. 자리수가 다르면 원하는 순서에서 예외의 경우가 나옴.
3과 30 을 비교해보면 330 vs 303 와 같이 30이 더 낮은 수로 나와야 함.
따라서, 일반적인 정렬로는 해결할 수 없고, 정렬 key function을 따로 정의해줘야 함.

이때 고려해볼 수 있는 방법은 sorted() 함수이며, 이는 기본적으로 __lt__() 매직매소드를 통해 정렬을 보장한다는 사실.
따라서 string 객체를 부모로 해서 str값을 받아온 다음 x+y 와 y+x 의 Less_Then 매직메소드를 정의해주면 끝.
내림차순이기에 reverse옵션을 True로 주고 마지막에 합침.
[0, 0] 과 같은 케이스는 "00" 이 되기 때문에 이부분만 따로 처리해주면 됨.
'''

class StringCompare(str):
    def __lt__(x,y):
        return x+y < y+x
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        ans = "".join(sorted(map(str, nums), key=StringCompare, reverse=True))
        return ans if ans[0] != "0" else "0"