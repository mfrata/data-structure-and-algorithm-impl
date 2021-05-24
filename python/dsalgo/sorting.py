from copy import deepcopy
from typing import List


def selectionSort(array: List[int]) -> List[int]:
    """
    TC: O(n²)
    MC: O(1)
    """
    arr = deepcopy(array)

    def swap(i, j):
        arr[i], arr[j] = (arr[j], arr[i])

    N = len(arr)
    maxIndex = 0
    for j in range(1, N + 1):
        for i in range(N - j + 1):
            maxIndex = i if arr[i] > arr[maxIndex] else maxIndex

        swap(N - j, maxIndex)
        maxIndex = 0
    return arr


def insertionSort(array: List[int]) -> List[int]:
    """
    TC: O(n²)
    MC: O(1)
    """
    arr = deepcopy(array)
    N = len(arr)

    def swap(i, j):
        arr[i], arr[j] = (arr[j], arr[i])

    def insertIntoSubArray(index):
        curIdx = index
        while arr[curIdx - 1] > arr[curIdx] and curIdx != 0:
            swap(curIdx, curIdx - 1)
            curIdx -= 1

    for i in range(1, N):
        insertIntoSubArray(i)

    return arr


def heapSort():
    pass


def shellSort():
    pass


def radixSort():
    pass


def quickSort(array: List[int]) -> List[int]:
    def findSplitPoint(A, first, last):
        def swap(i, j):
            A[i], A[j] = (A[j], A[i])

        pivot = A[first]
        leftmark = first + 1
        rightmark = last
        splitFound = False
        while not splitFound:
            while leftmark <= rightmark and A[leftmark] <= pivot:
                leftmark += 1
            while A[rightmark] >= pivot and rightmark >= leftmark:
                rightmark -= 1

            if rightmark < leftmark:
                splitFound = True
            else:
                swap(leftmark, rightmark)
        swap(first, rightmark)
        return rightmark

    def _quickSort(A, first, last):
        if first < last:
            split = findSplitPoint(A, first, last)
            _quickSort(A, first, split - 1)
            _quickSort(A, split + 1, last)
        return A

    return _quickSort(deepcopy(array), 0, len(array) - 1)


def mergeSort(array: List[int]) -> List[int]:
    """
    TC: O(n*log(n))
    MC: O(n)
    """

    def merge(L, R):
        merged = []
        i = 0
        j = 0

        def mergeRemainingOf(side, index):
            if index < len(side):
                [merged.append(side[x]) for x in range(index, len(side))]

        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                merged.append(L[i])
                i += 1
            else:
                merged.append(R[j])
                j += 1

        mergeRemainingOf(L, i)
        mergeRemainingOf(R, j)

        return merged

    def _mergeSort(A):
        N = len(A)
        mid = N // 2
        left = A[:mid]
        right = A[mid:]
        if N > 1:
            left = _mergeSort(left)
            right = _mergeSort(right)
            merged = merge(left, right)
        else:
            merged = A
        return merged

    return _mergeSort(deepcopy(array))


def bubbleSort(array: List[int]) -> List[int]:
    """
    TC: O(n²)
    MC: O(1)
    """
    arr = deepcopy(array)

    def swap(i, j):
        arr[i], arr[j] = (arr[j], arr[i])

    N = len(arr)

    for j in range(1, N):
        for i in range(N - j):
            if arr[i] > arr[i + 1]:
                swap(i, i + 1)

    return arr


def binarySearch(array: List[int], item: int) -> bool:
    def _binSearch(first, last):
        mid = (first + last) // 2
        if array[mid] == item:
            return True
        elif last <= first:
            return False
        else:
            if item > array[mid]:
                return _binSearch(mid + 1, last)
            else:
                return _binSearch(first, mid - 1)

    return False if len(array) == 0 else _binSearch(0, len(array) - 1)
