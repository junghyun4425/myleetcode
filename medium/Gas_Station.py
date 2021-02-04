# Problem Link: https://leetcode.com/problems/gas-station/

'''
문제 요약: Gas station에서 채울수 있는 가스량과 다음으로 이동할때 드는 비용 배열로 한바퀴 돌수 있는 시작시점을 반환하는 문제.
ask: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
answer: 3 (3에서 출발하면 cost가 부족하지 않고 모든 스테이션을 들릴수 있음)

해석:
첫번째 시도에서는 일단 빠르게 풀어보기로 결정. total 이라는 배열에 gas - cost 한 결과들을 모아놓음.
i가 시작지점이고 j는 한바퀴 돌수 있는지 체크하는 for루프. 모든 시작지점에서 한바퀴 돌수 있는지 확인.
possible이 만약 0보다 작으면 진행하고 끝지점 j가 끝까지 무사히 도착하면 i를 반환함. 리턴을 못했을땐 답이 없으니 -1을 반환.

두번째 시도는 첫번째 시도를 optimization 한 결과.
1. total 배열은 사실 메모리만 차지함. 필요할때 계산하면 되기 때문에 제거.
2. 쓸모없는 조건문 삭제. possible < 0 하나로 가스가 부족한지 아닌지 판단이 가능.
3. 시작지점 i 를 travel에 실패한 지점에서 시작할 수 있도록 설계. i += j + 1. 왜냐면 도중에 여행 실패했다면 또 거기서 막힐테니 넘어가 줌.

위의 최적화를 통해 시간복잡도 O(n^2) 에서 O(n) 으로, 공간복잡도 O(n) 에서 O(1) 로 성공적으로 변형.
결과적으로 100배정도 빠른 성능을 얻어냄.
'''

# Second Try (Optimized)
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        g_len = len(gas)
        i = 0
        while i < g_len:
            possible = 0
            j = 0
            while j < g_len:
                cur = (i+j) % g_len
                possible += gas[cur] - cost[cur]
                if possible < 0:
                     break
                j += 1
                if j == g_len:
                    return i
            i += j + 1
        return -1

# First Try
'''
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        g_len = len(gas)
        total = [gas[i] - cost[i] for i in range(g_len)]
        for i in range(g_len):
            possible = 0
            if total[i] < 0:
                continue
            for j in range(g_len):
                cur = (i+j) % g_len
                if possible + total[cur] < 0:
                    break
                possible += total[cur]
                if j == g_len-1:
                    return i
        return -1
'''