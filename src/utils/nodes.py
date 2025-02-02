class BaseNode():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class RedBlackNode(BaseNode):
    def __init__(self, value):
        super().__init__(value)
        self.red = True
        self.parent = None
