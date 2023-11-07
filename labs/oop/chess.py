"""Module to define the Chess class. 
"""


class Chess:
    def __init__(self, king=1, queen=1, rooks=2, bishops=2, knights=2, pawns=8):
        self.king = king
        self.queen = queen
        # update the rest of the attributes using the arguments
        self.rooks = 0  # FIXME
        self.bishops = 0  # FIXME
        self.knights = 0  # FIXME
        self.pawns = 0  # FIXME

    def __str__(self):
        return f'{self.king} {self.queen} {self.rooks} {self.bishops} {self.knights} {self.pawns}'

    def __sub__(self, other: 'Chess'):
        k_diff = self.king - other.king
        q_diff = self.queen - other.queen
        r_diff = self.rooks - other.rooks
        # FIXME - update the rest of the attributes' differences
        b_diff = 0  # FIXME
        kn_diff = 0  # FIXME
        p_diff = 0  # FIXME
        return Chess(k_diff, q_diff, r_diff, b_diff, kn_diff, p_diff)
