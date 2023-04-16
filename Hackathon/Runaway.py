import pygame, random

pygame.init()

W = 1440
H = 720
game_score = 0
intro = True
running = False

pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play() 


screen = pygame.display.set_mode((W,H))
clock = pygame.time.Clock()
# running = True


font_score = pygame.font.SysFont("Verdana", 25)                                                                 # <-- Fonts

#        <--------------------------------------------------BACKGROUND ---------------------------------------------------->      
#                                              
bg_x = 0                                  
bg_y = 0
list_of_background = ['City night.png','Day.png','City night 2.png','Desert.png','City night 3.png','Forest.png']
img_cnt = 0
background = pygame.image.load(list_of_background[img_cnt])
score_cnt = 20000
bound = -1280

def background_sc():
    global bg_x, bg_y, img_cnt, background, score_cnt, bound
    
    if game_score >= score_cnt:
        img_cnt += 1
        score_cnt += 20000
        if img_cnt == 6:
            img_cnt = 0
        background = pygame.image.load(list_of_background[img_cnt])
    if img_cnt == 0:
        bound = -1280
    if img_cnt == 1:
        bound = -1643
    if img_cnt == 2:
        bound = -2798
    if img_cnt == 3:
        bound = -1573
    if img_cnt == 4:
        bound = -1786
    if img_cnt == 5:
        bound = -1440
    screen.blit(background , (bg_x,bg_y))
    if bound < bg_x:
        bg_x -= 10
    else:
        bg_x = 0

#           <-------------------------------------------------- OBJECTS ----------------------------------------------------------------->

class Police(pygame.sprite.Sprite):                                #  <--Police car
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Police.png")
        self.rect = self.image.get_rect()
        self.rect.center=(200,660)
 
      def draw(self, surface):
        surface.blit(self.image, self.rect) 
                                                                 
n = 0
move_list = ['1.png','2.png','3.png','4.png','5.png','6.png']       # <-- Robber

class Robber(pygame.sprite.Sprite):                                 
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load(move_list[n])
        self.rect = self.image.get_rect()
        self.rect.y = 630
        self.rect.center = (W/2, self.rect.y)
        self.isJump = False
        self.jumpCount = 13
        self.last_update = 0


    def update(self):
        global n
        time_now = pygame.time.get_ticks()      # get the current time
        if time_now - self.last_update > 50:    # delay for 50  milliseconds
            self.last_update = time_now
            n += 1
            if n >= 6:
                n = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and not self.isJump:
            self.isJump = True
        if self.isJump:
            if self.jumpCount >= -13:
                neg = 1
                if self.jumpCount < 0:
                    neg = -1
                self.rect.y -= (self.jumpCount ** 2) / 2 * neg
                self.jumpCount -= 1
            else:
                self.isJump = False
                self.jumpCount = 13
        self.image = pygame.image.load(move_list[n])
        self.rect.clamp_ip(screen.get_rect())

    def draw(self, surface):
        surface.blit(self.image, self.rect)

all_sprites = pygame.sprite.Group()
police = pygame.sprite.Group()
cop = Police()
police.add(cop)
player = Robber()
all_sprites.add(player)


class Obstacle_1(pygame.sprite.Sprite):                                 # <-- Obstacle 1
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Obstacle 1.png")
        self.rect = self.image.get_rect()
        self.rect.center=(random.randint(6000,10000),670) 
 
    def move(self):
        global obstacles
        self.rect.move_ip(-12, 0)
        if self.rect.right < 0:
            self.rect.left = 1280

    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Obstacle_2(pygame.sprite.Sprite):                                 # <-- Obstacle 2
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Obstacle 2.png")
        self.rect = self.image.get_rect()
        self.rect.center=(random.randint(4000,6000),690) 
 
    def move(self):
        global obstacles
        self.rect.move_ip(-12, 0)
        if self.rect.right < 0:
            self.rect.left = 1280

    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Obstacle_3(pygame.sprite.Sprite):                                 # <-- Obstacle 3
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Obstacle 3.png")
        self.rect = self.image.get_rect()
        self.rect.center=(random.randint(2000,4000),705) 
 
    def move(self):
        global obstacles
        self.rect.move_ip(-12, 0)
        if self.rect.right < 0:
            self.rect.left = 1280

    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Coin(pygame.sprite.Sprite):                                 # <-- Coin
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Tenge.png")
        self.rect = self.image.get_rect()
        self.rect.center=(random.randint(1000,3000),random.randint(600,650)) 
 
    def move(self):
        global obstacles
        self.rect.move_ip(-12, 0)
        if self.rect.right < 0:
            self.rect.left = 1280

    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Dollar(pygame.sprite.Sprite):                                 # <-- Dollar
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Dollar.png")
        self.rect = self.image.get_rect()
        self.rect.center=(random.randint(4000,9000),680) 
 
    def move(self):
        global obstacles
        self.rect.move_ip(-12, 0)
        if self.rect.right < 0:
            self.rect.left = 1280

    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Cash(pygame.sprite.Sprite):                                 # <-- $$$$$
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Cash 2.png")
        self.rect = self.image.get_rect()
        self.rect.center=(random.randint(7000,15000),680) 
 
    def move(self):
        global obstacles
        self.rect.move_ip(-12, 0)
        if self.rect.right < 0:
            self.rect.left = 1280

    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Energy(pygame.sprite.Sprite):                                 # <-- Energy
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Flash.png")
        self.rect = self.image.get_rect()
        self.rect.center=(random.randint(7000,15000),680) 
 
    def move(self):
        global obstacles
        self.rect.move_ip(-12, 0)
        if self.rect.right < 0:
            self.rect.left = 1280

    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Box(pygame.sprite.Sprite):                                 # <-- ?BOX?
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Box.png")
        self.rect = self.image.get_rect()
        self.rect.center=(random.randint(10000,15000),680) 
 
    def move(self):
        global obstacles
        self.rect.move_ip(-12, 0)
        if self.rect.right < 0:
            self.rect.left = 1280

    def draw(self, surface):
        surface.blit(self.image, self.rect)


obstacles = pygame.sprite.Group()
obstacle_1 = Obstacle_1()
obstacles.add(obstacle_1)
obstacle_2 = Obstacle_2()
obstacles.add(obstacle_2)
obstacle_3 = Obstacle_3()
obstacles.add(obstacle_3)
coin = Coin()
obstacles.add(coin)
dollar = Dollar()
obstacles.add(dollar)
cash = Cash()
obstacles.add(cash)
energy = Energy()
obstacles.add(energy)
box = Box()
obstacles.add(box)

image_spark = pygame.image.load('Spark.png')                    #<--- SPARK

#              <--------------------------------------------------COLLISION---------------------------------------------------------->
img_game_over = pygame.image.load('Game over.jpg')

def collide():
    global obstacle_1, obstacle_2, obstacle_3, cash, coin, dollar, energy, box, game_score, running
    if cop.rect.colliderect(obstacle_1):
        obstacles.remove(obstacle_1)
        obstacle_1 = Obstacle_1()
        obstacles.add(obstacle_1)
        screen.blit(image_spark, (400,650))
    if cop.rect.colliderect(obstacle_2):
        obstacles.remove(obstacle_2)
        obstacle_2 = Obstacle_2()
        obstacles.add(obstacle_2)
        screen.blit(image_spark, (400,655))
    if cop.rect.colliderect(obstacle_3):
        obstacles.remove(obstacle_3)
        obstacle_3 = Obstacle_3()
        obstacles.add(obstacle_3)
        screen.blit(image_spark, (400,660))
    if player.rect.colliderect(coin):
        obstacles.remove(coin)
        coin = Coin()
        obstacles.add(coin)
        game_score += 150
        pygame.mixer.Sound('cash.mp3').play()
    if player.rect.colliderect(dollar):
        obstacles.remove(dollar)
        dollar = Dollar()
        obstacles.add(dollar)
        game_score += 1250
        pygame.mixer.Sound('cash.mp3').play()
    if player.rect.colliderect(cash):
        obstacles.remove(cash)
        cash = Cash()
        obstacles.add(cash)
        game_score += 5250
        pygame.mixer.Sound('cash.mp3').play()
    if player.rect.colliderect(energy):
        obstacles.remove(energy)
        energy = Energy()
        obstacles.add(energy)
        if player.rect.x < 715:
            player.rect.x += 100
    if player.rect.colliderect(box):
        obstacles.remove(box)
        box = Box()
        obstacles.add(box)
        num = random.randint(1,2)
        if num == 1:                #heal
            player.rect.x = W/2
        if num == 2:
            game_score += 10000


hp_full_image = pygame.image.load('hp full.png')
hp_middle_image = pygame.image.load('hp middle.png')
hp_low_image = pygame.image.load('hp low.png')

#             <----------------------------------------------GAME------------------------------------------------------------->

img_intro = pygame.image.load('Intro.jpg')
img_instruction = pygame.image.load('Instruction.jpg')

while intro:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            intro = False

    screen.blit(img_intro, (0,0))
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
            intro = False
    if keys[pygame.K_p]:
            running = True
            intro = False 
    if keys[pygame.K_i]:
            screen.blit(img_instruction, (0,0))

    clock.tick(60)
    pygame.display.update()
    
over_sound = True
game = True

while running:                                                             
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if game == True:        
            background_sc()
            scores = font_score.render("BANK: " + str(game_score) + "$", True, "green")
            screen.blit(scores, (100,100))
            Police().draw(screen)
            all_sprites.update()
            all_sprites.draw(screen)
            obstacles.update()
            obstacles.draw(screen)
            obstacle_1.move()
            obstacle_2.move()
            obstacle_3.move()
            coin.move()
            dollar.move()
            cash.move()
            energy.move()
            box.move()

            if player.rect.x >= 614 and player.rect.x <= 1200:
                screen.blit(hp_full_image, (75,40))
            if player.rect.x >= 508 and player.rect.x < 614:
                screen.blit(hp_middle_image, (80,40))
            if player.rect.x >= 300 and player.rect.x < 508:
                screen.blit(hp_low_image, (83,40))

            if pygame.sprite.spritecollide(player, obstacles, False):
                player.rect.x -= 5

            collide()

        if cop.rect.colliderect(player):
            game = False
            pygame.mixer.music.pause()
            if over_sound == True:
                pygame.mixer.Sound('Game over sound.mp3').play()
                over_sound = False 
                screen.blit(img_game_over, (0,0))
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            running = False

        clock.tick(60)
        pygame.display.update()

pygame.quit()                           