import time
import matplotlib.pyplot as plt

from utils.nodes import BaseNode
from utils.visualize_tree import visualize_tree

class BinarySearchTree():
    def __init__(self):
        self.root = None
    
    def insert(self, value):

        if value is None:
            raise Exception("Invalid Node Value")
        node = BaseNode(value)
        if self.root is None:
            self.root = node
            return
        else:
            self._insert_recursive(self.root, value)


    def _insert_recursive(self, node, value):
        if node is None:
            return BaseNode(value)
       
        if node.value == value:
            return node

        if value > node.value:
            node.right = self._insert_recursive(node.right, value)
        else:
            node.left = self._insert_recursive(node.left, value)

        return node

    def delete(self, value):
        self.root = self._delete_recursive(self.root, value)


    def _delete_recursive(self, node, value):
        if not node:
            return None
        
        if value < node.value:
            node.left = self._delete_recursive(node.left, value)
        elif value > node.value:
            node.right = self._delete_recursive(node.right, value)
        else:
            if not node.right:
                return node.left
            elif not node.left:
                return node.right
            else:
                temp = self._min_value_node(node.right)
                node.value = temp.value
                node.right = self._delete_recursive(node.right, temp.value)
        
        return node
    def _min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    def search(self, value):
        if value is None or self.root is None:
            return None
        
        curr = self.root
        while curr is not None:
            if value == curr.value:
                return curr
            elif value > curr.value:
                curr = curr.right
            elif value < curr.value:
                curr = curr.left

        return None

def main():
    tree = BinarySearchTree()
    actions = [
        ("insert", 2),
        ("insert", 1),
        ("insert", 4),
        ("insert", 3),
        ("insert", 5),
        ("insert", 9),
        ("delete", 2)
    ]

    plt.ion()
    fig, ax = plt.subplots(figsize=(10, 8))
    ax.set_title("Binary Tree", pad=20, size=16)

    for action, val in actions:

        if action == "insert":
            tree.insert(val)
        elif action == "delete":
            tree.delete(val)
        visualize_tree(tree, fig, ax)
        
    plt.ioff()
    plt.show()
    plt.pause(2)
    plt.close('all')



if __name__ == "__main__":
    main()
