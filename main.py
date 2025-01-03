import pygame
from game import *
from level import *

pygame.init()

ScreenWidth = 800
ScreenHeight = 600

m_screen = pygame.display.set_mode((ScreenWidth, ScreenHeight))
m_isRunning = True

m_game = Game()


while m_isRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            m_isRunning = False
        else:
            m_game.OnEvent(event)

    m_game.Update()

    m_screen.fill((0,0,0))
    m_game.Render(m_screen)

    pygame.display.flip()

pygame.quit()



