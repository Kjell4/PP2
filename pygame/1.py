import pygame
pygame.init()

W, H = 1200, 800
WHITE = (255, 255, 255)

sc = pygame.display.set_mode((W, H))
mickey = pygame.image.load("main-clock.png")
rhand = pygame.image.load("right-hand.png")
lhand = pygame.image.load("left-hand.png")


def blitRotateCenter(surf, image, topleft, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center = image.get_rect(topleft = topleft).center)
    surf.blit(rotated_image, new_rect)
    
angle_min = 0   
angle_sec = 0 
    
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
            
    sc.fill(WHITE)
    sc.blit(mickey, (170,10))
    angle_min -= 0.05
    angle_sec -= 0.5
    blitRotateCenter(sc, rhand, (330,310), angle_min)
    blitRotateCenter(sc, lhand, (365,320), angle_sec) 
    
    pygame.display.update()