import pygame

pygame.init()

screen = pygame.display.set_mode((600, 400))

pygame.display.set_caption("draw shapes with keys")

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

running = True

shape = ""

while running:
    screen.fill(WHITE)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                shape = "rectangle"
                    
            elif event.key == pygame.K_c:
                shape = "circle"
                    
            elif event.key == pygame.K_l:
                shape = "line"
                    
    if shape == "rectangle":
        pygame.draw.rect(screen, RED, (200, 150, 200, 100))
        
    elif shape == "circle":
        pygame.draw.circle(screen, BLUE, (300, 200), 50)
        
    elif shape == "line":
        pygame.draw.line(screen, GREEN, (100, 100), (500, 300), 5)
        
    pygame.display.update()
pygame.quit()