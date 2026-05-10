import pygame
import sys
import random

#this is learned from a tutorial
#I added sound effects

pygame.init()
pygame.mixer.init()

W, H = 800, 800

BLOCK_SIZE = 50
FONT = pygame.font.SysFont("Arial", BLOCK_SIZE * 2)

screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Simulation")
clock = pygame.time.Clock()

eat = pygame.mixer.Sound("eat.wav")
move = pygame.mixer.Sound("move.wav")
lose = pygame.mixer.Sound("lose.wav")

def drawGrid():
    for x in range(0, W, BLOCK_SIZE):
        for y in range(0, H, BLOCK_SIZE):
            rect = pygame.Rect(x,y, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(screen, "#989898", rect, 1)


class Snake:
    def __init__(self):
        self.x, self.y = BLOCK_SIZE, BLOCK_SIZE
        self.xdir = 1
        self.ydir = 0
        self.head = pygame.Rect(self.x,self.y, BLOCK_SIZE, BLOCK_SIZE)
        self.body = [pygame.Rect(self.x-BLOCK_SIZE,self.y, BLOCK_SIZE, BLOCK_SIZE)]
        self.dead = False

    def update(self):
        global apple

        for square in self.body:
            if self.head.x == square.x and self.head.y == square.y:
                self.dead = True
            if self.head.x not in range(0, W) or self.head.y not in range(0, H):
                self.dead = True

        if self.dead:
            self.x, self.y = BLOCK_SIZE, BLOCK_SIZE
            self.head = pygame.Rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE)
            self.body = [pygame.Rect(self.x - BLOCK_SIZE, self.y, BLOCK_SIZE, BLOCK_SIZE)]
            self.xdir = 1
            self.ydir = 0
            self.dead = False
            apple = Apple()
            lose.play()

        self.body.append(self.head)
        for i in range(len(self.body) - 1):
            self.body[i].x, self.body[i].y = self.body[i + 1].x, self.body[i + 1].y
        self.head.x += self.xdir * BLOCK_SIZE
        self.head.y += self.ydir * BLOCK_SIZE
        self.body.remove(self.head)

class Apple:
    def __init__(self):
        self.x = int(random.randint(0, W)/BLOCK_SIZE)*BLOCK_SIZE
        self.y = int(random.randint(0, H)/BLOCK_SIZE)*BLOCK_SIZE
        self.rect = pygame.Rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE)
        eat.play()
    
    def update(self):
        pygame.draw.rect(screen,"red", self.rect)


    
score = FONT.render("1", True, "white")
score_rect = score.get_rect(center = (W/2, H/19))

drawGrid()
snake = Snake()
apple = Apple()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN and snake.ydir != -1:
                snake.ydir = 1
                snake.xdir = 0
            elif event.key == pygame.K_UP and snake.ydir != 1:
                snake.ydir = -1
                snake.xdir = 0
            elif event.key == pygame.K_RIGHT and snake.xdir != -1:
                snake.ydir = 0
                snake.xdir = 1
            elif event.key == pygame.K_LEFT and snake.xdir != 1:
                snake.ydir = 0
                snake.xdir = -1

    snake.update()
    screen.fill("black")
    drawGrid()
    move.play()

    apple.update()

    score = FONT.render(f"{len(snake.body)+1}", True, "white")

    pygame.draw.rect(screen, "#05AF05", snake.head)
    for square in snake.body:
        pygame.draw.rect(screen, "green", square)

    screen.blit(score, score_rect)

    if snake.head.x == apple.x and snake.head.y == apple.y:
        snake.body.append(pygame.Rect(snake.head.x, snake.y, BLOCK_SIZE, BLOCK_SIZE))
        apple = Apple()

    pygame.display.update()
    clock.tick(10)