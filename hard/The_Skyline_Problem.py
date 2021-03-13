# Problem Link: https://leetcode.com/problems/the-skyline-problem/

'''
문제 요약: 빌딩의 왼쪽, 오른쪽좌표와 높이가 주어질때, 빌딩의 높이가 달라지는 지점을 모두 찾아내는 문제. (사이트 그림을보면 문제를 쉽게 이해 가능)
ask: buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
answer: [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]

해석:
First Try
알고리즘을 무시하고 메모리를 써서 쉽게 해결하려 했던게 잘못된 길로 가게된 원인.
모든 길이의 랜드를 미리 파악한 다음, 건물의 최대길이를 파악해 쉽게 달라진 지점을 찾을 수 있음.
간단한 예제는 모두 통과하지만 memory가 담을 수 없는 한계의 길이가 주어지면 통과 불가능.

Second Try with heap queue
다양한 예외를 만나면서 굉장히 오래걸렸던 문제. 예외는 마지막에 정리하도록 하고 일단 알고리즘 동작방식 부터 설명.
모든 빌딩에 대해 start_point 와 end_point 두가지 경우를 points에 모두 모아서 x에 대해 순차적으로 가장 높거나 낮은 포인트를 ans에 저장하는 방식.
x는 가로 y는 높이의 값을 나타냄.
heapq는 현재 최상위 지점을 의미함.
pointer가 start_point일때 y값이 heapq의 최대값 보다 크다면 heapq에 넣어주고 ans에 좌표(x,y)를 저장함.
pointer가 end_point일때 heapq에 들어있는 end_point를 제거하고 heapq에 남은 값을 ans에 좌표를 저장함. (단, y > heapq_max 보다 클때 저장)

마주친 예외들.
1. [[0,2,3],[2,5,3]] 와같이 연속적으로 같은값이 있을때. 정렬의 경우 x값이 같다면 start_point, end_point 중 start_point가 먼저 오게끔 해야함.
    안그러면 가운데 겹치는 부분의 모든 포인트를 찍어냄.
2. [[1,2,1],[1,2,2],[1,2,3]] 와같이 겹겹이 올린 사각형. 이 경우에는 y값에 대해 정렬을 해줘야함.
    따라서 end_point의 y와 start_point의 y와 각각 따로 정렬되게 하기 위해서 end_point y값에 음수를 붙여서 해결함.
굉장히 복잡하게 풀었지만 분명 좋은 방법이 있을거라고 예상함.
따라서 다음에 리뷰할떄는 다른 사람들의 코드를 보며 배우는 방식으로 복습해야 할것.
'''

# Second Try (Using Heap Queue)
from heapq import heappush, heapify
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        ans = []
        # Make start & end points
        points = []
        for b in buildings:
            points.extend([(b[0],b[2],'s'),(b[1],-b[2],'e')])
        points.sort(key=lambda x: (x[0], -x[1]))
        hq = [0]
        # Find all points
        for x,y,s in points:
            if s == 's':
                if y > -hq[0]:
                    ans.append([x,y])
                heappush(hq, -y)
            elif s == 'e':
                hq.remove(y)
                heapify(hq)
                if -y > -hq[0]:
                    ans.append([x,-hq[0]])
        return ans

# First Try (Memory Error)
'''
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        max_w = max([w for _, w, _ in buildings]) + 2
        line = [0] * max_w
        ans = []
        for start, end, height in buildings:
            for i in range(start, end+1):
                line[i] = max(line[i], height)
        if line[0] != 0:
            ans.append([0, line[0]])
        for i in range(1, max_w):
            if line[i-1] < line[i]:
                ans.append([i, line[i]])
            elif line[i-1] > line[i]:
                ans.append([i-1, line[i]])
        return ans
'''