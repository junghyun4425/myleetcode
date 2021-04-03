# Problem Link: https://leetcode.com/problems/shuffle-an-array/

'''
문제 요약: 동일한 확률로 순서를 바꿔서 셔플한 결과를 반환하는 클래스를 구현하는 문제.
ask:
["Solution", "shuffle", "reset", "shuffle"]
[[[1, 2, 3]], [], [], []]
answer:
[null, [3, 1, 2], [1, 2, 3], [1, 3, 2]]

해석:
순열로 공평하게 주는 방법으로 시도해봤지만 역시 순열 전체를 생성하는 작업은 비용이 너무 비쌈.
따라서 순열이 아니라 shuffle함수를 호출할때마다 섞어서 반환하기로 결정.
shuffle하는 방법으로는 각 숫자들을 배열길이의 범위로 랜던하게 하나씩 받아온다음, 하나씩 대입하기로 함.
이렇게 구현하면 O(n)의 시간복잡도를 가지며 숫자마다 균일한 확률을 보장할 수 있음.
'''

class Solution:
    def __init__(self, nums: List[int]):
        self.arr = nums
        self.origin = nums[:]

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        self.arr = self.origin[:]
        return self.arr

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        tmp = self.arr[:]
        for i in range(len(self.arr)):
            swap_i = randrange(len(tmp))
            self.arr[i] = tmp.pop(swap_i)
        return self.arr

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()