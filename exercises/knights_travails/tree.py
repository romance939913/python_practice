import pdb

class Node:
    def __init__(self, value):
        self._value = value
        self._parent = None
        self._children = list()

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
        node.children.append(self)

    def add_child(self, node):
        if node.parent == self or node in self.children:
            return None
        else:
            node.parent = self

    def remove_child(self, node):
        self.children.remove(node)

    def __repr__(self):
        val = None
        if self.parent:
            val = self.parent.value
        return f"<Node {self.value}, children:{len(self.children)}, parent:{val}>"

    
bre = Node('brennan')
der = Node('derek')
ter = Node('terri')
kei = Node('keith')

# pdb.set_trace()
ter.add_child(der)
ter.add_child(bre)

print(bre)
print(ter)
