import pygame
from level import *

class Game:
    def __init__(self) -> None:
        self.level1 = Level(1)
        pass

    def Update(self) -> None:
        pass

    def Render(self, screen) -> None:
        self.level1.Draw(screen)
        pass

    def OnEvent(self, event: pygame.event.Event):
        
        pass