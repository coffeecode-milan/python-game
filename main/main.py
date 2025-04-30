import pygame
import os
from os.path import join
from fighter import Fighter
from mage import Mage

pygame.init()

windowwidth = 800
bottompanel = 150
windowheight = 400 + bottompanel

display_surface = pygame.display.set_mode((windowwidth,windowheight))
pygame.display.set_caption('WARIOR')



#font
font = pygame.font.SysFont('Times New Roman', 26)

#color
red = (255, 0, 0)
green = (0, 255, 0)



#background
bg_image = pygame.image.load(join("gamu","bg","PNG","gamu-bg1","gamu-bg1.png"))
bg_image = pygame.transform.scale(bg_image,(windowwidth, windowheight))

def draw_bg():
    display_surface.blit(bg_image,(0,0))


class HealthBar():
     def __init__(self, x, y, hp, max_hp):
          self.hp = hp
          self.x = x
          self.y = y
          self.max_hp = max_hp

     def draw(self,hp):
          self.hp = hp
          ratio = self.hp / self.max_hp
          pygame.draw.rect(display_surface, red, (self.x, self.y, 150, 20))
          pygame.draw.rect(display_surface, green, (self.x, self.y, 150 * ratio, 20))



Knight = Fighter(200, 260, 'knight', 30, 10, 3)
mage = Mage (600, 260, 'mage', 30, 8, 2)

Knight_health_bar = HealthBar(100, windowheight - bottompanel + 40, Knight.hp, Knight.max_hp)
mage_health_bar = HealthBar(100, windowheight - bottompanel + 40, mage.hp, Knight.max_hp)
running = True

while running:
    
    draw_bg()
  

    Knight.draw(display_surface)
    mage.draw(display_surface)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
               if event.key == pygame.K_UP:
                    Knight.jump()
               elif event.key == pygame.K_DOWN:
                    Knight.attack()
               elif event.key == pygame.K_RIGHT:
                    Knight.attackExtra()
               elif event.key == pygame.K_LEFT:
                    Knight.climb()
    pygame.display.update()

pygame.quit()