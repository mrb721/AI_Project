#Piece class to handle each piece individually
class Piece:
    color = ""
    position = (0, 0)

    def __init__(self, newColor, newPos):
        self.color = newColor
        self.position = newPos

   # def moveDecision(self):
        #look all around


#Team class is for handling all pieces collectively
class Team:
    color = ""
    name = ""
    score = 0
    pieces = []
    remainingPieces = len(pieces)
    goals = []

    def __init__(self, newColor, newScore, newName):
        self.color = newColor
        self.score = newScore
        self.name = newName
        #make an array of initial board positions, perhaps it is general enough to use for both teams?
        newPiece = Piece(newColor, 0)
        for p in range (6):
            self.pieces.append(newPiece)


#Should each playing space be its own object?
class Box:
    Index = 0
    Contains = Piece("", "")

    def __init__(self, pos):
        self.Index = pos
        self.Contains = ""




#Gameboard to be played on
class Board:
    Player1 = Team("", 0, "")
    Player2 = Team("", 0, "")
    Bounds = []
    Boxes = []
    WhiteCastlePos = []
    BlackCastlePos = []

    def __init__(self, newP1, newP2):
        self.Player1 = newP1
        self.Player2 = newP2
        #for loop to generate all positions of boxes

    def EndGameByCapture(self):
        if self.Player1.remainingPieces - self.Player2.remainingPieces > 1 and self.Player2.remainingPieces == 0:
            return "Player 1 Wins!"
        elif self.Player2.remainingPieces - self.Player1.remainingPieces > 1 and self.Player1.remainingPieces == 0:
            return "Player 2 Wins!"
        else:
            return

  #  def EndGameByCastle(self, piece):
   #     if (self.Player1.pieces[piece].position == self.Player1.goals[0]):







class Game:
    gameBoard = Board("", "")

    def __init__(self, newBoard):
        self.gameBoard = newBoard



#eval function can be found in adversarial search ppt
def alphabeta_search(state, game, d=4, cutoff_test=None, eval_fn=None):
    """Search game to determine best action; use alpha-beta pruning.
    This version cuts off search and uses an evaluation function."""

    player = game.to_move(state)

    def max_value(state, alpha, beta, depth):
        if cutoff_test(state, depth):
            return eval_fn(state)
        v = -1000
        for (a, s) in game.successors(state):
            v = max(v, min_value(s, alpha, beta, depth+1))
            if v >= beta:
                return v
            alpha = max(alpha, v)
        return v

    def min_value(state, alpha, beta, depth):
        if cutoff_test(state, depth):
            return eval_fn(state)
        v = 1000
        for (a, s) in game.successors(state):
            v = min(v, max_value(s, alpha, beta, depth+1))
            if v <= alpha:
                return v
            beta = min(beta, v)
        return v

    # Body of alpha-beta_search starts here:
    # The default test cuts off at depth d or at a terminal state
    cutoff_test = (cutoff_test or
                   (lambda state,depth: depth>d or game.terminal_test(state)))
    eval_fn = eval_fn or (lambda state: game.utility(state, player))
    action, state = argmax(game.successors(state),
                           lambda ((a, s)): min_value(s, -1000, 1000, 0))
    return action
