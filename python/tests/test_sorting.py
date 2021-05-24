import pytest

from dsalgo.sorting import (
    bubbleSort,
    selectionSort,
    insertionSort,
    mergeSort,
    quickSort,
    binarySearch,
)


testCases = pytest.mark.parametrize(
    "_input,expected",
    [
        ([2, 3, 1], [1, 2, 3]),
        ([54, 26, 93, 17, 77, 31, 44, 55, 20], [17, 20, 26, 31, 44, 54, 55, 77, 93]),
        ([-10, 20, 3, 100, 40000, -6000], [-6000, -10, 3, 20, 100, 40000]),
        ([4, 5, 3, 7, -1, 7, 7, 8, 10, -10], [-10, -1, 3, 4, 5, 7, 7, 7, 8, 10]),
    ],
)


@testCases
def test_bubbleSort(_input, expected):
    assert expected == bubbleSort(_input)


@testCases
def test_selectionSort(_input, expected):
    assert expected == selectionSort(_input)


@testCases
def test_insertionSort(_input, expected):
    assert expected == insertionSort(_input)


@testCases
def test_mergeSort(_input, expected):
    assert expected == mergeSort(_input)


@testCases
def test_quickSort(_input, expected):
    assert expected == quickSort(_input)


@pytest.mark.parametrize(
    "array,item,expected",
    [
        ([1, 2, 3], 2, True),
        ([1, 2, 3], 4, False),
        ([1], 1, True),
        ([1], 2, False),
        ([], 100, False),
        ([-10, -1, 3, 4, 5, 7, 7, 7, 8, 10], 7, True),
        ([-10, -1, 3, 4, 5, 7, 7, 7, 8, 10], 6, False),
    ],
)
def test_binarySearch(array, item, expected):
    assert binarySearch(array, item) == expected
