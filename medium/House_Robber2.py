# Problem Link: https://leetcode.com/problems/house-robber-ii/

'''
문제 요약: 재산이 나열된 집이 있고, 도둑이 최대로 훔칠 수 있는 금액을 반환하는 문제. (연속된 집을 훔치면 경비에 걸리게 됨)
        추가로 첫번째 집과 마지막 집은 연결되어 있다고 가정.
ask: [2,7,9,3,1]
answer: 11 (2 + 9)

해석:
이전 House_Robber 문제와 굉장히 유사하지만 한가지 조건이 추가됨. 첫째집과 마지막집은 연결되어 있다는 조건.
기존의 DP방법에서 아무리 생각해봐도 적당한 DP 솔루션이 떠오르지 않음. 막힌 원인이 첫번째집을 훔쳤는지 안훔쳤는지에 대한 정보를 저장하기 힘듦.
왜냐하면 DP 솔루션이기에 예전에 첫번째 집을 훔쳤는지에 대한 정보를 보장하지 못하기 때문.
고로 생각해낸 방안이 그냥 마지막집을 뺀 결과와 첫번째집을 뺀 결과를 동시에 구해서 둘중 큰값을 반환하기로 함. 어차피 O(n)의 속도임은 마찬가지.

기존의 솔루션은 DP 배열을 썼지만 이번에는 포인터 2개를 가지고 해결.
또한, 두번 for loop를 돌려야 하기 때문에 함수화해서 코드의 중복을 막음.
결과적으로 굉장히 심플하게 문제를 해결함. (max 앞에 nums[0]을 넣어준 이유는 nums길이가 1인 경우를 대비하기 위함)
'''

class Solution:
    def rob(self, nums: List[int]) -> int:
        def acyclic_rob(nums):
            pre1, pre2 = 0, 0
            for n in nums:
                new_pre = max(pre1+n, pre2)
                pre1 = pre2
                pre2 = new_pre
            return pre2
        return max(nums[0], acyclic_rob(nums[1:]), acyclic_rob(nums[:-1]))