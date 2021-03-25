class Node:
    
    def __init__(self, value):
        self._value = value
        self._children = list()
        self._parent = None

    @property
    def value(self):
        return self._value
    
    @property
    def children(self):
        return self._children

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, node):
        if self.parent:
            self.parent.remove_child(self)
        self._parent = node
        if node:
            node.add_child(self)


    def add_child(self, node):
        if not node in self.children:
            self.children.append(node)
        

    def remove_child(self, node):
        if node in self.children:
            self.children.remove(node)


    def depth_search(self, value):
        if self.value == value:
            return self
        elif not self:
            return None
        for child in self.children:
            node = child.depth_search(value)
            if node:
                return node
        return None


    def breadth_search(self, value):
        queue = [self]
        while queue:
            node = queue[0]
            queue = queue[1:]
            if node.value == value:
                return node
            else:
                for child in node.children:
                    queue.append(child)
        return None


    def __repr__(self):
        parent_val = None
        if self.parent:
            parent_val = self.parent.value
        return f"<Node {self.value}, children:{len(self.children)}, parent:{parent_val}>"


