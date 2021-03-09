# Problem Link: https://leetcode.com/problems/course-schedule-ii/

'''
문제 요약: 스케쥴을 수행하고 다음 스케쥴을 수행할 수 있는 순서를 반환하는 문제. (사이클이 있는경우 [] 를 반환)
ask: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
answer: [0,2,1,3] (or [0,1,2,3])

해석:
처음으로 위상정렬을 코딩해봄. (이론만 알고있었고 코딩해본적은 없었음)
그래서 몇가지 잔실수와 한가지 시행착오를 겪음.
잔실수야 코드문제기 때문에 쉽게 발견가능했고, 시행착오는 사이클을 어떻게 판별할지 몰랐던 점.
생각해보니 사이클이 생겼다면 for루프를 빠져나왔을때 위상정렬의 결과가 모든 코스를 기록하지 못한다는 점을 발견. (사이클은 진입차수가 0이 될수없기 때문)
따라서 사이클은 마지막에 존재여부를 알수 있었음.
기본적인 알고리즘은,
1.indegree 배열을 만들어 집인차수를 관리함. (0이되면 stack에 빼줘야 하기 때문)
2.진입차수가 0인 값들을 stack으로 빼줘서 연계과목의 진입차수를 1씩 빼줌.
3.연계과목 진입차수를 1 뺐을때 0이되면 stack에 추가해줌.
이를 반복하면 문제 해결이 가능함. stack이 아니라 queue여도 문제없고, 순서만 달라질 뿐.

다음 리뷰때는 DFS로 푸는 방법을 통해 해결해보는걸로.
'''

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0]*numCourses
        courses = defaultdict(list)
        stack = []
        ans = []
        for c in prerequisites:
            courses[c[1]] += [c[0]]
            indegree[c[0]] += 1
        stack.extend([i for i, c in enumerate(indegree) if c == 0])
        while stack:
            cur = stack.pop()
            ans.append(cur)
            for c in courses[cur]:
                indegree[c] -= 1
                if indegree[c] == 0:
                    stack.append(c)
        return ans if len(ans) == numCourses else []