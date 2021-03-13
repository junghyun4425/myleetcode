# Problem Link: https://leetcode.com/problems/majority-element-ii/

'''
문제 요약: Majority (n / 3) 보다 많은 값을 가진 숫자들을 가져오는 문제. (공간복잡도 O(1)의 제약조건)
ask: [1,2]
answer: [1,2]

해석:
제약조건이 없다면 hashmap을 활용해 굉장히 빠르게 풀수 있음.
하지만 공간제약이 있기 때문에 선택한 방법은 정렬.
정렬을 통해서 순차적으로 비교해가면서 과반수이상인 값만을 ans에 담아서 결과를 반환하도록 구현.
다른 유명한 방법으로 정렬보다 효율적으로 구현이 가능하다고 해서 다음 리뷰때는 효율적인 방법으로 구현해 보는것을 목표로 함.
'''

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        nums.sort()
        n_len = len(nums)
        maj = n_len // 3 + 1
        cnt = 1
        ans = []
        nums.append(float('inf'))
        for i in range(1, n_len+1):
            if nums[i] == nums[i-1]:
                cnt += 1
            else:
                if cnt >= maj:
                    ans.append(nums[i-1])
                cnt = 1
        return ans