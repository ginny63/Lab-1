import pygame
pygame.init()

weight = 800
height = 600
screen = pygame.display.set_mode((weight, height))
pygame.display.set_caption('Player')
image = pygame.image.load(r'C:\Users\kairb\Desktop\LAB7\Second project\images\a.jpg')
image_scaled = pygame.transform.scale_by(image, 0.5)
center = (weight/2, height/2)
pause = True
playlist = ['bad_habits', 'perfect', 'save_your_tears', 'shape_of_you']
index = 0
vol = 0.1
pygame.mixer.music.set_volume(vol)
pygame.mixer.music.load(r"C:\Users\kairb\Desktop\LAB7\Second project\musics\bad_habits.mp3")
pygame.mixer.music.play(-1)


running = True
while running:

    image_rec = image_scaled.get_rect(center=center)
    screen.blit(image_scaled, image_rec.topleft)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if pause:
                    pygame.mixer_music.pause()
                    pause = False
                else:
                    pygame.mixer_music.unpause()
                    pause = True
            elif event.key == pygame.K_RIGHT and index <= 2:
                pygame.mixer.music.stop()
                index += 1
                pygame.mixer.music.load(r"C:\Users\kairb\Desktop\LAB7\Second project\musics\perfect.mp3")
                pygame.mixer.music.play(-1)
            elif event.key == pygame.K_LEFT and index >= -1:
                pygame.mixer.music.stop()
                index -= 1
                pygame.mixer.music.load(r"C:\Users\kairb\Desktop\LAB7\Second project\musics\{shape_of_you.mp3")
                pygame.mixer.music.play(-1)
            elif event.key == pygame.K_UP:
                vol += 0.1
                pygame.mixer.music.set_volume(vol)
                print(pygame.mixer.music.get_volume())
            elif event.key == pygame.K_DOWN:
                vol -= 0.1
                pygame.mixer.music.set_volume(vol)
                print(pygame.mixer.music.get_volume())