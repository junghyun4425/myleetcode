# Problem Link: https://leetcode.com/problems/subsets-ii/

'''
문제 요약: 숫자 리스트의 power set을 리스트에 담아 반환하는 문제. (단, 중복은 제거)
ask: [1,2,2]
answer: [[],[1],[1,2],[1,2,2],[2],[2,2]]

해석:
몇가지 방법을 생각했었는데, 가장 간단한건 중복을 append()함수를 쓰기전에 검사하는 방법이 있지만, 속도가 많이 저하되므로 패스.
아니면 완전히 리스트를 튜플로 만들어 set에 넣어서 성능을 향상시키는 방법이 있지만, 이 문제의 의도하는 방안이 아닌것 같아 패스.
그래서 재귀로 중복을 만날땐 넘기는 방식으로 시도.
여기서 조심해야할 것은, 중복된 숫자를 만나도 무시하면 안되는 경우가 발생. ([1,2,2] 에서 중복된 숫자 2는 추가해줘야 함)
고로, 재귀함수 인자로 rest of nums(rest) 를 넘겨받아 필요한 중복은 append() 가 수행되도록 구현.
'''

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        def recursion(cur, rest):
            ans.append(cur)
            for i in range(len(rest)):
                if i > 0 and rest[i] == rest[i-1]:
                    continue
                recursion(cur+[rest[i]], rest[i+1:])

        recursion([], nums)
        return ans