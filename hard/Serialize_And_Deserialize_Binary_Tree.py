# Problem Link: https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

'''
문제 요약: 바이너리 트리를 string으로 직렬화하고, 그 string을 다시 바이너리 트리로 원상복귀 시키는 문제.
ask: [1,2,3,null,null,4,5]
answer: [1,2,3,null,null,4,5]

해석:
문제의 난이도가 hard인것에 비해 간단하게 해결할 수 있었지만, 이 문제가 마음에 드는점은 실제 직렬화를 어떤식으로 하는지 궁금했었기 때문.
파이썬의 경우 pickle을 사용해서 필요할때 직렬화를 하는데, 이렇게라도 원리를 배우게되어서 굉장히 뜻깊었던 문제.
트리를 직렬화하는 방법은 어렵지 않음.원
-직렬화-
우선 루트부터 차근차근 아래로 내려가야하기 때문에 preorder 순회로 데이터의 값을 저장.
이때 중요한점은, None값을 의미없는 값으로 대신해서 넣어줘야 복원할때 문제없이 가능. (여기선 '#' 으로 NULL을 표현함)
-복원-
데이터를 하나씩 꺼내서 preorder순서대로 복원시키면 됨. '#'을 만나면 None을 반환해주는것 외에는 별다른 특징없이 해결 가능.
데이터를 앞에서부터 꺼내오기 때문에 일반 리스트 보다는 효율이 좋은 파이썬 내장함수 deque로 구현함.
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        res = []
        def preorder(root):
            if not root:
                res.append('#')
                return
            res.append(str(root.val))
            preorder(root.left)
            preorder(root.right)
        preorder(root)
        return ','.join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        queue = deque()
        for d in data.split(','):
            queue.append(d)
        def recursion(data):
            if not data:
                return None
            if data[0] == '#':
                queue.popleft()
                return None
            root = TreeNode(queue.popleft())
            root.left = recursion(queue)
            root.right = recursion(queue)
            return root
        return recursion(queue)

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))