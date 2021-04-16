# Problem Link: https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

'''
문제 요약: 1부터 n까지의 숫자 중에서 배열에 없는 숫자들을 반환하는 문제. (Follow up: O(1) 공간복잡도를 만족하게끔 설계)
ask: nums = [4,3,2,7,8,2,3,1]
answer: [5,6]

해석:
추가 메모리를 사용할 수 있다면 쉽게 풀림. (n의 배열을 체크하거나, 해쉬맵으로 저장하는 방식 등등)
하지만 추가메모리를 사용할수 없기 때문에 스왑을 통해 정렬의 효과를 내는 방법으로 해결함.
배열이 1부터 시작하는걸 알기 때문에, 인덱스 0을 1의 자리라고 가정을 함.
그렇다면 1부터 n까지의 자리가 되겠고, 인덱스 + 1이 배열의 값으로 들어오게끔 정렬비슷한 방식으로 구현.
인덱스 0 부터 끝까지 올바른 자리에 위치하도록 스왑을 진행함.
이로인해 추가 메모리를 쓰지않고도 Linear한 시간에 수행을 완료하게 됨.
'''

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            while nums[nums[i]-1] != nums[i]:
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
        return [i+1 for i, n in enumerate(nums) if n != i + 1]