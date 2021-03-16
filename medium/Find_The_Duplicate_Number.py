# Problem Link: https://leetcode.com/problems/find-the-duplicate-number/

'''
문제 요약: 숫자열에 하나만 중복된값이 있고 나머진 유니크한 값. 값의 범위는 배열의 길이보다 작을때 중복된 값을 찾는 문제.
ask: [1,3,4,2,2]
answer: 2

해석:
정렬로 푸는 방법은 시간, 공간 복잡도가 각각 O(nlogn), O(1) or O(n).
set혹은 hashmap으로 푸는 방법은 O(n), O(n)
이 문제에서는 O(n), O(1) 을 만족하기를 원하기 때문에 일반적인 방법으로는 해결이 불가능.
배열안에 있는 값은 '배열의 길이보다 작다' 를 활용해야 해결이 가능.
이전에 풀었던 Linked List에서 Cycle의 진입점을 찾는 방안을 봐야 함. 즉, 저 숫자는 링크드 리스트의 next값이라고 생각.
그럼 자연스레 값이 여러개있는게 존재하기 떄문에 cycle이 생길것이고 Floyd's cycle법칙을 적용하면 해결이 가능.

x가 시작점부터 cycle진입지점 까지, y가 cycle지점으로부터 만난지점 까지, z가 만난지점부터 cycle까지 남은거리 라고 가정했을때,
먼저 meeting position을 찾음. fast 경로: (x + y + z) + x + y /// slow 경로: x + y
2배 빠른 fast와 거리가 같아지려면 fast = 2 * slow
즉, x = z 가 성립함.
따라서 slow가 처음부터 시작해서 다시 만나는지점이 cycle이 시작되는 지점. 그 값을 리턴하면 끝.
'''

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast = slow = nums[0]
        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]
            if fast == slow:
                break
        fast = nums[0]
        while fast != slow:
            fast = nums[fast]
            slow = nums[slow]
        return fast