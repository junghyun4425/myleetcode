# Problem Link: https://leetcode.com/problems/majority-element/

'''
문제 요약: 숫자 배열에서 과반수 이상의 값을 가지는 숫자를 찾는 문제. (과반수의 수가 항상 존재한다고 가정)
ask: [3,2,3]
answer: 3

해석:
dictionary 에 값을 담아서 O(n) time, O(n) space 로 품.
dict의 key값을 value에서 카운팅 하고 가장 많이 카운팅 된 값을 반환하도록 함.
재밌게도 O(n) time, O(1) space 로 푸는 방법이 있다고 해서 찾아봄.

(Boyer-Moore Voting Algorithm)
majority 값을 찾는데 index 0 부터 차례로 올라감. 0번째가 majority라 가정하고 다른값을 만나면 -1을, 같은값을 만나면 +1을 카운팅함.
만약 카운팅이 0에서 다른값을 만난다면 majority를 빼앗기게 됨.
이런식으로 suffix 단위의 majority가 바뀌게 되고, 끝에 가서는 가장 많이 나왔던 값이 남게되는 알고리즘.
'''
# Boyer_Moore Voting Algorithm
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maj = nums[0]
        cnt = 0
        for n in nums:
            cnt += 1 if maj == n else -1
            if cnt < 0:
                maj = n
                cnt = 1
        return maj

# First Try with HashMap
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        for n in nums:
            d[n] = d.get(n, 0) + 1
        return max(d, key=d.get)