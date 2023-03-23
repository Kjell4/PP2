import pygame

pygame.init()
w = 1280
h = 720
screen = pygame.display.set_mode((w,h))
running = True

audio_list = ['Haggstrom.mp3','Living Mice.mp3','Mice on Venus.mp3','Moog City.mp3']

pause = False

song = 0

pygame.mixer.music.load(audio_list[song])
pygame.mixer.music.play()     

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:                 #pause
                pause = not pause
                if pause:
                    pygame.mixer.music.pause()                 
                else:
                    pygame.mixer.music.unpause()                
            if event.key == pygame.K_RIGHT:                 #next song
                song+=1
                pygame.mixer.music.load(audio_list[song])
                pygame.mixer.music.play()   
            if event.key == pygame.K_LEFT:                  #prev song
                song-=1
                pygame.mixer.music.load(audio_list[song])
                pygame.mixer.music.play()   
           
pygame.quit()