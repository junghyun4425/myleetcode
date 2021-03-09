'''
개요: 퀵정렬을 실제로 구현하기.
설명:
퀵정렬을 이해하고 바로 구현.
다른 정렬알고리즘은 막힘없이 진행되었다면 퀵정렬은 특정 부분에 막혀 굉장히 오래 걸림.
partition 함수에서 pivot 위치를 찾는 알고리즘에서 문제가 발생.
low 와 high를 원하는 위치(pivot보다 작거나 or 크거나)까지 간다음 자리를 교체하는 식으로 알고리즘을 구현했는데, 결과가 원치않게 나옴.
그 이유는 마지막 마무리 처리를 안해서 그럼.
이전에는 while문을 수행하고 마지막에 조건절 없이 arr[high]와 arr[low]를 바꿈.
하지만 high < low 되는 경우는 교환하지 않고 while loop를 빠져나와 pivot자리와 바꿔야 함.
단순하지만 이걸 당연히 처리했다 생각하고 코딩한 결과 구현에 시간이 오래걸림. (나중에 퀵정렬은 한번 더 구현해봐야겠음)

시간복잡도: Best - O(nlogn) / Worst - O(n^2)
공간복잡도: O(1)
'''

class QuickSort:
    def sort(self, arr):
        a_len = len(arr)
        self.quick_sort(arr,0, a_len-1)

    def quick_sort(self, arr, l, r):
        if l < r:
            pivot = self.partition(arr, l, r)
            self.quick_sort(arr, l, pivot-1)
            self.quick_sort(arr, pivot+1, r)

    def partition(self, arr, l, r):
        low, high = l+1, r
        pivot = arr[l]
        while low <= high:
            while low <= r and arr[low] <= pivot:
                low += 1
            while high > l and arr[high] > pivot:
                high -= 1
            if low <= high:
                arr[low], arr[high] = arr[high], arr[low]
        arr[high], arr[l] = arr[l], arr[high]
        return high


if __name__ == "__main__":
    arr = [5,4,6,5,4,3,8,7,1]
    quick = QuickSort()
    quick.sort(arr)
    print(arr)