# Problem Link: https://leetcode.com/problems/bulb-switcher-iii/

'''
문제 요약: 전구가 1번부터 on되어서 연결되면 파란불빛, 연결없이 하나만 on되면 노란불빛이 밝혀진다고 할때, 파란불빛이 켜지는 경우의 수를 구하는 문제.
ask: light = [2,1,3,5,4]
answer: 3 (2,1 때 blue on, 2,1,3 때 blue on, 2,1,3,5,4 때 blue on, 그외 2가지 경우는 yellow on)

해석:
brute force로 문제를 해결하면 O(n^2) 이 나오게 됨. 여기서 최적화 하는 방법은 포인터 두개를 가지고 해결이 가능.
왼쪽부터 현재 진행 순서를 나타내는 cur, 현재 켜진 마지막 전구의 위치를 end_pos 라고 할때 cur == end_pos 인경우만 blue on.
따라서 조건문을 통해 blue on인 경우를 카운팅만 해주면 해결.
'''

class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        l_len = len(light)
        cur = end_pos = 0
        cnt = 0

        for i in range(l_len):
            end_pos = max(end_pos, light[i])
            cur += 1
            if cur == end_pos:
                cnt += 1
        return cnt