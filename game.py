import pygame
from level import *
from spriteAnimation import *
from character import *
from typing import List

class Game:
    def __init__(self) -> None:
        self.level1 = Level(1)

        self.soldierSpritesheet = pygame.image.load("characters//soldier.png")
        self.orcSpriteSheet = pygame.image.load("characters//Orc.png")

        #Hero
        soldierIdle = SpriteAnimation(spritesheet=self.soldierSpritesheet, frameRect=(0, 0, 100,100), numFrames=6, frameTime=100)
        soldierAttack = SpriteAnimation(spritesheet=self.soldierSpritesheet, frameRect=(0, 200, 100,100), numFrames=6, frameTime=100)
        
        self.hero = Character()
        self.hero.AddAnimation('idle', soldierIdle)
        self.hero.AddAnimation('attack', soldierAttack)      
        self.hero.position = pygame.Vector2(0,0) 

        #Orc
        orcIdle = SpriteAnimation(spritesheet=self.orcSpriteSheet, frameRect=(0, 0, 100,100), numFrames=6, frameTime=100)
        self.orc = Character()
        self.orc.AddAnimation('idle', orcIdle)
        self.orc.position = pygame.Vector2(100,0) 

        self.orc2 = Character()
        self.orc2.AddAnimation('idle', orcIdle)
        self.orc2.position = pygame.Vector2(300,0) 

        self.allCharacters: List[Character] = []
        self.allCharacters.append(self.hero)
        self.allCharacters.append(self.orc)
        self.allCharacters.append(self.orc2)        

        pass

    def Update(self) -> None:
        
        for c in self.allCharacters:
            c.Update()
        pass

    def Render(self, screen) -> None:
        self.level1.Draw(screen)

        for c in self.allCharacters:
            c.Draw(screen)

        pass

    def OnEvent(self, event: pygame.event.Event):

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.hero.SelectAnimation('attack')
            if event.key == pygame.K_LCTRL:
                self.hero.SelectAnimation('idle')
