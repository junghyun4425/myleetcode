'''
개요: 자료구조 Heap을 배열로 직접 구현해보기
설명:
힙의 동작원리를 이해하고 바로 소스코드로 작성.
insert를 구현할땐 굉장히 쉽다고 생각했는데 delete가 조금 복잡한 부분이 있었음.
범용성이나 안전성 생각하지 않고 순수히 동작도로만 작성한 코드라 헛점이 많음.
다음에 복습할때는 최적화도 고려해 리뷰하기.
'''

class Heap:
    def __init__(self):
        self.h = []
        self.index = -1

    def insert(self, v):
        self.h.append(v)
        self.index += 1
        cur = self.index
        while self.h[cur] > self.h[cur//2]:
            self.h[cur], self.h[cur//2] = self.h[cur//2], self.h[cur]
            cur //= 2

    def delete(self):
        if self.index < 0: return
        v = self.h[0]
        self.h[0] = self.h[self.index]
        self.h = self.h[:-1]
        self.index -= 1
        cur = 0
        while cur < self.index:
            if cur*2+1 <= self.index:
                if self.h[cur*2] > self.h[cur*2+1]:
                    self.h[cur], self.h[cur*2] = self.h[cur*2], self.h[cur]
                else:
                    self.h[cur], self.h[cur*2+1] = self.h[cur*2+1], self.h[cur]
                cur = cur*2+1
                continue
            elif cur*2 <= self.index and self.h[cur*2] > self.h[cur]:
                self.h[cur], self.h[cur * 2] = self.h[cur * 2], self.h[cur]
            cur *= 2
        return v

    def getHeap(self):
        return self.h

if __name__ == "__main__":
    h = Heap()
    h.insert(3)
    h.insert(5)
    h.insert(7)
    h.insert(10)
    h.insert(5)
    h.insert(4)
    h.insert(9)
    h.insert(11)
    print(h.getHeap())
    h.delete()
    h.delete()
    h.delete()
    h.delete()
    print(h.getHeap())