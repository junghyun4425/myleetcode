# Problem Link: https://leetcode.com/problems/queue-reconstruction-by-height/

'''
문제 요약: 한 사람에 대해 [h, k]에서 h는 키, k는 앞에 크거나 같은 사람의 인원 수를 의미하고 이를 정렬하는 문제.
ask: people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
answer: [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]

해석:
키만 고려하는게 아니라 앞에 몇명의 더큰 사람이 있는지 까지 고려해야해서 오래 고민했던 문제.
처음 생각해낸 방법은 키를 오른차순으로 정렬하고 포지션에 맞게끔 위치를 넣어주는 방식으로 구현했음.
이미 채워진공간은 뛰어넘어서 다음칸에 삽입하는 방식.
하지만 키가 작은사람의 위치에 문제가 생겨버림. 키가 작은사람이 큰사람보다 먼저 오니까 작은사람의 k에 대해 맞춰줄수 없었음.
따라서 반대로 키가 큰사람부터 채워넣는 방식으로 구현. 위치는 오름차순 그대로 유지되어야 하기떄문에 이부분을 주의해야 함.
그리고 사람의 위치 k에 맞에 배열에 삽입해 주기만 하면 끝.
'''

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        ans = []
        people.sort(key=lambda x: (x[0], -x[1]), reverse=True)
        for p in people:
            ans.insert(p[1], p)
        return ans