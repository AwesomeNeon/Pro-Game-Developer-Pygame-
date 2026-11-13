import pygame
import random

pygame.init()

WIDTH = 900
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Weather Simulator")

clock = pygame.time.clock()

SKY = (134, 206, 235)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 120, 255)
GREEN = (60, 180, 75)

font = pygame.font.SysFont(None, 30)

weather = "Sunny"

clouds = []

for i in range(5):
    x = random.randint(0, WIDTH)
    y = random.randint(30, 180)
    clouds.append([x, y])
    
raindrops = []

for i in range(250):
    x = random.randint(0,WIDTH)
    y = random.randint(-HEIGHT, HEIGHT)
    raindrops.append([x, y])
    
snowflakes = []

for i in range(200):
    x = random.randint(0, WIDTH)
    y = random.randint(-HEIGHT,HEIGHT)
    size = random.randint(2, 5)
    snowflakes.append([x, y, size])
    
sun_button = pygame.Rect(60, 525, 120, 50)
rain_button = pygame.Rect(250, 525, 120, 50)
snow_button = pygame.Rect(440, 525, 120, 50)

running = True
while running:
    screen.fill(SKY)
    if weather == "sunny":
        pygame.draw.circle(screen, YELLOW, (760, 100), 55)
        
        for angle in range (0, 360, 30):
            
            x1 = 760 + 65 * pygame.math.Vector2(1, 0).rotate(angle.x)
            y1 = 760 + 65 * pygame.math.Vector2(1, 0).rotate(angle.y)
        
            x2 = 760 + 85 * pygame.math.Vector2(1, 0).rotate(angle).x
            y2 = 100 + 85 * pygame.vector2(1, 0).rotate(angle).y
            
            pygame.draw.line(screen, YELLOW, (x1, y1), (x2, x2),3)
            
    if weather == "rain":
        cloud_color = (70, 70, 70)
    else:
        cloud_color = WHITE
    for cloud in clouds:
            
        pygame.draw.circle(screen, cloud_color, (cloud[0], cloud[1]), 25)
        pygame.draw.circle(screen, cloud_color, (cloud[0] + 25, cloud[1] - 10), 30)
        pygame.draw.circle(screen, cloud_color, (cloud[0] + 55, cloud[1]), 25)
        
        cloud[0] += 1
        
        if cloud[0] > WIDTH + 60:
            cloud[0] = -60
   
    if weather == "rain":
        
        for drop in raindrops:
            
            pygame.draw.line(screen, BLUE, (drop[0], drop[1], drop[0], drop[1] + 12), 2)
            
            drop[0] += 10
            
            if drop[1] > HEIGHT:
                drop[1] = random.randint(-100, 0)
                drop[0] = random.randint(0, WIDTH)
                
    if weather == "snow":
        
        for snow in snowflakes:
            
            pygame.draw.circle(screen, WHITE, (snow[0], snow[1]), snow[2])
            
            snow[1] += 2
            snow[0] += random.randint(-1, 1)
            
            if snow[1] > HEIGHT:
                snow[1] = random.randint(-100, 0)
                snow[0] = random.randint(0, WIDTH)
                
                if weather == "Snow":
                    ground_color = WHITE
                else:
                    ground_color = GREEN
                    pygame.draw.rect(screen, ground_color, (0, 420, WIDTH, 180))
    
    if weather == "Snow":
        
        pygame.draw.circle(screen, WHITE, (730, 355), 55)
        
        pygame.draw.circle(screen, WHITE, (730, 275), 42)
        
        pygame.draw.circle(screen, WHITE (730 215), 28)
        
        pygame.draw.arc(screen, BLACK, (722, 215), 28)
        pygame.draw.circle(screen, BLACK (738, 208), 3)
        
        pygame.draw.arc(screen, BLACK, (722, 208),)