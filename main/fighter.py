import pygame

class Fighter():
    def __init__(self, x, y, name, hp, max_hp, strength, position = "left"):
        self.name = name 
        self.hp = hp
        self.strength = strength
        self.position = position
        self.max_hp = max_hp
        self.alive = True
        self.animation_list = []
        self.frame_index = 0
        self.action = 6 #0:attack, 1:attack extra 

        #load Attackh
        attack_list = []
        for i in range(4):
             img = pygame.image.load(f"main/characters/PNG/Knight/Attack/attack{i}.png").convert_alpha()
             attack_list.append(img)
        self.animation_list.append(attack_list)
        
        #attack extraa
        attackextra_list = []
        for i in range(1,8):
             img = pygame.image.load(f"main/characters/PNG/Knight/Attack_Extra/attack_extra{i}.png").convert_alpha()
             attackextra_list.append(img)
        self.animation_list.append(attackextra_list)
        
        #load Climb
        climb_list = []
        for i in range(1,4):
             img = pygame.image.load(f"main/characters/PNG/Knight/Climb/climb{i}.png").convert_alpha()
             climb_list.append(img)
        self.animation_list.append(climb_list)
        
        #load Death
        death_list = []
        for i in range(1,10):
             img = pygame.image.load(f"main/characters/PNG/Knight/Death/death{i}.png").convert_alpha()
             death_list.append(img)
        self.animation_list.append(death_list)
        
        #load High jump
        high_list = []
        for i in range(1,12):
             img = pygame.image.load(f"main/characters/PNG/Knight/High_jump/high_jump{i}.png").convert_alpha()
             high_list.append(img)
        self.animation_list.append(high_list)

        #load Hurt
        hurt_list = []
        for i in range(1,4):
             img = pygame.image.load(f"main/characters/PNG/Knight/Hurt/hurt{i}.png").convert_alpha()
             hurt_list.append(img)
        self.animation_list.append(hurt_list)
       
        #load idle
        idle_list = []
        for i in range(1,12):
             img = pygame.image.load(f"main/characters/PNG/Knight/Idle/idle{i}.png").convert_alpha()
             idle_list.append(img)
        self.animation_list.append(idle_list)
        
        #load jump
        jump_list = []
        for i in range(1,7):
             img = pygame.image.load(f"main/characters/PNG/Knight/Jump/jump{i}.png").convert_alpha()
             jump_list.append(img)
        self.animation_list.append(jump_list)

        #load push
        push_list = []
        for i in range(1,4):
             img = pygame.image.load(f"main/characters/PNG/Knight/Push/push{i}.png").convert_alpha()
             push_list.append(img)
        self.animation_list.append(push_list)

        #load idle
        run_list = []
        for i in range(1,8):
             img = pygame.image.load(f"main/characters/PNG/Knight/Run/run{i}.png").convert_alpha()
             run_list.append(img)
        self.animation_list.append(run_list)

        #load run attack
        runattack_list = []
        for i in range(1,8):
             img = pygame.image.load(f"main/characters/PNG/Knight/Run_attack/run_attack{i}.png").convert_alpha()
             runattack_list.append(img)
        self.animation_list.append(runattack_list)

        #load walk
        walk_list = []
        for i in range(1,6):
             img = pygame.image.load(f"main/characters/PNG/Knight/Walk/walk{i}.png").convert_alpha()
             walk_list.append(img)
        self.animation_list.append(walk_list)

        #load walk attack
        walkattack_list = []
        for i in range(1,6):
             img = pygame.image.load(f"main/characters/PNG/Knight/Walk_Attack/walk_attack{i}.png").convert_alpha()
             walkattack_list.append(img)
        self.animation_list.append(walkattack_list)

        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = self.image.get_rect(center = (x, y))

        #self animation
        self.last_update = pygame.time.get_ticks()
        self.animation_cooldown = 100

    def idle(self):
         self.action = 6
         self.frame_index = 0
         self.update_time = pygame.time.get_ticks()
     

    def attack(self):
         if self.action != 0:
              self.action = 0
              self.frame_index = 0
              self.last_update = pygame.time.get_ticks()

    def attackExtra(self):
         if self.action != 1:
              self.action = 1
              self.frame_index =0
              self.last_update = pygame.time.get_ticks()

    def jump(self):
         if self.action != 7:
              self.action = 7
              self.frame_index = 0
              self.last_update = pygame.time.get_ticks()

    def climb(self):
         if self.action != 2:
              self.action = 2
              self.frame_index = 0
              self.last_update = pygame.time.get_ticks()
     
    def update(self):
         current_time = pygame.time.get_ticks()

         if current_time - self.last_update > self.animation_cooldown:
              self.last_update = current_time
              self.frame_index += 1

              if self.frame_index >= len(self.animation_list[self.action]):
                   #after jump (or any 1 -time animation), return to idle
                   if self.action == 7:
                        self.action = 6 #idle index
                   elif self.action == 0:
                        self.action = 6
                   elif self.action == 1:
                        self.action = 6
                   elif self.action == 2:
                        self.action = 6
                   self.frame_index = 0
                   
              self.image = self.animation_list[self.action][self.frame_index]

    
    def draw(self, display_surface):
        self.update()
      
        display_surface.blit(self.image,self.rect)

