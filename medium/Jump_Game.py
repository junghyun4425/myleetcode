# Problem Link: https://leetcode.com/problems/jump-game/

'''
문제 요약: 숫자 리스트에서 숫자는 최대 움직일수 있는 거리를 의미, 끝까지 갈수 있는가에 대한 여부를 반환하는 문제.
ask: [3,2,1,0,4]
answer: False (인덱스 간격이 step이므로, 최대 움직일수 있는거리가 0인 index=3인 지점때문에 끝까지 갈수 없음)

해석:
우선 Brute Force방식이 아닌 선에서 생각해낸 아이디어는 거리가 0인 index들을 리스트에 저장.
이후에 zero_index 보다 낮은 값들에서 그 인덱스를 뛰어넘는 거리가 나오면 통과.
시간복잡도면에선 괜찮은 결과가 나오지만 역시 문제는 메모리쪽에서 O(n).
다른 저명한 아이디어(뒤에서 부터 step을 계산에 num값이 스텝을 넘어서나 안서나 확인하고 최종적으로 0인지 판단)를 공부한 후에 재코딩.
'''

# First Try with Simple Idea
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n_len = len(nums)
        zeros_i = [i for i in range(n_len - 1) if nums[i] == 0]

        for z in zeros_i:
            gt = False
            for i in range(z):
                if (nums[i] + i) > z:
                    gt = True
                    break
            if not gt:
                return False
        return True

# Second Try with Decent Idea
'''
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Second Try
        dis = 0
        for n in nums[-2::-1]:
            dis += 1
            if dis <= n:
                dis = 0
        return True if dis == 0 else False
'''