# Problem Link: https://leetcode.com/problems/random-pick-index/

'''
문제 요약: 입력값에 대해 특정값의 랜덤한 index를 반환하는 클래스를 구현하는 문제.
ask:
["Solution", "pick", "pick", "pick"]
[[[1, 2, 3, 3, 3]], [3], [1], [3]]
answer:
[null, 4, 0, 2]

해석:
입력값으로 중복된 값들이 들어오게 되면, 해쉬맵에 인덱스들을 캐싱한 다음 랜덤한 값을 반환.
캐싱하면 굉장히 쉬워지는데 캐싱하지 않고 해결되는 방법이 있다고 함.
따라서 다음에 복습하게 되면 캐싱하지 않고 해결하는 방법으로 시도해볼 것.
'''

class Solution:
    def __init__(self, nums: List[int]):
        self.hm = defaultdict(list)
        for i, n in enumerate(nums):
            self.hm[n].append(i)

    def pick(self, target: int) -> int:
        return choice(self.hm[target])


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)