import pygame
import random

class Block:
    def __init__(self, x, y):
        
        self.x = x
        self.y = y
        self.color = white
        self.points = 1
        self.hitsLeft = 1
        self.width = 99
        self.height = 20
        self.rect = pygame.rect.Rect([self.x, self.y], [self.width, self.height])

    def hit(self):
        self.hitsLeft -= 1
        
        if self.hitsLeft == 0:
            return True
        else:
            return False
    
    def moveTo(self):
        pass
    
    def draw(self):
        pygame.draw.rect(window, self.color, self.rect)

def reset():
    global location
    location = [screen_size[0]//2, screen_size[1]//2]

def drawScore():
    global Score, white, top, Lives
    ScoreText = GameFont.render(str(Score), True, white)
    NameText = GameFont.render(str(PlayerName), True, white)
    LivesText = GameFont.render(str("Lives: ")+str(Lives), True, white)
    GameOverText = GameFont.render(GameOver, True, white)
    
    window.blit(ScoreText, (screen_size[0]//2-30, 30))
    window.blit(GameOverText, (screen_size[0]//2-127, screen_size[1]//2+20))
    window.blit(NameText, (20, 30))
    window.blit(LivesText, (350, 30))
    pygame.draw.line(window, white, (0,top), (screen_size[0], top))
    

def Collide(pad, padSpeed):
    global speed, ball
    
    #print("Ball: ", ball.bottom)
    #print("Pad: ", pad.top)
    
    if ball.colliderect(pad):
        speed[1] = -speed[1]
        speed[0] += 0.5*padSpeed
    #print("speed: ", speed)

def drawBlock(Block):
    
    pygame.draw.rect(window, white, Block)

def drawBall():
    global white, GameOver, Lives, location, radius, thickness, screen_size, speed, leftScore, rightScore, ball
    #If the ball hits the right edge of screen bounce.
    location[1] += speed[1]
    location[0] += speed[0]
    
    ball = pygame.draw.circle(window, white, location, radius, thickness)
    
    #If ball hits right side, bounce it
    if ball.right >= screen_size[0]:
        speed[0] = -speed[0]
    #If the ball hits the left side then bounce
    if ball.left <= 0:
        speed[0] = -speed[0]
    # If the ball hits the bottom of the screen
    if ball.bottom >= screen_size[1]:
        #speed[1] = -speed[1]
        print("bottom screen triggered")
        #Right HERE decrement the lives by 1
        Lives -=1
        #Reset the ball
        reset()
        speed= [0,0]
        #If you run out of lives, stop the ball, Give a game over screen
        if Lives <= 0:
            GameOver="Game Over"
    # If the ball hits the top of the screen
    if ball.top <= top:
        speed[1] = -speed[1]
        print("top screen triggered")
        
    
    
def drawPaddleA():
    global blue, padA, aSpeed
    if padA.left <= 0 and aSpeed < 0:
        aSpeed = 0
    if padA.right >= screen_size[0] and aSpeed > 0:
        aSpeed = 0
    padA = padA.move(aSpeed, 0)
    padA = pygame.draw.rect(window, blue, padA)

timer = pygame.time.Clock()

#Screen Properties
screen_size = [600,800]
top = 100 #Where the line on the top goes
#This makes a window
window = pygame.display.set_mode(screen_size)

#Ball Attributes
speed = [3, 3]
radius = 20
location = [500, 300]
thickness = 0

#Colors
black = (0,0,0)
white = (255, 255, 255)
orange = (235, 140, 52)
yellow = (247, 244, 37)
green = (99, 204, 51)
blue = (51, 117, 204)
purple = (173, 51, 204)
red = (184, 7, 31)

#PaddleA Attributes
aSpeed = 0
leftTop = [screen_size[0]//2, screen_size[1]-30]
widthHeight = [100, 30]
blue = (0, 0, 255)
padA = pygame.Rect(leftTop, widthHeight)


#Scoring Attributes
#print(pygame.font.get_fonts())
pygame.font.init()
GameFont = pygame.font.SysFont("consolas", 52)
Score = 0
Lives = 3
ball = pygame.draw.circle(window, white, location, radius, thickness)
GameOver=""
#Block
Block1 = Block(0,top)
Block1.color = yellow
Block1.points = 5
Block1.hitsLeft = 3

Block2 = Block(100,top)
Block2.color = orange
Block2.points = 4
Block2.hitsLeft = 2

Block3 = Block(200,top)
Block3.color = green
Block3.points = 3
Block3.hitsLeft = 2

Block4 = Block(300,top)
Block4.color = blue
Block4.points = 2


Block5 = Block(400,top)
Block5.color = purple
Block5.points = 1

Block6 = Block(500,top)
Block6.color = yellow
Block6.points = 5
Block6.hitsLeft = 3

Block7 = Block(0,top+21)
Block7.color = orange
Block7.points = 4
Block7.hitsLeft = 2

Block8 = Block(100,top+21)
Block8.color = green
Block8.points = 3
Block8.hitsLeft = 2

Block9 = Block(200,top+21)
Block9.color = blue
Block9.points = 2

Block10 = Block(300,top+21)
Block10.color = purple
Block10.points = 1

Block11 = Block(400,top+21)
Block11.color = yellow
Block11.points = 5
Block11.hitsLeft = 3

Block12 = Block(500,top+21)
Block12.color = orange
Block12.points = 4
Block12.hitsLeft = 2

Blocks = [Block1, Block2, Block3,Block4,Block5,Block6,Block7,Block8,Block9,Block10,Block11,Block12]

PlayerName = input("Player Name:")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit = True
            pygame.quit()
            sys.exit(0)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                aSpeed = 4
                #print("Right")
            elif event.key == pygame.K_LEFT:
                aSpeed = -4
                
            elif event.key == pygame.K_SPACE:
                print("Space")
                xvar = random.randint(-3,3)
                speed = [xvar,3]
                
            elif event.key == pygame.K_r:
                print("r")
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                aSpeed = 0
        
    
    window.fill(black)
    #Is the ball colliding with the paddle?
    Collide(padA, aSpeed)
    drawBall()
    drawPaddleA()
    drawScore()

    for Block in Blocks:
        if ball.colliderect(Block):
            if Block.hit():
                Blocks.remove(Block)
                Score += Block.points
            speed[1] = -speed[1]
        Block.draw()
        
    pygame.display.flip()
    timer.tick(60)