# Problem Link: https://leetcode.com/problems/circular-array-loop/

'''
문제 요약: 0번째와 마지막 인덱스가 이어진 배열이 있다고 가정하고, 싸이클이 형성되는지 여부를 묻는 문제. (단, 자기자신만 반복이면 싸이클x)
    추가로, 배열안의 이동값이 양수이다가 갑자기 음수가 되면 사이클로 인정하지 않음.
ask: [2,-1,1,2,2]
answer: True (0번 인덱스에서 길이 3의 싸이클이 존재함.)

해석:
이 문제의 핵심은 사이클 여부를 판단하는 것. 보통 사이클을 체크하기 위해 알고있던 방식이 Union-Find 알고리즘이지만, 구현하기엔 복잡성이 증가함.
크게 두가지 방법으로 사이클 여부를 판단하는 방법을 생각해봄.
첫째는 포인터 두개를 사용. 시작점 i 를 고정시킨채로, 다른 변수로 움직이다가 다시 i를 만나면 사이클을 체크하는 방법.
이는 visited 를 하나만 필요로 하기 때문에 메모리 효율이 좋지만 따로 길이를 판별해야하기 때문에 코드가 조금더 길어짐.
두번째는 visited 를 두개 사용해서 해결하는 방법. global visited는 중복 방지를, local visited는 루프가 존재하는지 판단.
두번째 방법을 선택했으며, visited를 만들기 위해 set 자료구조를 활용.
만약 방문한적이 있는 path라면 사이클이 형성되었으므로 True를 반환하여 마무리하고, 아니라면 모든 배열을 체크해 빠져나가 False를 반환.
시간복잡도는 중복 계산을 피했기 떄문에 O(n) 이며 공간 복잡도도 O(n).
'''

class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n_len = len(nums)
        visited = set()
        for i in range(n_len):
            if i not in visited:
                local = set()
                while True:
                    if i in local:
                        return True
                    local.add(i)
                    visited.add(i)
                    prev, i = i, (i + nums[i]) % n_len
                    if prev == i or (nums[prev] > 0) != (nums[i] > 0):
                        break
        return False