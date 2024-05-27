
'''
    In this project we demonstrated the use of the pygame library in python to create a fast clicker game
    combining the use of classes and objects in python, we created a simple game where the user is required
    to click on a box that displays the text "Click me" and the box changes color when clicked, the user is

    this game tests the user's reaction time and the user is required to click on the box as fast as possible
'''

import pygame
from random import randint
from time import time

pygame.init()

mw = pygame.display.set_mode((500,500))
mw.fill((255,0,0))
class Area():
  def __init__(self, x = 0, y = 0, width = 10, height = 10, color = None):
      self.rect = pygame.Rect(x, y, width, height) 
      self.fill_color = color
      self.x = x
      self.y = y
  def color(self, new_color):
      self.fill_color = new_color
  def fill(self):
      pygame.draw.rect(mw, self.fill_color, self.rect)
  def collidepoint(self, x,y):
      return self.rect.collidepoint(x,y)
  def outline(self, frame_color, thickness):
      pygame.draw.rect(mw, frame_color, self.rect, thickness)

#setting up fonts
class Label(Area):
    def placeText(self, text):
        return pygame.font.SysFont("verdana", 30).render(text, True, (0,255,0))
    def displayText(self, text):
        mw.blit(box.placeText(text), (self.x+5,self.y+5))
    
clock = pygame.time.Clock()
wait = 0

# making a timer text
timer_title  = pygame.font.SysFont("verdana", 30).render("Time:", True, (0,255,0))
mw.blit(timer_title, (0,0))
time_text = pygame.font.SysFont("verdana", 30)
mw.blit(time_text.render("0", True, (0,255,0)), (0,30))

# dealing with time counters
start_time = time()
current_time = start_time
while True:
    
    active_time = time() - current_time
    if active_time >= 1:
        current_time = time()
        time_text.render(round(active_time,0),True, (0,255,0) )

    pygame.display.update()
    clock.tick(40)
    click_x = 0
    click_y = 0

    if wait == 0:
        wait = 20
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                click_x, click_y = event.pos
        random_number = randint(0,3)
        box_list = []

# printing the 4 boxes instead of just 1
        x = 10
        for i in range(4):
            box = Label(x,100, 100,120,(0,0,255))
            if box.collidepoint(click_x,click_y):
                if random_number == i:
                    box.color((9, 135, 43))
                else: 
                    box.color((237, 40, 26))
        
            box.fill()
            box_list.append(box)
            x = x + 100 + 8

# displaying the Click me value inside a random box
        box_list[random_number].displayText("Click me")
    else:
        wait = wait -1




pygame.display.flip()