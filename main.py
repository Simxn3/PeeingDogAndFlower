 # imports
import pygame, os, sys 

# center pygame window on display
# technique found at https://stackoverflow.com/questions/5814125/how-to-designate-where-pygame-creates-the-game-window
os.environ['SDL_VIDEO_CENTERED'] = '1'

# initialize pygame
pygame.init()

# constants
WIDTH = 400
HEIGHT = 300
FPS = 2

# RGB colors
white = (255, 255, 255)
black = (0, 0, 0)

# variables
image_count = 0 # counter for images
clock = pygame.time.Clock() # clock object
running = True
timer = 0

# load images into pygame
my_images = [
pygame.image.load('./Pictures/frame_1.png'),
pygame.image.load('./Pictures/frame_2.png'),
pygame.image.load('./Pictures/frame_3.png'),
pygame.image.load('./Pictures/frame_4.png'),
pygame.image.load('./Pictures/frame_5.png'),
pygame.image.load('./Pictures/frame_6.png')
]

# changes size of all images to fit screen
for i in range(len(my_images)):
  my_images[i] = pygame.transform.scale(my_images[i], (300, 200))

# set Window
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Yellow Showers")
WINDOW.fill(white)
 
# set up your font
font = pygame.font.Font('Fonts/NYCD.ttf', 20)

# create your text
text = font.render('By: Simone and Layla', True, black, white)
textRect = text.get_rect()

# position the texty
textRect.center = (WIDTH // 2, HEIGHT // 7)

# display text
WINDOW.blit(text, textRect)
pygame.display.flip()

# draw shape function
def drawShape():
  global my_images
  global image_count
  if (image_count == 6):
    image_count = 0
  WINDOW.blit(my_images[image_count], (0, 100))
  pygame.display.flip()
  image_count += 1
  
# main animation Loop that will run for 10 seconds
while running and timer < 50:

  # upadate screen according to FPS value
  clock.tick(FPS)

  # update timer
  timer += 1

  # check if "X" is clicked by user 
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
      pygame.quit()
      sys.exit()

  # call to drawShape function
  drawShape()