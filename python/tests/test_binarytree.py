from dsalgo.binarytree import BST
from dsalgo.binarytree import preorder, inorder, postorder, levelorder

import pytest

@pytest.fixture
def bst():
    """
          _10_
         5    20
        2   11  30
      -5 3        40
    """
    bst = BST()
    [bst.insert(_) for _ in [10,20,30,40,5,2,-5,3,11]]
    return bst


def test_insertion(bst):
    root = bst.root
    assert root.key == 10
    assert root.right.key == 20
    assert root.left.key == 5

    leftOf5 = bst.root.left.left
    assert leftOf5.key == 2
    assert leftOf5.left.key == -5
    assert leftOf5.right.key == 3

    rightOf5 = bst.root.left.right
    assert rightOf5 is None

    leftOf20 = bst.root.right.left
    assert leftOf20.key == 11
    assert leftOf20.left is None
    assert leftOf20.right is None

    rightOf20 = bst.root.right.right
    assert rightOf20.key == 30
    assert rightOf20.right.key == 40
    assert rightOf20.left is None


@pytest.mark.parametrize('key,expected', [
    (20, True),
    (-10, False),
    (0, False)
])
def test_search(bst, key, expected):
    assert bst.search(key) == expected


def test_min_max(bst):
    assert bst.max() == 40
    assert bst.min() == -5


@pytest.mark.parametrize('func,expected', [
    (preorder, [10,5,2,-5,3,20,11,30,40]),
    (inorder, [-5,2,3,5,10,11,20,30,40]),
    (postorder, [-5,3,2,5,11,40,30,20,10]),
    (levelorder, [10,5,20,2,11,30,-5,3,40]),
])
def test_traversals(bst, func, expected):
    assert [k for k in func(bst.root)] == expected
