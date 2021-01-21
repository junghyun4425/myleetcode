# Problem Link: https://leetcode.com/problems/recover-binary-search-tree/

'''
문제 요약: 한번의 잘못된 스왑이 된 BST 트리가 인풋으로 오면 이를 원상복귀 시키는 문제. (단, 추가 스페이스는 O(1)을 만족할 것)
ask: [1,3,null,null,2]
answer: [3,1,null,null,2]

해석:
문제의 근본적인 의도를 못찾으면 코드가 굉장히 복잡해 지거나 문제 해결이 굉장히 까다로운 문제.
처음 낸 아이디어는, 잘못된 부분을 찾고 그 값이 들어갈 부분을 찾는 방법.
잘못된 부분을 찾는건 굉장히 쉬운편이지만, 이 잘못된 부분과 바꿔야 할 부분을 찾는 것이 굉장히 까다로움.
공간을 따로 사용하지 못하기 때문에 특히나 코드가 쓸데없이 길어지고 어려워짐.

한참 생각 끝에 단순히 BST의 성질을 파고들기 시작함. BST는 '정렬된 리스트'를 트리화 시킨것.
헌데, 만약 스왑을 해서 오류가 발생했다면 잘못된 부분은 하나 혹은 두개가 된다는 점.
예를들어,
List = [1,2,3,4,5,6,7,8] 의 잘 정렬된 리스트에서 오류로 스왑을 한번 했다고 친다면,
List_err = [1,2,3,8,5,6,7,4] 가 될것이며, 오류를 찾기위해선 잘못된부분 8->5 / 7->4 두군데를 찾으면 끝. 처음찾은 prev=8과 나중에 찾은 node=4를 바꾸면 끝.
만약 바로 옆자리 숫자와 바뀌었다면?
List = [1,2,3,4,5,6,7,8]
List_err = [1,2,3,5,4,6,7,8] 가 될것이며, 오류를 찾기위해선 잘못된 부분 5->4 한군데만 찾으면 끝. prev=5, node=4 이고, 뒤에 잘못된 부분이 발견되지 않으면 그대로 바꾸면 끝.
리스트를 예제로 보았으니 트리에 적용시키기만 하면 간단하게 해결이 됨.
트리를 '순차적'으로 탐색하면 정렬된 리스트와 같은 결과를 얻을 수 있음. 따라서 값이 이전보다 커지면, prev=i, node=j 를 기록.
한번 더 커지는 구간이 발견되면 node=k 를 기록하고 i와 k를 바꾸면 됨. 한번만 이상현상이 나타났다면, i와 j를 바꾸면 됨.
코드에서 보면 err1이 prev이고, err2가 node를 지칭함.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def searching(root):
            nonlocal prev, err1, err2
            if not root:
                return
            searching(root.left)
            if prev and prev.val >= root.val:
                if not err1:
                    err1 = prev
                err2 = root
            prev = root
            searching(root.right)

        err1 = err2 = None
        prev = None
        searching(root)
        err1.val, err2.val = err2.val, err1.val