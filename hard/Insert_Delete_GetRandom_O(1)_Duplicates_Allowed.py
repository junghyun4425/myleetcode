# Problem Link: https://leetcode.com/problems/insert-delete-getrandom-o1-duplicates-allowed/

'''
문제 요약: 숫자를 추가하고 추가된 숫자들로부터 랜덤한 값을 가져오는 클래스를 구현하는 문제. (중복 허용, 중복개수가 확률에 영향을 미침)
ask:
["RandomizedCollection", "insert", "insert", "insert", "getRandom", "remove", "getRandom"]
[[], [1], [1], [2], [], [1], []]
answer:
[null, true, false, true, 2, true, 1]

해석:
중복이 허용되지 않는 이전 문제는 간단히 해결했지만 이번에는 O(1)을 맞추기위해 다른방법으로 구현해야 함.
우선 value에 대해 arr의 idx를 모아서 저장해놓는 해쉬맵을 하나 정의함.
그리고 실제 랜덤값으로 가져올 arr를 정의.
insert()
해쉬맵 키가 val 이 되며 값으로는 set()안에 arr의 인덱스를 저장해놓음.
그리고 val을 배열에 저장.
remove()
삭제 함수를 O(1)로 만드는게 핵심.
단순히 해쉬맵에서 인덱스를 참고해 그 인덱스를 삭제하게되면 O(n)의 시간복잡도를 가지게 됨.
O(1)로 하기위해서는 삭제한 인덱스에 가장뒤에있는 배열의값을 삭제하는 위치에 저장하고 맨끝의 배열을 없애는 방법을 사용해야함.
이러려면 맨 뒤에있는 값의 해쉬맵 인덱스를 수정해줘야하고 번거롭지만 수행시간이 굉장히 빨라짐.
getRandom()
insert, remove를 이런식으로 설계함은 getRandom에서 O(1)로 값을 뽑아내기위한 노력.
배열을 Random모듈의 choice함수로 O(1)의 시간복잡도를 가지는 랜덤값을 가져옴.
'''

class RandomizedCollection:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hm = defaultdict(set)
        self.arr = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        self.hm[val].add(len(self.arr))
        self.arr.append(val)
        return len(self.hm[val]) == 1

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        if not self.hm[val]:
            return False
        new_idx, last_val = self.hm[val].pop(), self.arr[-1]
        self.arr[new_idx] = last_val
        self.hm[last_val].add(new_idx)
        self.arr.pop()
        self.hm[last_val].discard(len(self.arr))
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        return choice(self.arr)


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()