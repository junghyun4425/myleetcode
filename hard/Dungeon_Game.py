# Problem Link: https://leetcode.com/problems/dungeon-game/

'''
문제 요약: 기사는 (0,0)을 시작점, 공주는 (n,m)에 잡혀있을때, 공주를 구하러가는 최소 체력을 구하는 문제.
        좌측, 아래측으로만 움직일 수 있음. 음수는 몬스터에게 입는 피해, 양수는 체력 회복. 체력 0이하는 죽음.
ask: [[-2,-3,3],[-5,-10,1],[10,30,-5]]
answer: 7 (right -> right -> down -> down)

해석:
문제가 생각보다 복잡한 구성을 띄고 있음. -> 최소한의 체력이기 때문에 중간에 체력회복하는 경우는 0으로 처리해줘야 함.
DP로 문제를 풀어야 하겠지만, 기본 알고리즘이 잘 동작하는지 부터 확인해 보기위해 recursion 방식으로 우선 해결.

-Recursion
시작점부터 끝까지 좌측과 하단의 모든 경우를 탐색함.
마지막 지점에 왔을때는 음수의 경우 최소체력에 필요한 정보이기에 반환, 양수면 비교에 방해되기 때문에 0으로 자름.
이전 함수로 돌아오면서 좌측과 아래측의 최소값을 저장함. 이 변수는 min_req.
두 방향 중에서 최소값을 구했다면 이전으로 돌아가기위해 return.
반환할때 return -min(dungeon[i][j]-min_req, 0) 만해도 충분히 해결이 가능하지만, 예외의 경우때문에 추가적으로 max()함수를 씀.
바로 [[-3,5]] 와같은 예외 케이스의 경우에 정답은 4인데 3이 반환됨 (2번째 값이 양수기 때문에)
이런 케이스를 없애고자 조금은 쓸모없는 -min(dungeon[i][j]-1, 0) 를 계산하고 위의 식 중에서 max값을 찾음.
결과는 상당히 만족스럽지만, 최종 결과는 time limit exceeded

DP로 다시 풀어보기.
'''

# Solution with Recursion: Timeout [Failed]
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        h, w = len(dungeon)-1, len(dungeon[0])-1
        di = [(0,1),(1,0)]
        def search(i, j):
            if i == h and j == w:
                return -min((dungeon[i][j]-1), 0)
            min_req = float('inf')
            for d in di:
                new_i, new_j = i+d[0], j+d[1]
                if new_i > h or new_j > w:
                    continue
                require = search(new_i, new_j)
                min_req = min(min_req, require)
            return max(-min(dungeon[i][j]-1, 0), -min(dungeon[i][j]-min_req, 0))
        return max(1, search(0, 0))