# Import Libraries

import numpy as np
import argparse
import cv2
import regions
import tictactoe
import time
import pygame
import serial

# define video port here, usually 0
VIDEPORT = 1
done = 1

# Define Game Methods

# returns the position and the size of the circles found
def findCircles(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.blur(gray,(5,5))
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1.3, 100, param1=30, param2=65, minRadius=50, maxRadius=70)
    return circles

# returns the move of the opponent
def findMove(image, circles):
    
    # convert coordinates to integer
    circles = np.round(circles[0, :]).astype("int")
    opponentMove = 0

    # iterate all circles found
    for (x, y, r) in circles: 
        isMoved = True
        
        # check which region the found circle belongs to
        if((x >= regions.minX) and (x <= regions.maxX)) and ((y >= regions.minY) and (y <= regions.maxY)):
            region = regions.checkRegion(x,y)
        else:
            break

        # iterate all available moves
        for move in board.availableMoves():
            
            # if the region has'nt been occupied, take it as the opponent's move
            if move + 1  == region:
                isMoved = False
                break
            # do nothing if the region has been occupied before
            else:
                pass

        if not isMoved:
            opponentMove = region - 1
            isMoved = True
            return opponentMove

# returns the next best move for the arm
def nextMove(opponentMove):
    
    player = 'O'
    # save the opponent's move in the list
    board.makeMove(opponentMove, player)
    print("Opponent Move: ", opponentMove + 1)
    board.show()
    
    # play a beep sound the acknowldge the opponent's move
    pygame.mixer.music.load("beep.wav")
    pygame.mixer.music.play()
    if board.complete():
        return 20
    
    # get the next best move based on the opponent's move
    player = tictactoe.getEnemy(player)
    computerMove = tictactoe.determine(board, player)

    # save the computer's move in the list
    board.makeMove(computerMove, player)
    print("Computer Move: ", computerMove + 1)
    board.show()
    return computerMove + 1

# Define GUI Methods

# draws all the tic-tac-toe squares on the frame
def drawRegions(image):
    '''
    sample data
    [0, 213, 426, 639]
    [0, 160, 320, 480]
    r1 = (0   , 0  ) (213  , 160)
    r2 = (213 , 0  ) (426  , 160)
    r3 = (426 , 0  ) (640  , 160)

    r4 = (0 ,  160 ) (213, 320)
    r5 = (213, 160 ) (426, 320)
    r6 = (426, 160 ) (640, 320)

    r7 = (0, 320 ) (213, 480)
    r8 = (213, 320 ) (426, 480)
    r9 = (426, 320 ) (640, 480)
    '''
    fontIndex = 0
    for i in range(regions.totalYintercepts-1):
        for ii in range(regions.totalXintercepts-1):
            x1 = regions.xIntercepts()[ii]
            x2 = regions.xIntercepts()[ii + 1]
            y1 = regions.yIntercepts()[i]
            y2 = regions.yIntercepts()[i+1]
            
            # draw the rectangles
            cv2.rectangle(image,(int(x1),int(y1)),(int(x2),int(y2)),(0,255,0),2)
            fontIndex = fontIndex + 1
            
            #draw the labels
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(image,str(fontIndex),(int(x1) +5,int(y1)+25), font, 0.7,(255,255,255),2)

# draws all the opponent's moves on the frame
def drawOpponentMoves(image):
    for move in board.getSquares('O'):
        x = regions.center()[move][0]
        y = regions.center()[move][1]
        cv2.circle(image, (int(x), int(y)), 40, (0, 0, 255), 10)

# draws all the computer's moves on the frame
def drawComputerMoves(image):
    for move in board.getSquares('X'):
        x = regions.center()[move][0]
        y = regions.center()[move][1]
        cv2.rectangle(image, (int(x) - 40, int(y) - 40), (int(x) + 40, int(y) + 40), (255, 0, 0), 10)

# Define Main 

def main():
    global done
    turn = 0
    frame_rate = 10
    prev = 0
    counter = 0
    pygame.init()
    
    # continue looping until there's a winner
    while not board.complete():

        # get the frame from the video feed
        time_elapsed = time.time() - prev
        ret, image = videoCapture.read()
        if not time_elapsed > 1./frame_rate:
            continue
        prev = time.time()

        # find the circles on the frame
        circles = findCircles(image)
        
        if circles is not None and counter >= 10:

            # get opponent's move
            counter = 0
            opponentMove = findMove(image, circles)
            if not opponentMove in board.availableMoves():
                continue
            
            # calculate what's the next move
            time.sleep(5)
            computerMove = nextMove(opponentMove)
            if computerMove == 20:
                break

            if turn <= 3:
                
                # start the arm procedures
                turn = turn + 1
                if computerMove == 1:
                    ser.write(b'A')
                elif computerMove == 2:
                    ser.write(b'B')
                elif computerMove == 3:
                    ser.write(b'C')
                elif computerMove == 4:
                    ser.write(b'D')
                elif computerMove == 5:
                    ser.write(b'E')
                elif computerMove == 6:
                    ser.write(b'F')
                elif computerMove == 7:
                    ser.write(b'G')
                elif computerMove == 8:
                    ser.write(b'H')
                elif computerMove == 9:
                    ser.write(b'I')
                while (ser.inWaiting() < 0): 
                    time.sleep(0.1)
                confirm = ser.read()
                ser.flushInput()
                      
            # end the game if there's any winner
            if board.complete():
                break

        # draw opponent's and computer's move on the screen
        counter = counter + 1
        drawComputerMoves(image)
        drawOpponentMoves(image)
        drawRegions(image)
        cv2.imshow('TICTACTOE',image)
        cv2.setWindowProperty('TICTACTOE',cv2.WND_PROP_TOPMOST,1)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            done = 0
            break

    print("winner is", board.winner())
    copy = None
    while(counter <= 10):
    
        # get the frame from the video feed
        time_elapsed = time.time() - prev
        ret, image = videoCapture.read()
        if not time_elapsed > 1./frame_rate:
            continue
        prev = time.time()
        counter = counter + 1
        drawComputerMoves(image)
        drawOpponentMoves(image)
        drawRegions(image)
        cv2.imshow('TICTACTOE',image)
        cv2.waitKey(1)

    time.sleep(5)
    pygame.mixer.music.load("beep2.wav")
    pygame.mixer.music.play()
    videoCapture.release()
    cv2.destroyAllWindows()

# Run Main/Game

if __name__ == "__main__":
    ser = serial.Serial(port='COM5', baudrate=9600, timeout=1)
    regions = regions.Regions(50,500,500,50,3,3)
    while(done):
        videoCapture = cv2.VideoCapture(VIDEPORT)
        videoCapture.set(cv2.CAP_PROP_FPS, 10)    
        board = tictactoe.Tic()
        image = None
        main()

