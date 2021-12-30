import pygame
import random
import sys


imageURL = sys.argv[1]
backGround = pygame.image.load(imageURL)
scalingFactor = 4
(length, width) = backGround.get_size()
if(int(length)<180 and int(width)<180):
    scalingFactor = 8

mainWindow = pygame.display.set_mode((length*scalingFactor, width*scalingFactor))
mainWindow.fill((240, 240, 250))

for x in range(0, length*scalingFactor):
    for y in range(0, width*scalingFactor):
        (r, g, b, _) = backGround.get_at((x//scalingFactor, y//scalingFactor))
       
        luminance = (0.2126 * r + 0.7152 * g + 0.0722 * b) / 255   
        
        if(luminance > .85):
            w = int((random.random()*3)+1)
            if(w==1):
                pygame.draw.circle(mainWindow, (200, 0, 0), (x, y), (1))
                
            elif(w==2):
                pygame.draw.circle(mainWindow, (0, 200 , 0), (x, y), (1))

            elif(w==3):
                pygame.draw.circle(mainWindow, (0, 0, 200), (x, y), (1))
           
        elif(luminance>.55):
            w = int((random.random()*5)+1)
            if(w==1):
                pygame.draw.circle(mainWindow, (200, 0, 0), (x, y), (1))
            elif(w==2):
                pygame.draw.circle(mainWindow, (0, 200, 0), (x, y), (1))
            elif(w==3):
                pygame.draw.circle(mainWindow, (0, 0, 200), (x, y), (1))
            else:
                pygame.draw.circle(mainWindow, (0, 0, 0), (x, y), (1))
        elif(luminance>.25):
            w = int((random.random()*16)+1)
            if(w==1):
                pygame.draw.circle(mainWindow, (200, 0, 0), (x, y), (1))
            elif(w==2):
                pygame.draw.circle(mainWindow, (0, 200, 0), (x, y), (1))
            elif(w==3):
                pygame.draw.circle(mainWindow, (0, 0, 200), (x, y), (1))
            else:
                pygame.draw.circle(mainWindow, (0, 0, 0), (x, y), (1))
        elif(luminance>.05):
            w = int((random.random()*20)+1)
            if(w==1):
                pygame.draw.circle(mainWindow, (200, 0, 0), (x, y), (1))
            elif(w==2):
                pygame.draw.circle(mainWindow, (0, 200, 0), (x, y), (1))
            elif(w==3):
                pygame.draw.circle(mainWindow, (0, 0, 200), (x, y), (1))
            else:
                pygame.draw.circle(mainWindow, (0, 0, 0), (x, y), (1))
        else:
            pygame.draw.circle(mainWindow, (0, 0, 0), (x, y), (1))

pygame.display.update()
pygame.time.delay(10000)