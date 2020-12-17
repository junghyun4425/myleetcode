# Problem Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/

'''
문제 요약: 정렬된 숫자 배열을 받아서 중복을 제거한 결과를 반환. (단, Space complexity 를 O(1)로)
ask: [0,0,0,1,1,2,3,4,5,5,5,6]
answer: 7, [0,1,2,3,4,5,6]

해석:
메모리를 O(1) 만큼만 사용해야 하기 때문에 다른 배열 하나를 추가로 만들 수 없음.
따라서 포인터를 두개로 만들어 이전의 값을 가리키고, 값이 달라지면 그 다음 자리에 변경된 값을 저장. (이미 정렬되었기 때문에 가능)
이렇게 하면 추가적인 배열을 따로 만들지 않아도 중복을 제거할 수 있음.
'''

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n_len = len(nums)
        if n_len < 1:
            return 0
        j = 0

        for i in range(1, n_len):
            if nums[i] != nums[j]:
                j += 1
                nums[j] = nums[i]
        return j + 1