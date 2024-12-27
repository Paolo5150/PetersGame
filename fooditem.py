import pygame
from enum import Enum

class FoodType(Enum):
    SOUP = 0
    TACO = 1
    RAMEN = 2
    BURGER = 3
    PIZZA_SLICE = 4
    PIZZE = 5
    SUSHI = 6
    WEIRD_BROWN_THING = 7
    EGG = 9 

class FoodItem:
    def __init__(self, type: FoodType, spriteSheet):
        self.foodType = type
        self.spriteSheet = spriteSheet
        self.position = pygame.Vector2(0,0)
        pass

    def Draw(self, screen: pygame.Surface):
        framePos = (0, 0)
        if self.foodType == FoodType.TACO:
            framePos = (16, 0)
        if self.foodType == FoodType.SUSHI:
            framePos = (0, 32)

        frame = self.spriteSheet.subsurface(pygame.Rect(framePos[0], framePos[1], 16,16))

        scaledSize = (32, 32)
        scaledFrame = pygame.transform.scale(frame, scaledSize)

        screen.blit(scaledFrame, self.position)

