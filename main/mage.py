import pygame

class Mage():
    def __init__(self, x, y, name, max_hp, strength, position):
        self.name = name
        self.max_hp = max_hp
        self.alive = True
        self.animation_list = []
        self.frame_index = 0
        self.action = 0
        self.last_update = pygame.time.get_ticks()
        self.animation_cooldown = 100


        #load idle
        idle_list = []
        for i in range(1,14):
             img = pygame.image.load(f"main/characters/PNG/Mage/Idle/idle{i}.png").convert_alpha()
             idle_list.append(img)
        self.animation_list.append(idle_list)
        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = self.image.get_rect(center= (x, y))

    def idle(self):
        self.action = 0
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()
    
    def update(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_update > self.animation_cooldown:
            self.last_update = current_time
            self.frame_index += 1
            if self.frame_index >= len(self.animation_list[self.action]):
                self.frame_index = 0
            self.image = self.animation_list[self.action][self.frame_index]


    def draw(self, display_surface):
        self.update()

        display_surface.blit(self.image, self.rect)
    