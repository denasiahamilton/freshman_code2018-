import pygame
import sys
import random

def main():
    width = 600
    height = 600
    color = [(0,0,0), (255,0,0),(255,255,255)]
    pygame = pygame.init()
    display = pygame.display.set_mode((width, height))
    speed = 60
    time = pygame.time.Clock()
    caption = pygame.display.set_caption("game.py")
    display.fill((0,0,0))
    image = pygame.image.load("imSquare.png")
    imageRect = image.get_rect()
    moving = [2,2]
    paddle = pygame.image.load("ImRectangle")
    imagePaddle = paddle.get_rect()
    
   while True:
    #game
    imageRect = imageRect.move(moving)
    display.blit(image, imageRect)
    
    pygame.display.flip()
    time.tick(speed)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                display.fill((random.randint(0,255), random.randint(0,255), random.randint(0,255)))
    

if __name__ == "__main__":
    main()
