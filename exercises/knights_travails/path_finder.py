import tree
import pdb

class KnightPathFinder:

    def __init__(self, coord):
        self._node = tree.Node(coord)
        self._considered_positions = { coord }

    @property
    def node(self):
        return self._node

    @property
    def considered_positions(self):
        return self._considered_positions

    @considered_positions.setter
    def considered_positions(self, new_positions):
        self._considered_positions = new_positions


    def valid_moves(self, pos):
        moves = [           
            (pos[0] + 1, pos[1] + 2),
            (pos[0] + 1, pos[1] - 2),
            (pos[0] - 1, pos[1] + 2),
            (pos[0] - 1, pos[1] - 2),
            (pos[0] + 2, pos[1] - 1),
            (pos[0] + 2, pos[1] + 1),
            (pos[0] - 2, pos[1] - 1),
            (pos[0] - 2, pos[1] + 1)
        ]
        result = [pos for pos in moves if self.helper_valid(pos)]
        return result


    def helper_valid(self, pos):
        if pos[0] >= 0 and pos[0] < 8 and pos[1] >= 0 and pos[1] < 8:
            return True
        return False


    def new_move_positions(self, pos):
        all_moves = self.valid_moves(pos)
        moves = set([ tree.Node(move)
                    for move in all_moves 
                    if move not in self.considered_positions])
        self.considered_positions = set(all_moves) | self.considered_positions
        return moves
        

    def build_move_tree(self):
        queue = [self.node]
        while queue:
            ele = queue[0]
            queue = queue[1:]
            moves = self.new_move_positions(ele.value)
            for move_node in moves:
                queue.append(move_node)
                ele.children.append(move_node)
        return None           
            


b = KnightPathFinder((1, 2))
pdb.set_trace()
print(b.node)
print(b.build_move_tree())
