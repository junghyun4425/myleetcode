# Problem Link: https://leetcode.com/problems/remove-duplicate-letters/

'''
문제 요약: 입력으로 들어오는 문자열의 중복된 철자를 제거하는 문제. (단, 모든 가능한 경우의 수에서 최대한 사전순 정렬되게 결과를 반환)
ask: "cbacdcbc"
answer: "acdb"

해석:
중복을 제거하는것 자체는 해쉬맵을 사용하면 O(n)의 시간복잡도로 쉽게 해결이 가능함.
여기서는 한가지 제약조건이 주어졌는데, 모든 경우의 수 중에서 사전순으로 정렬.
절대적인 정렬이 아닌게 오히려 고민을 많이하게되었는데, 모든 경우의 수를 만들기에는 너무 좋지않은 성능을 야기할 것임이 분명함.
생각해낸 아이디어가 stack을 활용해서 정답을 하나씩 쌓아올리는 방법.
hashmap에 모든 철자를 카운팅해놓고 1이상이면 순서에 안맞을때 지워질 수 있도록 구현.
즉, 더 큰 character를 만나면 append()하기 전까지 stack을 pop() 한다는 의미.
사실 처음엔 이게 100% 통과될지 의구심이 들었는데, 이런 방법으로 해결이 됨.
'''

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        hm = collections.Counter(s)
        ans = []
        for c in s:
            hm[c] -= 1
            if c not in ans:
                while ans and hm[ans[-1]] > 0 and c < ans[-1]:
                    ans.pop()
                ans.append(c)
        return ''.join(ans)