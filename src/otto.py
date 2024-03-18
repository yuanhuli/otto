import time,pygame
import button
from sys import exit
# drawing the background of the application
pygame.init()
screen = pygame.display.set_mode((850,500))
pygame.display.set_caption('OTTO')
clock = pygame.time.Clock()
text_font = pygame.font.Font('fonts/always forever.ttf',70)
theFont = pygame.font.Font(None,70)



home_page = pygame.Surface((850,500))
home_page.fill((249,211,227))
text_surface = text_font.render('OTTO',False,(71,129,195))
splash_image = pygame.image.load('images/OTTO.png')

# Show splash screen
screen.blit(splash_image, (0, 0))
pygame.display.flip()
pygame.time.delay(2000)  # Display the splash screen for 2000 milliseconds (2 seconds)

#button
#load in images
chatbot_img = pygame.image.load('images/button (1).png').convert_alpha()
calendar_img = pygame.image.load('images/button (2).png').convert_alpha()

#button class
#create button instances
chatbot_button = button.Button(300,150,chatbot_img,0.25)
calendar_button = button.Button(650,50,calendar_img,0.1)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.blit(home_page,(0,0))
    screen.blit(text_surface,(400,50))
    #make button
    
    #make clock
    clock.tick(1)
    theTime = time.strftime("%H:%M:%S", time.localtime())
    timeText = theFont.render(str(theTime), True, (249,211,227), (71,129,195))
    screen.blit(timeText, (80, 60))
    #draw all our elements
    if chatbot_button.draw(screen) == True:
        print("talk")
    if calendar_button.draw(screen) == True:
        print("calendar")
    #updat everything
    pygame.display.update()
    clock.tick(60)
    
