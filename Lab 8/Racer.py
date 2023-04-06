import pygame, sys, time
import random

pygame.init()
w = 1080
h = 720

pygame.mixer.music.load('track.mp3')
pygame.mixer.music.play() 

screen = pygame.display.set_mode((w,h))
clock = pygame.time.Clock()
running = True

font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, "black")


class Coin(pygame.sprite.Sprite):                               #Coin
    def __init__(self):         
        super().__init__() 
        self.image = pygame.image.load("Coin.png")
        self.rect = self.image.get_rect()
        self.rect.center=(random.randint(150,w-150),0) 
        self.cscore = 250
 
    def move(self):
        self.rect.move_ip(0,10)
        if (self.rect.bottom > 1080):
            self.rect.top = 0
            self.rect.center = (random.randint(150, w-150), 0)
 
    def draw(self, surface):
        surface.blit(self.image, self.rect) 


class Enemy(pygame.sprite.Sprite):                                 #Enemy
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center=(random.randint(150,w-150),0) 
 
      def move(self):
        self.rect.move_ip(0,12)
        if (self.rect.bottom > 1080):
            self.rect.top = 0
            self.rect.center = (random.randint(150, w-150), 0)
 
      def draw(self, surface):
        surface.blit(self.image, self.rect) 

class Road(pygame.sprite.Sprite):                               #ROAD
      def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Road.png")
        self.rect = self.image.get_rect()
        self.rect.center=(w/2,h/2)
 
      def move(self):
        self.rect.move_ip(0,20)
        if (self.rect.bottom > 1916):
            self.rect.top = 0
            self.rect.center = (w/2, h/2)

      def draw(self, surface):
        surface.blit(self.image, self.rect)

class Player(pygame.sprite.Sprite):                             #CAR
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Car.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
 
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[pygame.K_DOWN]:
            self.rect.move_ip(0,5) 
            
        if self.rect.left > 0:
              if pressed_keys[pygame.K_LEFT]:
                  self.rect.move_ip(-15, 0)
        if self.rect.right < w:        
              if pressed_keys[pygame.K_RIGHT]:
                  self.rect.move_ip(15, 0)
 
    def draw(self, surface):
        surface.blit(self.image, self.rect)

Car = Player()
road = Road()
E = Enemy()
coin = Coin()

game_score = 0

coins = pygame.sprite.Group()
coins.add(coin)

def collidecoin():
    global game_score
    for c in coins:
        global coin
        if Car.rect.colliderect(coin.rect):
            pygame.mixer.Sound('cash.mp3').play()
            game_score += coin.cscore
            c.kill()
            coin = Coin()
            coins.add(coin)
            all_sprites.add(coin)

enemies = pygame.sprite.Group()
enemies.add(E)
all_sprites = pygame.sprite.Group()
all_sprites.add(road)
all_sprites.add(coin)
all_sprites.add(Car)
all_sprites.add(E)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    scores = font_small.render("SCORE: " + str(game_score), True, "white")
    screen.blit(scores, (100,100))


    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)
        entity.move()

    collidecoin()

    if pygame.sprite.spritecollideany(Car , enemies):
        pygame.mixer.Sound('crash.mp3').play()
        time.sleep(0.5)
        screen.fill("RED")
        screen.blit(game_over, (360,200))
        pygame.display.update()
        time.sleep(2)
        pygame.quit()
        sys.exit()   

    screen.blit(scores, (100,100))
    
    clock.tick(60)
    pygame.display.update()
    

pygame.quit()