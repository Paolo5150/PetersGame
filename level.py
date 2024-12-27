import pygame
import random
from fooditem import *

class Tile:
    def __init__(self, type:str, position, color):
        self.position = position
        self.color = color
        self.type = type
        self.item: FoodItem = None
        pass

    def Draw(self, screen) -> None:
        pygame.draw.rect(screen, self.color,(*self.position, 40,40) )   
        if self.item != None:
            self.item.position = self.position
            self.item.Draw(screen)




class Level:
    def __init__(self, levelNumber) -> None:
        self.mapSize = 15,15
        self.tileSize = 40
        self.grid = []
        foodSpriteSheet = pygame.image.load("foodpacks\\general-food.png")

        fileName = 'lvl' + str(levelNumber) + '.txt'
        print(f"File name will be {fileName}")

        with open('levels\\' + fileName, 'r') as file:
            row = 0
            for line in file:
                columns = []
                col = 0
                for character in line:
                    tileType = 'grass'
                    tilePoistion = (col * self.tileSize, row * self.tileSize)
                    tileColor = (0,random.randint(220,255),0)
                    tile = Tile(tileType, tilePoistion, tileColor)

                    if character == '#':
                        tileType = 'wall'
                        tileColor = (139,69,19)
                        tile.color = tileColor
                        tile.type = tileType
                    elif character == 'X':
                        tileType = 'exit'
                        tileColor = (0,0,0)
                        tile.color = tileColor
                        tile.type = tileType
                    elif '1' <= character <= '9':
                        foodId = int(character)
                        foodType = FoodType(foodId)
                        item = FoodItem(foodType, foodSpriteSheet)  
                        tile.item = item                     
                        

                    columns.append(tile)
                    col +=1
                row +=1
                self.grid.append(columns)

    def Draw(self, screen) -> None:
        for row in range(self.mapSize[0]):
            for col in range(self.mapSize[1]):
                tile = self.grid[row][col]
                tile.Draw(screen)



