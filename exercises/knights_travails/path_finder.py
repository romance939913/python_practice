import tree
import pdb

class KnightPathFinder:

    def __init__(self, coord):
        self._root = tree.Node(coord)
        self._considered_positions = { coord }


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
        if pos[0] > 0 and pos[0] < 8 and pos[1] > 0 and pos[1] < 7:
            return True
        return False


    def new_move_positions(self, pos):
        all_moves = self.valid_moves(pos)
        moves = set([ move 
                    for move in all_moves 
                    if move not in self.considered_positions])
        self.considered_positions = moves | self.considered_positions
        return moves
        


b = KnightPathFinder((1, 2))
b.considered_positions.add((2, 3))
b.considered_positions.add((3, 2))
print(b.new_move_positions((4, 4)))
print(b.considered_positions)