class Tic(object):
    winningCombos = (
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6])

    
    def __init__(self, squares=[]):
        if len(squares) == 0:
            self.squares = [0 for i in range(9)]
        else:
            self.squares = squares
            
    #This function is used to draw the board's current state every time the user turn arrives. 
    def show(self):
        print("Current State Of Board : \n\n");
        for i in range (0,9):
            if((i>0) and (i%3)==0):
                print("\n")
            if(self.squares[i]==0):
                print("- ",end=" ")
            if (self.squares[i]==1):
                print("X ",end=" ")
            if(self.squares[i]==-1):    
                print("O ",end=" ")
        print("\n\n")
    

    def availableMoves(self):
        # returns all the available moves from 0 - 8
        """what spots are left empty?"""
        return [k for k, v in enumerate(self.squares) if v == 0]

    
    def complete(self):
        # Check if the game is over yet
        """is the game over?"""
        if 0 not in [v for v in self.squares]:
            return True
        if self.winner() != None:
            return True
        return False

    
    def winner(self):
        for player in (1, -1):
            positions = self.getSquares(player)
            for combo in self.winningCombos:
                win = True
                for pos in combo:
                    if pos not in positions:
                        win = False
                if win:
                    if player == -1:
                        return "O"
                    else:
                        return "X"
        return None

    def getSquares(self, player):
        """squares that belong to a player"""
        return [k for k, v in enumerate(self.squares) if v == player]

    def makeMove(self, position, player):
        """place on square on the board"""
        self.squares[position] = player

    
    #MinMax function.
    def minimax(self,player):
        x=self.analyzeboard()
        if(x!=0):
            return (x*player)
        pos=-1
        value=-2
        for i in range(0,9):
            if(self.squares[i]==0):
                self.squares[i]=player
                score=-self.minimax(player*-1)
                if(score>value):
                    value=score
                    pos=i
                self.squares[i]=0;

        if(pos==-1):
            return 0;
        return value;
    
    #This function makes the computer's move using minmax algorithm.
    def compTurn(self):
        pos=-1
        value=-2
        for i in range(0,9):
            if(self.squares[i]==0):
                self.squares[i]=1
                score=-self.minimax(-1)
                self.squares[i]=0
                if(score>value):
                    value=score
                    pos=i
        return pos

    #This function is used to analyze a game.
    def analyzeboard(self):
        cb=self.winningCombos
        for i in range(0,8):
            if(self.squares[cb[i][0]] != 0 and self.squares[cb[i][0]] == self.squares[cb[i][1]] and self.squares[cb[i][0]] == self.squares[cb[i][2]]):
                return self.squares[cb[i][2]]
        return 0

def getEnemy(player):
        if player == 1:
            return -1
        return 1
    
