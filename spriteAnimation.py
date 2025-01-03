import pygame

class SpriteAnimation:
    def __init__(self, spritesheet, frameRect, numFrames, frameTime):
        self.frames = self.extractFrames(spritesheet, frameRect, numFrames)
        self.currentFrame = 0

        self.frameTime = frameTime
        self.lastUpdateTime = pygame.time.get_ticks()
        self.animationComplete = False

    def extractFrames(self, spritesheet, frameRect, numFrames):
        frames = []
        frameWidth, frameHeight = frameRect[2], frameRect[3]
        for i in range(numFrames):
            frameX = frameRect[0] + i * frameWidth
            frameY = frameRect[1]
            frame = spritesheet.subsurface(pygame.Rect(frameX, frameY, frameWidth, frameHeight))
            frames.append(frame)
        return frames
        

    def Update(self):
        currentTime = pygame.time.get_ticks()
        if currentTime - self.lastUpdateTime > self.frameTime:
            #self.currentFrame = (self.currentFrame +1) % len(self.frames)
            self.lastUpdateTime = currentTime
            self.currentFrame += 1
            if self.currentFrame >= len(self.frames) - 1:
                self.animationComplete = True
                self.currentFrame = 0

    def Draw(self, screen: pygame.Surface, position):

        scaledSize = (200, 200)
        scaledFrame = pygame.transform.scale(self.frames[self.currentFrame], scaledSize)
        screen.blit(scaledFrame, position)



        