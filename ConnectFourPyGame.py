import pygame
import random
from pygame import mixer

rows = 6
columns = 7
grid = [" "] * 7, [" "] * 7, [" "] * 7, [" "] * 7, [" "] * 7, [" "] * 7
PlayerPieceX = 71
PlayerPieceY = 82
PlayerPieceY2 = 82
PlayerPieceX2 = 71
finalpos = 0
User1Win = False
User2Win = False
CPUWin = False
n = 0
MoveNum = 0


rect_surface = pygame.Surface((800, 700), pygame.SRCALPHA)
rect_color = (80, 80, 80, 150)
pygame.draw.rect(rect_surface, rect_color, rect_surface.get_rect())

def GameBoard():

    for i in range(rows):
        for x in range(columns):
            if grid[i][x] == " ":
                screen.blit(Emptyboardslot, (55 + (100 * x), 70 + (92 * i) ))
            if grid[i][x] == 0:
                screen.blit(Redboardslot, (55 + (100 * x), 70 + (92 * i) ))
            if grid[i][x] == 1:
                screen.blit(Yellowboardslot, (55 + (100 * x), 70 + (92 * i) ))

def UserEntry():

    global PlayerPieceY
    global PlayerPieceX
    global finalpos
    global count
    global ColumnNum
    global LastMoveColumn
    global LastMoveRow
    global ValidMoveMade
    global MoveNum

    ColumnNum = (PlayerPieceX // 100)
    count = 5
    Empty = True

    while Empty == True:

        if grid[count][ColumnNum] == " ":
            finalpos = PlayerPieceY + (92 * (count))
            LastMoveRow = count
            LastMoveColumn = ColumnNum
            ValidMoveMade = True
            MoveNum = MoveNum + 1
            return True
        else:
            count = count - 1
        
        if count < 0:
            break

    if Empty == True:
        ValidMoveMade = False
        return False
      
def UpdateGameBoard():
    global LastMoveRow
    global LastMoveColumn
    global PlayerPieceY
    global PlayerPieceX
    global ValidMoveMade
    global PlayerPieceY2
    global PlayerPieceX2

    if ValidMoveMade == True:
        if MoveNum % 2 == 0:
            grid[LastMoveRow][LastMoveColumn] = 1
        elif MoveNum % 2 == 1:
            grid[LastMoveRow][LastMoveColumn] = 0

        PlayerPieceX = 71
        PlayerPieceY = 82
        PlayerPieceX2 = 71
        PlayerPieceY2 = 82

def CheckWin():
    global LastMoveRow
    global LastMoveColumn
    InARow = 0

# Checks Vertical (up & down)

    for i in range(1, 4):
        try:
            if LastMoveRow - i < 0:
                break
            if grid[LastMoveRow][LastMoveColumn] == grid[LastMoveRow - i][LastMoveColumn]:
                InARow = InARow + 1
            else:
                break
        except:
            pass

    for i in range(1, 4):
        try:
            if LastMoveRow + i > 5:
                break
            if grid[LastMoveRow][LastMoveColumn] == grid[LastMoveRow + i][LastMoveColumn]:
                InARow = InARow + 1
            else:
                break
        except:
            pass

    if InARow < 3:
        InARow = 0

# Check Row (left & right)

    for y in range(1, 4):
        try:
            if LastMoveColumn - y < 0:
                break

            if grid[LastMoveRow][LastMoveColumn] == grid[LastMoveRow][LastMoveColumn - y]:
                InARow = InARow + 1
            else:
                break
        except:
                pass
        
    for y in range(1, 4):
            
            if LastMoveColumn + y > 6:
                break

            try:   
                if grid[LastMoveRow][LastMoveColumn] == grid[LastMoveRow][LastMoveColumn + y]:
                    InARow = InARow + 1
                else:
                    break
            except:
                pass
    if InARow < 3:
        InARow = 0

#Check Diagonal
    for y in range(1, 4):
        if LastMoveRow + y > 5 or LastMoveColumn - y < 0:
            break
        try:
            if grid[LastMoveRow][LastMoveColumn] == grid[LastMoveRow + y][LastMoveColumn - y]:
                InARow = InARow + 1
            else:
                break
        except:
                pass
        
    for y in range(1, 4):
        if LastMoveRow - y < 0 or LastMoveColumn + y > 6:
            break
        try:   
            if grid[LastMoveRow][LastMoveColumn] == grid[LastMoveRow - y][LastMoveColumn + y]:
                InARow = InARow + 1
            else:
                break
        except:
                pass
    if InARow < 3:
        InARow = 0        
    
    for y in range(1, 4):
        if LastMoveRow + y > 5 or LastMoveColumn + y > 6:
            break
        try:
            if grid[LastMoveRow][LastMoveColumn] == grid[LastMoveRow + y][LastMoveColumn + y]:
                InARow = InARow + 1
            else:
                break
        except:
                pass
    
    for y in range(1, 4):
        if LastMoveRow - y < 0 or LastMoveColumn - y < 0:
            break
        try:
            if grid[LastMoveRow][LastMoveColumn] == grid[LastMoveRow - y][LastMoveColumn - y]:
                InARow = InARow + 1
            else:
                break
        except:
                pass

    if InARow < 3:
        InARow = 0
    
    if InARow >= 3:
        return True
    else:
        return False

def ComMove(Move):
    """
    NOT IN USE

    Makes a computer make random move and prints game board after move

    Parameters: Move, grid #Array, rows, columns
    
    """

    global LastMoveRow
    global LastMoveColumn
    global ValidMoveMade
    Empty = True
    count2  = 5
    while Empty == True:

        if grid[count2][Move] == " ":
            grid[count2][Move] = 0
            Empty = False
            LastMoveRow = count2
            LastMoveColumn = Move
            ValidMoveMade = True

        else:
            count2 = count2 - 1

        if count2 < 0:
            break

    if Empty == True:
        ValidMoveMade = False

def UserEntry2():

    global PlayerPieceY
    global PlayerPieceX
    global finalpos
    global count2
    global ColumnNum
    global LastMoveColumn
    global LastMoveRow
    global ValidMoveMade
    global MoveNum

    ColumnNum = (PlayerPieceX2 // 100)
    count2 = 5
    Empty = True

    while Empty == True:

        if grid[count2][ColumnNum] == " ":
            finalpos = PlayerPieceY2 + (92 * (count2))
            LastMoveRow = count2
            LastMoveColumn = ColumnNum
            ValidMoveMade = True
            MoveNum = MoveNum + 1
            return True
        else:
            count2 = count2 - 1
        
        if count2 < 0:
            break

    if Empty == True:
        ValidMoveMade = False
        return False



# Game initialize
pygame.init()

 # Create Screen
screen = pygame.display.set_mode((800, 700))

# Title & Icon
pygame.display.set_caption("Connect Four")
icon = pygame.image.load('Pictures/Connect4icon.png')
pygame.display.set_icon(icon)

# Load Images
Emptyboardslot = pygame.image.load('Pictures/EmptyPixel.png')
Redboardslot = pygame.image.load('Pictures/RedPixel.png')
Yellowboardslot = pygame.image.load('Pictures/YellowPixel.png')
PlayerPiece = pygame.image.load('Pictures/Player2.png')
background = pygame.image.load('Pictures/connect4background.png')
RWin = pygame.image.load('Pictures/RedWin Image.png')
LWin = pygame.image.load('Pictures/YellowWin Image.png')
PlayerPiece2 = pygame.image.load('Pictures/Player1.png')
GameOver = pygame.image.load('Pictures/game over.png')

# Load Audio
mixer.music.load('Audio/BackgroundM.mp3')
mixer.music.play(-1)
selectsound = mixer.Sound('Audio/select.wav')
dropsound = mixer.Sound('Audio/drop.wav')
WinSound = mixer.Sound('Audio/win.wav')
Error = mixer.Sound('Audio/error.wav')
Loss = mixer.Sound('Audio/GameOver.wav')

# Game Loop
running = True
while running == True:
    screen.fill((28, 1, 37))
    screen.blit(background, (0,0))

    if User1Win == False and User2Win == False:

        if MoveNum % 2 == 0:
            GameBoard()
            screen.blit(PlayerPiece, (PlayerPieceX, PlayerPieceY))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        if PlayerPieceX == 671:
                            PlayerPieceX = -29
                            selectsound.play()
                        PlayerPieceX = PlayerPieceX + 100
                        selectsound.play()
                    if event.key == pygame.K_LEFT:
                        if PlayerPieceX == 71:
                            PlayerPieceX = 771
                            selectsound.play()
                        PlayerPieceX = PlayerPieceX - 100
                        selectsound.play()
                    if event.key == pygame.K_SPACE:
                        UserEntry()
                        if ValidMoveMade ==  True:
                            dropsound.play()
                            GameBoard()
                            while PlayerPieceY != finalpos:
                                PlayerPieceY += 0.5
                                screen.blit(PlayerPiece, (PlayerPieceX, PlayerPieceY))
                            
                            UpdateGameBoard()
                            if CheckWin() == True:
                                User1Win = True
                                break
                            # Code if Computer was playing instead of 2 humans:
                            # ComMove(random.randint(0, 6))
                            # while ValidMoveMade == False:
                               # ComMove(random.randint(0, 6))
                             #if CheckWin() == True:
                               # CPUWin = True
                                
                        else:
                            Error.play()
            
            screen.blit(PlayerPiece, (PlayerPieceX, PlayerPieceY))
            GameBoard()
        
        if MoveNum % 2 == 1:
            GameBoard()
            screen.blit(PlayerPiece2, (PlayerPieceX2, PlayerPieceY2))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        if PlayerPieceX2 == 671:
                            PlayerPieceX2 = -29
                            selectsound.play()
                        PlayerPieceX2 = PlayerPieceX2 + 100
                        selectsound.play()
                    if event.key == pygame.K_LEFT:
                        if PlayerPieceX2 == 71:
                            PlayerPieceX2 = 771
                            selectsound.play()
                        PlayerPieceX2 = PlayerPieceX2 - 100
                        selectsound.play()
                    if event.key == pygame.K_SPACE:
                        UserEntry2()
                        if ValidMoveMade ==  True:
                            dropsound.play()
                            GameBoard()
                            while PlayerPieceY2 != finalpos:
                                PlayerPieceY2 += 0.5
                                screen.blit(PlayerPiece2, (PlayerPieceX2, PlayerPieceY2))
                            
                            UpdateGameBoard()
                            if CheckWin() == True:
                                User2Win = True
                                break
                                
                        else:
                            Error.play()
            screen.blit(PlayerPiece2, (PlayerPieceX2, PlayerPieceY2))
            GameBoard()
        
        if MoveNum == 42:
            while n < 1:
                pygame.mixer.music.pause()
                Loss.play(0)
                n = 2
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            GameBoard()
            screen.blit(rect_surface, (0,0))
            screen.blit(GameOver, (178, 230))
           

    elif User1Win == True:
        while n < 1:
            pygame.mixer.music.pause()
            WinSound.play(0)
            n = 2
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        GameBoard()
        screen.blit(rect_surface, (0, 0))
        screen.blit(RWin, (120, 280))
    
    elif User2Win == True:
        while n < 1:
            pygame.mixer.music.pause()
            WinSound.play(0)
            n = 2
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        GameBoard()
        screen.blit(rect_surface, (0, 0))
        screen.blit(LWin, (35, 300))
        pygame.display.update()



    pygame.display.update()


