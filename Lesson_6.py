import pygame

pygame.init()

WIDTH = 96
HEIGHT = 96

display = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("ball")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            
    frame1 = pygame.image.load("BallFrames/BallFrame1.png")
    frame2 = pygame.image.load("BallFrames/BallFrame2.png")
    frame3 = pygame.image.load("BallFrames/BallFrame3.png")
    frame4 = pygame.image.load("BallFrames/BallFrame4.png")
    frame5 = pygame.image.load("BallFrames/BallFrame5.png")
    frame6 = pygame.image.load("BallFrames/BallFrame6.png")
    frame7 = pygame.image.load("BallFrames/BallFrame7.png")
    frame8 = pygame.image.load("BallFrames/BallFrame8.png")
    
    display.blit(frame1,(0,0))
    pygame.display.update()
    pygame.time.delay(83)
    
    display.blit(frame2,(0,0))
    pygame.display.update()
    pygame.time.delay(83)
    
    display.blit(frame3,(0,0))
    pygame.display.update()
    pygame.time.delay(83)

    display.blit(frame4,(0,0))
    pygame.display.update()
    pygame.time.delay(83)
    
    display.blit(frame5,(0,0))
    pygame.display.update()
    pygame.time.delay(83)
    
    display.blit(frame6,(0,0))
    pygame.display.update()
    pygame.time.delay(83)
    
    display.blit(frame7,(0,0))
    pygame.display.update()
    pygame.time.delay(83)
    
    display.blit(frame8,(0,0))
    pygame.display.update()
    pygame.time.delay(83)