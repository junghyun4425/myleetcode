# Problem Link: https://leetcode.com/problems/perfect-rectangle/

'''
문제 요약: 입력으로 들어오는 좌표들이 사각형을 의미할때, 모든 사각형의 합이 하나의 사각형이 되는 경우를 확인하는 문제.
ask: rectangles = [[1,1,3,3],[3,1,4,2],[3,2,4,4],[1,3,2,4],[2,3,3,4]]
answer: True

해석:
Perfect한 사각형이 되기 위한 원리를 알면 쉽지만 그게 아니라면 굉장히 어려운 문제.
처음에는 모든 사각형의 양 변을 활용해 최대길이까지 이어지는지 확인해보려 했으나 굉장히 코드가 복잡해지고 비효율적인 면을 보임.
고민끝에 사각형의 넓이를 구하는 방법을 채택함.
모든 사각형들의 넓이를 구하고 가장 끝에 존재하는 x,y 들의 좌표를 통해 원래 area값을 구하게 됨.
이 또한 문제가 발생하는데, [[0,0,1,1],[0,1,3,2],[1,0,2,2]] 의 경우와 같이 넓이가 중복되는 경우를 판단하지 못함.
그래서 이를 방지하고자 겹치는 점의 개수를 셈.
모든 사각형의 점 4개를 각각 저장하면 perfect사각형인 경우에는 안쪽 사각형일경우 짝수개의 점을 만나게 됨.
즉, 홀수개의 점이 남는다면 이는 완벽한 사각형이 아님. 따라서 XOR 연산으로 짝수개인지 홀수개인지 판단하고, 최종적으로 4개의 꼭지점만 남아야 함.

결론을 지어보자면, 2가지 규칙을 지켜줘야 Perfect 사각형이라 할수 있음.
1. 작은 사각형들의 꼭지점을 모두 카운팅 했을때, 꼭지점 4개를 제외하고는 모두 짝수개가 되어야함. (좌표를 XOR 연산으로 해서 사라져야함)
2. 꼭지점에 의한 사각형의 넓이와 모든 사각형의 넓이가 같아야 함.
위 두가지 조건만 맞춰주면 쉽게 해결이 가능.
'''

class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        sum_area = 0
        points = set()
        for x,y,X,Y in rectangles:
            sum_area += (X - x) * (Y - y)
            points ^= {(x,y), (x,Y), (X,y), (X,Y)}
        if len(points) != 4: return False
        x, y = min(points, key = lambda x: x[0] + x[1])
        X, Y = max(points, key = lambda x: x[0] + x[1])
        return sum_area == (X - x) * (Y - y)