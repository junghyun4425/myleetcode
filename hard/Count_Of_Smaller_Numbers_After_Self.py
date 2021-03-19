# Problem Link: https://leetcode.com/problems/count-of-smaller-numbers-after-self/

'''
문제 요약: 배열의 오른쪽에있는 값들 중 자신이 더 큰 숫자면 1씩 더해서 결과를 반환하는 문제.
ask: nums = [5,2,6,1]
answer: [2,1,1,0]

해석:
First Try
왼쪽의 모든 작은수들을 카운팅하기위해 hashmap을 사용하면 O(n^2).
따라서 좀더 효율적일 수 있는 Binary Search Tree를 활용하기로 함.
각 트리노드에 count 라는 변수를 두고, 자신보다 작은값이 있다면 추가시켜주는 용도. (큰값을 만나면 이 값을 결과로 주도록)
성능 자체는 O(nlogn)으로 생각했으나, Worst case에서 O(n^2)이 나오기 때문에 시간초과가 뜸.
아마 밸런스 트리로 구현해야 될것 같은데, 다른방법으로 다음에 다시도전할때 좀더 연구해보기로.
'''

# First Try with BST. (Time Limit Exceeded cause of worst case 'Unbalanced Tree')
'''
class BSTNode():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.count = 1

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        if not nums: return []
        n_len = len(nums)
        root = BSTNode(nums[-1])
        ans = [0]*n_len
        def insert(node, val):
            new_count = 0
            while True:
                if node.val >= val:
                    node.count += 1
                    if node.left:
                        node = node.left
                    else:
                        node.left = BSTNode(val)
                        break
                else:
                    new_count += node.count
                    if node.right:
                        node = node.right
                    else:
                        node.right = BSTNode(val)
                        break
            return new_count
        for i in reversed(range(n_len-1)):
            ans[i] = insert(root, nums[i])
        return ans
'''