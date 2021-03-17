# Problem Link: https://leetcode.com/problems/range-sum-query-mutable/

'''
문제 요약: range에 존재하는 배열의 합을 구하는 클래스를 구현하는 문제.
ask:
["NumArray", "sumRange", "update", "sumRange"]
[[[1, 3, 5]], [0, 2], [1, 2], [0, 2]]
answer:
[null, 9, null, 8]

해석:
도중에 update가 있기 때문에 배열의 합을 따로 저장하는것은 비효율적.
O(n)이하로 만드는 좋은방법이 안떠올라서 찾아보니 segment tree라는 처음보는 자료구조가 존재했다는걸 알게됨.
segment트리를 배열로 구현하면 심플해서 시도해봄. 개인적으로 sum_range 함수를 구현하는데 굉장히 어려웠음.
tree의 0번은 쓰지않고 1번부터 해야 자식노드간 관계를 확실히 할수 있음. 거기에 원래 배열 길이의 2배가 되어야 segment tree구현이 가능.
init에 segment tree를 만들어야 하는데 leaf노드에 원래값이 들어있으므로 여기부터 채우고, 부모노드를 하나씩 더해가면서 채움.
update는 어렵지 않은데, index에 맞는 트리에서부터 부모노드까지 올라가면서 차이점만 더해주면 됨.
sum_range가 정말 어려웠는데 이부분은 여러 조건이 있기 때문.

sum_range
1.left, right 가 바로 붙어있을때. 부모가 같다면 부모를 더해주면 끝 / 부모가 다르다면 서로 자기자신만 더해주면 끝.
2.left가 왼쪽에 있을때 -> 어차피 오른쪽을 더해야하기 때문에 현재 노드를 더하지않고 부모노드로 올라감. (부모가 양쪽 노드의 합이기 때문)
3.left가 오른쪽 있을때 -> 왼쪽을 더하면 안되기 때문에 오른쪽만 더하고 오른쪽에있는 부모노드로 넘어감.
4.right가 왼쪽에 있을때 -> left와는 반대로 오른쪽을 더하면 안되니 현재노드를 더하고 이전의 부모노드로 넘어감.
위의 규칙을 생각해서 구현하는데 생각보다 너무 어려웠음. 구현을 하고도 된다는게 신기한 상황.
segment tree는 무조건 다시 복습.
'''

class NumArray:
    def __init__(self, nums: List[int]):
        self.len = len(nums)
        self.tree = [0] * (self.len * 2)
        for i in range(self.len, self.len*2):
            self.tree[i] = nums[i-self.len]
        for i in reversed(range(1, self.len)):
            self.tree[i] = self.tree[i*2] + self.tree[i*2+1]
        print(self.tree)

    def update(self, index: int, val: int) -> None:
        index += self.len
        diff = val - self.tree[index]
        while index > 0:
            self.tree[index] += diff
            index //= 2

    def sumRange(self, left: int, right: int) -> int:
        left += self.len
        right += self.len
        summ = 0
        while left <= right:
            if left % 2 == 1:
                summ += self.tree[left]
                left += 1
            if right % 2 == 0:
                summ += self.tree[right]
                right -= 1
            left //= 2
            right //= 2
            print(summ)
        return summ

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)