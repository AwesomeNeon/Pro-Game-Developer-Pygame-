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
            y1 = 760 + 65 * pygame.math.Vector2(1, 0).rotate(rotate(angle).y)
        
            x2 = 760 + 85 * pygame.math.Vector2(1, 0).rotate(angle).x
            y2 = 100 + 85 * pygame.vector2(1, 0).rotate(angle).y
            
            pygame.draw.line(screen, YELLOW, (x1, y1), (x2, x2),3)
            
            if weather == "rain":
                cloud_color = (70, 70, 70)
                                                 