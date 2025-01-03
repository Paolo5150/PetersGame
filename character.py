from spriteAnimation import *
from typing import Dict

class Character:
    def __init__(self):
        self.animations: Dict[str, SpriteAnimation] = {}
        self.currentAnimation = 'idle'
        self.position = pygame.Vector2(0,0)

        pass

    def AddAnimation(self, animationName:str, spAnim: SpriteAnimation) -> None:
        self.animations[animationName] = spAnim

    def SelectAnimation(self, animationName: str):
        self.currentAnimation = animationName

    def Update(self):
        self.animations[self.currentAnimation].Update()
        if self.currentAnimation == 'attack':
            if self.animations[self.currentAnimation].animationComplete:
                self.animations[self.currentAnimation].animationComplete = False
                self.currentAnimation = 'idle'


    def Draw(self, screen: pygame.Surface):
        self.animations[self.currentAnimation].Draw(screen,  self.position)
