class MedianFinder:
    min_heap = []

    def __init__(self):
        self.min_heap.append(0)

    def addNum(self, num: int) -> None:
        self.min_heap.append(num)
        # swim
        i = len(self.min_heap) - 1
        while i > 1 and self.min_heap[int(i / 2)] > self.min_heap[i]:
            self.min_heap[i], self.min_heap[int(i / 2)] = self.min_heap[int(i / 2)], self.min_heap[i]
            i = int(i / 2)

    def findMedian(self) -> float:
        if len(self.min_heap) % 2 == 0:
            # 홀수 개
            return float(self.min_heap[int(len(self.min_heap) / 2)])
        else:
            mid_index = int(len(self.min_heap) / 2)
            return float((self.min_heap[mid_index] + self.min_heap[mid_index + 1]) / 2)


obj = MedianFinder()
obj.addNum(1)
param_2 = obj.findMedian()
print(param_2)
