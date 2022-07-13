import pygame

class GokuSprite(pygame.sprite.Sprite):
    """A class to manage the character."""

    #The parameter ai_game is a reference to the current instance of the class Alien_Invasion
    def __init__(self, ai_game):
        """Initialize the character and set its starting position. """
        #assign screen as an attribute of class Character
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        
        super(GokuSprite, self).__init__()

        #Load the Character and gets it rect
        self.images = []
        #In this case, it is not yet animating but only loading the images
        self.is_animating = False
        self.images.append(pygame.image.load('.venv/Alien_Invasion/images/goku-0.png'))
        self.images.append(pygame.image.load('.venv/Alien_Invasion/images/goku-1.png'))
        self.images.append(pygame.image.load('.venv/Alien_Invasion/images/goku-2.png'))
        self.images.append(pygame.image.load('.venv/Alien_Invasion/images/goku-3.png'))
        self.images.append(pygame.image.load('.venv/Alien_Invasion/images/goku-4.png'))
        self.images.append(pygame.image.load('.venv/Alien_Invasion/images/goku-5.png'))
        self.images.append(pygame.image.load('.venv/Alien_Invasion/images/goku-6.png'))
        self.images.append(pygame.image.load('.venv/Alien_Invasion/images/goku-7.png'))
        self.images.append(pygame.image.load('.venv/Alien_Invasion/images/goku-8.png'))
        self.images.append(pygame.image.load('.venv/Alien_Invasion/images/goku-9.png'))
        self.images.append(pygame.image.load('.venv/Alien_Invasion/images/goku-10.png'))
        self.images.append(pygame.image.load('.venv/Alien_Invasion/images/goku-11.png'))
        self.images.append(pygame.image.load('.venv/Alien_Invasion/images/goku-12.png'))
        self.images.append(pygame.image.load('.venv/Alien_Invasion/images/goku-13.png'))
        self.images.append(pygame.image.load('.venv/Alien_Invasion/images/goku-14.png'))
        self.images.append(pygame.image.load('.venv/Alien_Invasion/images/goku-15.png'))
        self.images.append(pygame.image.load('.venv/Alien_Invasion/images/goku-16.png'))

        #index value to get the image from the array
        #initially it is of value 0
        self.current_sprite = 0

        #now the image that we will display will be the index from the image array
        self.image = self.images[self.current_sprite]

        #get the rect of each value of the list
        for self.image in self.images:
            i =0
            i =+1
            self.rect = self.images[i].get_rect()

        #Start a new character at the mid left of the screen
        self.rect.midleft = self.screen_rect.midleft


        

    def animate(self):
        self.is_animating = True

    def update(self):
        #This only starts when we press on a key for it to start animating
        if self.is_animating == True:
            #when the update method is called, we will increment the index
            self.current_sprite+=1
            
            
        #if the index is larger than the total images
        if self.current_sprite >= len(self.images):
            #we will make the index to 0 again
            self.current_sprite = 0
            #we reset and stop the animation and turn it False
            self.is_animating = False


        
        #finally we will update the image that will be displayed
        self.image = self.images[self.current_sprite]
        
    
    