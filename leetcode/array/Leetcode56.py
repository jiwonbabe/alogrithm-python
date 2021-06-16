from collections import deque
from typing import List


def checkIfItHasOverlappingPart(top: List[int], new: List[int]) -> bool:
    return top[1] >= new[0]


class Solution:
    """
    Time Complexity: O(NlogN) -> sorting 때문에
    Space Complexity: O(N) -> stack 을 따로 두었기 때문(개선 여지 존재)
    1. 예시를 이용해 어떤식으로 접근할지
    2. 어떤 자료구조를 사용할 수 있을지
    3. 시/공간 복잡도 계산
    4. edge case 검토
    """
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda i: i[0])
        stack = deque()
        index = 0
        while index <= len(intervals) - 1:
            if len(stack) == 0:
                stack.append(intervals[index])
            elif checkIfItHasOverlappingPart(stack[-1], intervals[index]):
                top = stack[-1]
                new = intervals[index]
                stack.pop()
                stack.append([top[0], max(new[1], top[1])])
            else:
                stack.append(intervals[index])
            index += 1

        return list(stack)