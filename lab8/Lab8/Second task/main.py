import pygame
import random

pygame.init()

WIDTH, HEIGHT = 600, 400
GRIDSIZE = 20
GRIDWIDTH, GRIDHEIGHT = WIDTH // GRIDSIZE, HEIGHT // GRIDSIZE

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

def drawtext(surface, text, size, x, y):
    font = pygame.font.SysFont('Arial', size)
    textsurface = font.render(text, True, WHITE)
    textrect = textsurface.get_rect()
    textrect.center = (x, y)
    surface.blit(textsurface, textrect)

def drawapple(surface, apple):
    pygame.draw.rect(surface, RED, (apple[0]*GRIDSIZE, apple[1]*GRIDSIZE, GRIDSIZE, GRIDSIZE))

def drawsnake(surface, snake):
    for seg in snake:
        pygame.draw.rect(surface, WHITE, (seg[0]*GRIDSIZE, seg[1]*GRIDSIZE, GRIDSIZE, GRIDSIZE))

def main():

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Snake')

    snake = [(GRIDWIDTH // 2, GRIDHEIGHT // 2)]
    snake_direction = RIGHT
    apple = (random.randint(0, GRIDWIDTH-1), random.randint(0, GRIDHEIGHT-1))
    running = True
    sum_food = 0
    level = 1
    delay = 110
    food_collec = 0

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake_direction != DOWN:
                    snake_direction = UP
                elif event.key == pygame.K_DOWN and snake_direction != UP:
                    snake_direction = DOWN
                elif event.key == pygame.K_LEFT and snake_direction != RIGHT:
                    snake_direction = LEFT
                elif event.key == pygame.K_RIGHT and snake_direction != LEFT:
                    snake_direction = RIGHT

        newhead = (snake[0][0] + snake_direction[0], snake[0][1] + snake_direction[1])
        snake.insert(0, newhead)

        if not (0 <= newhead[0] < GRIDWIDTH) or not (0 <= newhead[1] < GRIDHEIGHT):
            running = False

        if len(snake) != len(set(snake)):
            running = False

        if newhead == apple:
            apple = (random.randint(0, GRIDWIDTH-1), random.randint(0, GRIDHEIGHT-1))
            sum_food += 1
            food_collec += 1
        else:
            snake.pop()

        screen.fill(BLACK)
        drawsnake(screen, snake)
        drawapple(screen, apple)
        drawtext(screen, f"Your level: {level}", 20, WIDTH - 60, 30)
        drawtext(screen, f"Foods collected: {food_collec}", 20, WIDTH - 80, 60)
        pygame.display.flip()

        if sum_food == 3:
            sum_food = 0
            level += 1
            delay = delay - 10

        pygame.time.delay(delay)

    screen.fill(BLACK)
    drawtext(screen, "Game Over", 50, WIDTH//2, HEIGHT//2)
    pygame.display.flip()
    pygame.time.delay(2000)

    # Закрыть окно
    pygame.quit()

main()