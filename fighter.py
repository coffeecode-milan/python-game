import pygame
from os.path import join
import random

pygame.init()


WINDOWWIDTH = 800
BOTTOMPANEL = 150
WINDOWHEIGHT = 400 + BOTTOMPANEL


display_surface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('FIGHTER')

current_fighter = 1
total_fighter = 3
action_cooldown = 0
action_wait_time = 90

#Define Fonts
font = pygame.font.SysFont('Times New Roman', 26)

#define colours
red = (255, 0, 0)
green = (0, 255, 0)
#background image
background_img = pygame.image.load(join("battle","img","Background","background.png"))

#panel image
panel_img = pygame.image.load(join("battle","img","Icons","panel.png"))

#creare function for drawing text
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    display_surface.blit(img, (x, y))

#function for drawing back
def draw_bg():
    display_surface.blit(background_img,(0,0))

#function for drawing panal
def draw_panel():
    #draw panel rectangle
    display_surface.blit(panel_img, (0, WINDOWHEIGHT - BOTTOMPANEL))
    #show knight stats
    draw_text(f'{Knight.name} HP :{Knight.hp}', font, red,100, WINDOWHEIGHT - BOTTOMPANEL +10)
    for count, i in enumerate(bandit_list):
        #show name and health
        draw_text(f'{i.name} HP :{i.hp}', font, red, 550, (WINDOWHEIGHT - BOTTOMPANEL +10) + count * 60)


class Fighter():
    def __init__(self, x, y, name, max_hp, strength, potions):
        self.name = name
        self.max_hp = max_hp
        self.hp = max_hp
        self.strength = strength
        self.start_positions = potions
        self.potions = potions
        self.alive = True
        self.animation_list = []
        self.frame_index = 0
        self.action = 0 #0:idle, 1:attack, 2:hurt, 3:dead
        self.update_time = pygame.time.get_ticks()
        #load idle image
        temp_list = []
        for i in range(8):
          img = pygame.image.load(f"battle/img/{self.name}/Idle/{i}.png").convert_alpha()
          img = pygame.transform.scale(img, (img.get_width() * 3, img.get_height() * 3))
          temp_list.append(img)
        self.animation_list.append(temp_list)
         #load attack images
        temp_list = []
        for i in range(8):
          img = pygame.image.load(f"battle/img/{self.name}/Attack/{i}.png").convert_alpha()
          img = pygame.transform.scale(img, (img.get_width() * 3, img.get_height() * 3))
          temp_list.append(img)
        self.animation_list.append(temp_list)
        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)



    def update(self):
        animation_cooldown = 100
        #handle animation
        #update image
        self.image = self.animation_list[self.action][self.frame_index]
        #check if enough time has passed since the last update
        if pygame.time.get_ticks() - self.update_time > animation_cooldown:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
        #if the animation has run out then reset back to the start
        if self.frame_index >= len(self.animation_list[self.action]):
            self.idle()
    

    def idle(self):
        self.action = 0
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()
 
   
    def attack(self, target):
        rand = random.randint(-5, 5)
        damage = self.strength+ rand
        target.hp -= damage
        self.action = 1
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()


    def draw(self):
        display_surface.blit(self.image,self.rect)


class HealthBar():
    def __init__(self, x, y, hp, max_hp):
        self.x = x
        self.y = y
        self.hp = hp
        self.max_hp = max_hp

    def draw(self, hp):
        #update with new health
        self.hp = hp
        ratio = self.hp / self.max_hp
        pygame.draw.rect(display_surface, red, (self.x, self.y, 200, 20)) 
        pygame.draw.rect(display_surface, green, (self.x, self.y, 200 * ratio, 20))




Knight = Fighter(200, 260, 'Knight', 30, 10, 3)
bandit1 = Fighter(550, 270, 'Bandit', 20, 6, 1)
bandit2 = Fighter(700, 270, 'Bandit', 20, 6, 1)

bandit_list = []
bandit_list.append(bandit1)
bandit_list.append(bandit2)

knight_health_bar = HealthBar(100, WINDOWHEIGHT - BOTTOMPANEL + 40, Knight.hp, Knight.max_hp)
bandit1_health_bar = HealthBar(550, WINDOWHEIGHT - BOTTOMPANEL + 40, bandit1.hp, bandit1.max_hp)
bandit2_health_bar = HealthBar(550, WINDOWHEIGHT - BOTTOMPANEL + 100, bandit2.hp, bandit2.max_hp)
running = True
while running:


    #draw background
    draw_bg()

    #draw panel
    draw_panel()

    knight_health_bar.draw(Knight.hp)
    bandit1_health_bar.draw(bandit1.hp)
    bandit2_health_bar.draw(bandit2.hp)
    

    #draw fighter
    Knight.draw()

    Knight.update()
    
    #draw bandit
    for bandit in bandit_list:
        bandit.update()
        bandit.draw()

    #plyayer action
    if Knight.alive == True:
        if current_fighter == 1:
            action_cooldown += 1
            if action_cooldown >= action_wait_time:
              #look for player action
              #attack
              Knight.attack(bandit1)
              current_fighter += 1
              action_cooldown


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
   
pygame.quit()