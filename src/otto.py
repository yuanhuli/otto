import pygame
from sys import exit
# drawing the background of the application
pygame.init()
screen = pygame.display.set_mode((850,500))
pygame.display.set_caption('OTTO')
clock = pygame.time.Clock()
text_font = pygame.font.Font('src/fonts/always forever.ttf',70)


home_page = pygame.Surface((850,500))
home_page.fill((249,211,227))
text_surface = text_font.render('OTTO',False,(71,129,195))
splash_image = pygame.image.load('src/images/OTTO.png')

# Show splash screen
screen.blit(splash_image, (0, 0))
pygame.display.flip()
pygame.time.delay(2000)  # Display the splash screen for 2000 milliseconds (2 seconds)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.blit(home_page,(0,0))
    screen.blit(text_surface,(400,50))
    #draw all our elements
    #updat everything
    pygame.display.update()
    clock.tick(60)
    