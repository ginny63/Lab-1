import pygame
pygame.init()

screen = pygame.display.set_mode((800, 600))
screen.fill('white')
pygame.display.set_caption("Circle")

move = 5
ball_x = 400
ball_y = 300

running = True
while running:

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and ball_y > 25:
        ball_y -= move
    if keys[pygame.K_DOWN] and ball_y < 600 - 25:
        ball_y += move
    if keys[pygame.K_LEFT] and ball_x > 25:
        ball_x -= move
    if keys[pygame.K_RIGHT] and ball_x < 800 - 25:
        ball_x += move

    pygame.draw.circle(screen, 'red', (ball_x, ball_y), 25)

    pygame.display.flip()

    screen.fill('white')

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

    pygame.time.Clock().tick(30)