import pygame
import time
pygame.init()
import sys
start = False
click = False
screen = pygame.display.set_mode((860,780))
pygame.display.set_caption("screen")
l_time = pygame.time.get_ticks()
x = 0
bg = pygame.image.load("flabybird/images/f6.png")
ground = pygame.image.load("flabybird/images/f1.png")
birds = ["f3","f5","f7"]
fps = pygame.time.Clock()
class bird(pygame.sprite.Sprite):
     def __init__(self,x,y):
          pygame.sprite.Sprite.__init__(self)
          self.images = []
          for bir in birds:
               img = pygame.image.load("flabybird/images/"+ bir +".png")
               self.images.append(img)
          self.index = 0
          self.image = self.images[self.index]
          self.rect = self.image.get_rect()
          self.rect.center = x,y
          self.counter = 0
          self.velocity = 0
     def update(self):
          global click
          if start == True:
            if pygame.mouse.get_pressed()[0] == True and click == False:
                 self.velocity = - 8
                 click = True
            if pygame.mouse.get_pressed()[0] == False:
                 click = False
            

            self.velocity = self.velocity + 0.25
            if self.velocity > 30:
                 self.velocity = 30
            if self.rect.y < 575:
                 self.rect.y = self.rect.y + self.velocity

            self.counter = self.counter + 1
            if self.counter >= 10:
              self.index = self.index + 1
              if self.index > 2:
                   self.index = 0
              self.image = self.images[self.index]
              self.counter = 0
            self.image = pygame.transform.rotate(self.images[self.index],-self.velocity*2)

class pipe(pygame.sprite.Sprite):
     def __init__(self,x,y,flip):
          pygame.sprite.Sprite.__init__(self)
          self.image = pygame.image.load("flabybird/images/f2.png")
          self.rect = self.image.get_rect()
          if flip == True:
               self.image = pygame.transform.flip(self.image,False,True)
               self.rect.center = x,y
          else:
               self.rect.center = x,y
     def update(self):
          self.rect.x = self.rect.x - 3

group_pipe = pygame.sprite.Group()

bird_object = bird(50,350)
group_birds = pygame.sprite.Group()
group_birds.add(bird_object)
while True:
     fps.tick(60)
     screen.blit(bg,(0,0))
     group_pipe.draw(screen)
     screen.blit(ground,(x,615))
     x = x - 4
     if x < -30:
          x = 0
     group_birds.draw(screen)
     group_birds.update()
     c_time = pygame.time.get_ticks()
     if c_time - l_time > 3000:
       pipe_object_b = pipe(600,590,False)
       pipe_object_t = pipe(600,0,True)
       group_pipe.add(pipe_object_b)
       group_pipe.add(pipe_object_t)
       l_time = c_time
     group_pipe.update()
     for event in pygame.event.get():
          if event.type == pygame.MOUSEBUTTONDOWN:
               start = True
          if event.type == pygame.QUIT:
               pygame.quit()
               sys.exit()
     pygame.display.update()