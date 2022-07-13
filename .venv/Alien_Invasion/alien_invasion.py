from pickle import NONE
import sys
import pygame
from settings import Settings
from character import GokuSprite



class AlienInvasion:
  
   """Overall class to manage game assets and behavior."""
   
   
   def __init__(self):
      """Initialize the game, and create game resources."""
      pygame.init()
      self.settings = Settings()
      self.screen = pygame.display.set_mode(
         (self.settings.screen_width, self.settings.screen_height))
      
      #creating our sprite object
      self.character = GokuSprite(self)

      #creating a group with our sprite
      self.my_group = pygame.sprite.Group(self.character)

      #getting the pygame clock for handling fps
      self.clock = pygame.time.Clock()

      pygame.display.set_caption("Alien Invasion")
     
   
   
   def run_game(self):
      """Start the main loop for the game."""
      while True:

         self._check_events_()
         self._update_screen()

         
   #This takes in the decision on closing the window      
   def _check_events_(self):
         # Watch for keyboard and mouse events.
         for event in pygame.event.get():
            if event.type == pygame.QUIT:
               sys.exit()
            elif event.type == pygame.KEYDOWN:
               if event.key == pygame.K_SPACE:
                  self.character.animate()


    #This function takes in the code that draws the bg, ship and flips the screen    
   def _update_screen(self): 
       #Redraw the screen during each pass through the loop
      self.screen.fill(self.settings.bg_color)

         #updating the sprite
      self.my_group.update()

         #drawing the sprite
      self.my_group.draw(self.screen)

         #updating the display
      pygame.display.update()

         #delaying the loop with clock tick for 50FPS
      self.clock.tick(24)         
         
          # Make the most recently drawn screen visible.
      pygame.display.flip()





if __name__ == '__main__':
 # Make a game instance, and run the game.
 ai = AlienInvasion()
 ai.run_game()
