from pygame.locals import QUIT,K_RIGHT,K_LEFT,K_UP,K_DOWN,K_ESCAPE
import pygame
from random import randint
from math import sqrt

screenSize = scrWidth, scrHeight = 800, 600
COLOURS = {
    'black' : (0,0,0),
    'green' : (0,255,0),
    'red'   : (255,0,0)
    }

snake_radius = 30
time_delay_ms = 100

class Music():
    
    def __init__(self):
        pygame.mixer.pre_init(44100,16,2,4096)
        pygame.init()
        
    def play_music(self):
        #Let's make some music
        pygame.mixer.music.load('music_background.mp3')
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1) #it will run continously
        
    def stop_music(self):
        pygame.mixer.music.stop()
        

class Game:
    def isCollision(self,x1,y1,x2,y2,bsize):
        if sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2) < bsize:
            return True
        return False
    
class Apple:
 
    def __init__(self,x,y):
        self.x = x
        self.y = y
 
    def draw(self, surface, image=None):
        #If needs to load images instead of colors
        #surface.blit(image,(self.x, self.y))
        pygame.draw.circle(surface, COLOURS['red'], (self.x,self.y), snake_radius) 

class Player:
    speed = 32
    direction = 1
    length = 3
    score = 0
    x = [0] * length
    y = [0] * length
    
    def __init__(self,length,x,y):
        self.length = length
        self.x[0] = x
        self.y[0] = y
        
    
    def update(self):    
            #update previous positions for longer snake
            for i in range(self.length-1,0,-1):
                self.x[i] = self.x[i-1]
                self.y[i] = self.y[i-1]
            
            #update directions of player
            if self.direction == 0:
                self.y[0] = self.y[0] - self.speed
                #if player moves out of the screen - take him to another side
                #of screen
                if self.y[0] + snake_radius < 0:
                    self.y[0] = screenSize[1]
                       
            if self.direction == 1:
                self.x[0] = self.x[0] + self.speed
                if self.x[0] - snake_radius > screenSize[0]:
                    self.x[0] = 0
                    
            if self.direction == 2:
                self.y[0] = self.y[0] + self.speed
                if self.y[0] - snake_radius > screenSize[1]:
                    self.y[0] = 0
                    
            if self.direction == 3:
                self.x[0] = self.x[0] - self.speed
                if self.x[0] + snake_radius < 0:
                    self.x[0] = screenSize[0]

    def moveUp(self):
        self.direction = 0

    def moveRight(self):
        self.direction = 1
        
    def moveDown(self):
        self.direction = 2
 
    def moveLeft(self):
        self.direction = 3
        
    def draw(self, surface,image=None):
        for i in range(self.length):
            #If needs to load images instead of colors
            #surface.blit(image,(self.x[i],self.y[i])) 
            pygame.draw.circle(surface, COLOURS['green'], (self.x[i],self.y[i]), snake_radius)
 
class App:
 
    def __init__(self):
        self._running = True
        self._display_surf = None
        #If needs to load images instead of colors
        #self._image_surf = None
        self.player = Player(3,20,40)
        self.game = Game() 
        self.apple = Apple(400,100)
        self.music = Music()
        self.music.play_music()
    
    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(screenSize)
        pygame.display.set_caption('Python Academy - Snake')
        self._running = True
        #If needs to load images instead of colors
        #self._image_surf = pygame.image.load("snake.jpg").convert()
        self._image_surf = pygame.display.get_surface()
 
    #On exit
    def on_event(self, event):
        if event.type == QUIT:
            self._running = False
 
    def on_loop(self):
        self.player.update()
        
        # does snake eat apple?
        for i in range(0,self.player.length):
            if self.game.isCollision(self.apple.x,self.apple.y,self.player.x[i], self.player.y[i],snake_radius):
                self.player.score += 1
                self.apple.x = randint(2,790)
                self.apple.y = randint(2,590)
                self.player.length += 1
                self.player.x.append(1000)
                self.player.y.append(1000)
 
 
        # does snake collide with itself?
        for i in range(2,self.player.length):
            if self.game.isCollision(self.player.x[0],self.player.y[0],self.player.x[i], self.player.y[i],snake_radius):
                pygame.time.delay(3000)
                self.music.stop_music()
                exit(0)
 
    def on_render(self):
        self._display_surf.fill(COLOURS['black'])
        #self._display_surf.blit(pygame.transform.scale(self._image_surf,(30,30)), (self.player.x, self.player.y))
        self.player.draw(self._display_surf)
        self.apple.draw(self._display_surf)
        font = pygame.font.Font(None,48)
        score_text = font.render("Score: {}".format(str(self.player.score)),True,COLOURS['red'])
        self._display_surf.blit(score_text,(600,0))
        pygame.display.flip()
 
    def on_cleanup(self):
        pygame.quit()
 
    def on_execute(self):
        if self.on_init() == False:
            self._running = False
 
        while( self._running ):
            pygame.event.pump()
            keys = pygame.key.get_pressed() 
 
            if (keys[K_RIGHT]):
                self.player.moveRight()
 
            if (keys[K_LEFT]):
                self.player.moveLeft()
 
            if (keys[K_UP]):
                self.player.moveUp()
 
            if (keys[K_DOWN]):
                self.player.moveDown()
 
            if (keys[K_ESCAPE]):
                self._running = False
 
            self.on_loop()
            self.on_render()
            pygame.time.delay(time_delay_ms)
            
        self.on_cleanup()
 
if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()