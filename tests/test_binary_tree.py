import pytest
from src.trees.binary_search import BinarySearchTree

@pytest.fixture
def tree():
    return BinarySearchTree()

def test_empty_tree_insert(tree):
    tree.insert(5)
    assert tree.root.value == 5
    assert tree.root.left is None
    assert tree.root.right is None

def test_multiple_inserts(tree):
    values = [5, 3, 7]
    for value in values:
        tree.insert(value)
        
    assert tree.root.value == 5
    assert tree.root.left.value == 3
    assert tree.root.right.value == 7