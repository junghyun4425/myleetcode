# Problem Link: https://leetcode.com/problems/single-number-iii/

'''
문제 요약: 배열에 하나만 존재하는 값이 2개가 있을때, 이 둘을 반환하는 문제.
ask: [1,2,1,3,2,5]
answer: [3,5]

해석:
공간복잡도를 O(1)로 하고싶다면 정렬을, 시간복잡도를 linear하게 하고싶다면 hashmap을 활용하면 되는 문제.
둘다 O(1), Linear 하게 풀수있는 방법은 아마 비트연산을 하면 가능하지 싶음. (두개의 변수에 담아서 xor연산을 잘섞으면 될듯함)
시간이 굉장히 오래걸릴것 같아 일단 해쉬맵으로 풀고 넘어가고, 시간이 된다면 비트연산으로 풀어보는 걸로.
'''

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        hm = defaultdict(int)
        for n in nums:
            hm[n] += 1
        return [k for k, v in hm.items() if v == 1]