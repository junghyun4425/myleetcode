'''
개요: Segment Tree 구현
설명:
Range Sum에 최적의 성능을 보이는 Segment Tree를 배열과 재귀함수를 통해 구현.
세그먼트 트리란 배열의 값을 leaf노드로 하고 부모노드는 그 값들의 합을 저장하고 있는 트리형 자료구조.
트리로 구현이 가능하지만 배열로도 효율적으로 구현이 가능.
세그먼트 트리의 필수 함수들을 설명하자면,

init()
배열을 받아 길이의 4배만큼 tree배열을 할당해준 뒤, build() 재귀함수를 호출해 tree를 완성.
여기서 4배를 해준이유는 사이즈를 정확하게 하지않고 메모리를 좀더 써서 사용.
실제 사이즈는 트리의 높이만큼의 사이즈만큼만 할당하면 되기 때문에, 2의 logn승 만큼만 가져오면 됨.
물론 루트는 1부터 시작해야하니 이부분도 고려하면 2^(logn+1) - 1 이 되어야 함.

build()
index start 부터 end 까지를 divide_and_conquer 방식으로 쪼개면서 위치를 찾아감.
start==end 되는 지점이 leaf노드를 의미하므로 tree배열에 넣어줌.
부모는 자식들의 노드를 합해주면 되기 때문에 자식 둘의 합을 tree배열에 저장.

update() + update_diff()
값의 변경을 확인하고 차이를 구한다음 그에 맞는 위치의 leaf노드와 부모노드 합을 변경해줌.
부모노드에서부터 값을 바꿔가면서 자식노드까지 변경하면 되는 간단한 원리.
인덱스 i가 start, end범위를 벗어나면 값을 변경하지않고 리턴.

sum() + sum_range()
left와 right의 범위값을 계산하는 함수.
부모에서 자식으로 내려가면서 range가 포함되는 노드를 찾아감.
현재 부모노드가 가지는 start~end 범위에 만약 left, right 모두 포함된다면 부모노드가 합이기 때문에 이를 리턴함.
left, right 중에서 하나라도 벗어났다면 그 밑단까지 내려가야함.
둘다 벗어났다면 값이 없는 상태이므로 0을 반환.
그렇게 양쪽으로 나눈 재귀함수들의 합을 구하면 최종 결과를 얻을 수 있음.

사실 이는 최적화된 Segment Tree는 아님. 바이너리트리의 사이즈를 이보다 훨씬 줄인 2*n 으로 트리를 구성할 수 있는 방법이 있음.
따라서 다음 복습을 할때는 새로운 방법으로 구현해보도록 할 것.
'''

class SegmentTree:
    def __init__(self, arr):
        self.arr = arr
        self.tree = [0]*(4*len(arr))
        self._build(1, 0, len(arr)-1)

    def _build(self, root, start, end):
        if start == end:
            self.tree[root] = arr[start]
            return arr[start]
        m = (start + end) // 2
        self.tree[root] = self._build(root*2, start, m) + self._build(root*2+1, m+1, end)
        return self.tree[root]

    def update(self, i, val):
        diff = val - self.arr[i]
        self.arr[i] = val
        self._update_diff(1, 0, len(self.arr)-1, i, diff)

    def _update_diff(self, root, start, end, i, diff):
        if i < start or i > end: return
        self.tree[root] += diff
        if start == end: return
        m = (start + end) // 2
        self._update_diff(root*2, start, m, i, diff)
        self._update_diff(root*2+1, m+1, end, i, diff)

    def sum(self, left, right):
        return self._sum_range(1, 0, len(self.arr)-1, left, right)

    def _sum_range(self, root, start, end, left, right):
        if left > end or right < start: return 0
        if left <= start and end <= right: return self.tree[root]
        m = (start + end) // 2
        return self._sum_range(root*2, start, m, left, right) + self._sum_range(root*2+1, m+1, end, left, right)

    def print(self):
        print(self.tree)


if __name__ == "__main__":
    arr = [1,2,3,4,5,6,7,8,9]
    seg = SegmentTree(arr)
    seg.print()
    # [0, 45, 15, 30, 6, 9, 13, 17, 3, 3, 4, 5, 6, 7, 8, 9, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    seg.update(3, 10)
    seg.print()
    # [0, 51, 21, 30, 6, 15, 13, 17, 3, 3, 10, 5, 6, 7, 8, 9, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    print(seg.sum(0, 3))    # 16
    print(seg.sum(4, 6))    # 18