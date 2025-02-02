from src.utils.nodes import BaseNode
from src.utils.visualize_tree import visualize_tree

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
        
        curr = self.root
        while True:

            if value == curr.value:
                return

            if value > curr.value:
                if curr.right is None:
                    curr.right = node
                    return
                else:
                    curr = curr.right
            elif value < curr.value:
                if curr.left is None:
                    curr.left = node
                    return
                else:
                    curr = curr.left

    def insert_recursive(self, node, value):
        if node is None:
            return BaseNode(value)
       
        if node.value == value:
            return node

        if value > node.value:
            node.right = self.insert_recursive(node.right, value)
        else:
            node.left = self.insert_recursive(node.left, value)

        return node

    def delete(self, value):
        pass

    def search(self, value):
        pass



def main():
    tree = BinarySearchTree()
    values = [2,1,4,3,5]
    for val in values:
        tree.insert(val)
    visualize_tree(tree)


if __name__ == "__main__":
    main()
