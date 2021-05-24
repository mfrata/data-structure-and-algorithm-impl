from typing import Any, Optional, List
from dataclasses import dataclass, field

from dsalgo.queue import Queue


class Tree:
    pass

@dataclass
class BinaryTree(Tree):
    key: Any
    left: Optional[Tree] = None
    right: Optional[Tree] = None


def preorder(t: Tree):
    if t is not None:
        yield t.key
        yield from preorder(t.left)
        yield from preorder(t.right)


def inorder(t: Tree):
    if t is not None:
        yield from inorder(t.left)
        yield t.key
        yield from inorder(t.right)


def postorder(t: Tree):
    if t is not None:
        yield from postorder(t.left)
        yield from postorder(t.right)
        yield t.key


def levelorder(t: Tree):
    toVisit = Queue()
    toVisit.enqueue(t)

    while not toVisit.empty():
        visitingNode = toVisit.dequeue()

        if visitingNode.left is not None:
            toVisit.enqueue(visitingNode.left)
        if visitingNode.right is not None:
            toVisit.enqueue(visitingNode.right)

        yield visitingNode.key


@dataclass
class BST:
    root: Optional[BinaryTree] = None
    maxDepth: int = 0

    def insert(self, key: int):
        def _insert(parent: BinaryTree, key: int, depth: int):
            self.maxDepth = max(depth, self.maxDepth)
            if key > parent.key:
                if parent.right is None:
                    parent.right = BinaryTree(key)
                else:
                    _insert(parent.right, key, depth+1)
            else:
                if parent.left is None:
                    parent.left = BinaryTree(key)
                else:
                    _insert(parent.left, key, depth+1)

        if self.root is None:
            self.root = BinaryTree(key)
            self.maxDepth += 1
        else:
            _insert(self.root, key, 1)

    def search(self, key: int) -> bool:
        def _search(node: BinaryTree, key: int) -> bool:
            if node is None:
                return False
            elif node.key == key:
                return True
            else:
                if key > node.key:
                    return _search(node.right, key)
                else:
                    return _search(node.left, key)

        return _search(self.root, key)

    def max(self):
        def _max(parent: BinaryTree):
            if parent.right is None:
                return parent.key
            else:
                return _max(parent.right)
        return _max(self.root)

    def min(self):
        def _min(parent: BinaryTree):
            if parent.left is None:
                return parent.key
            else:
                return _min(parent.left)
        return _min(self.root)

    def delete(self, key: int):
        raise NotImplementedError


    def _balance_tree(self):
        raise NotImplementedError
