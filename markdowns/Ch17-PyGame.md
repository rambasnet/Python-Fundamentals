# PyGame
http://openbookproject.net/thinkcs/python/english3e/pygame.html

- third-party package that is used in Game development using Python
- must install using pip - https://www.pygame.org/download.shtml

```bash
$ pip install pygame
```

- see documentation: http://openbookproject.net/thinkcs/python/english3e/pygame.html
- see `demos/pygamedemos` folder within the repository to run the provided source codes


```bash
%%bash
# install pygame
pip install pygame
```

    Requirement already satisfied: pygame in /Users/rbasnet/miniconda3/lib/python3.7/site-packages (1.9.4)


# The game loop

<img src="http://openbookproject.net/thinkcs/python/english3e/_images/pygame_structure.png">

In every game, in the setup section we’ll create a window, load and prepare some content, and then enter the game loop. The game loop continuously does four main things:

- it polls for events — i.e. asks the system whether events have occurred — and responds appropriately,
- it updates whatever internal data structures or objects need changing,
- it draws the current state of the game into a (non-visible) surface,
- it puts the just-drawn surface on display.


```python
import pygame

def main():
    """ Set up the game and run the main game loop """
    pygame.init()      # Prepare the pygame module for use
    surface_sz = 480   # Desired physical surface size, in pixels.

    # Create surface of (width, height), and its window.
    main_surface = pygame.display.set_mode((surface_sz, surface_sz))

    # Set up some data to describe a small rectangle and its color
    small_rect = (300, 200, 150, 90)
    some_color = (255, 0, 0)        # A color is a mix of (Red, Green, Blue)

    while True:
        ev = pygame.event.poll()    # Look for any event
        if ev.type == pygame.QUIT:  # Window close button clicked?
            break                   #   ... leave game loop

        # Update your game objects and data structures here...

        # We draw everything from scratch on each frame.
        # So first fill everything with the background color
        main_surface.fill((0, 200, 255))

        # Overpaint a smaller rectangle on the main surface
        main_surface.fill(some_color, small_rect)

        # Now the surface is ready, tell pygame to display it!
        pygame.display.flip()

    pygame.quit()     # Once we leave the loop, close the window.

main()
```

    pygame 1.9.4
    Hello from the pygame community. https://www.pygame.org/contribute.html



```python
import pygame
import time

def main():

    pygame.init()    # Prepare the PyGame module for use
    main_surface = pygame.display.set_mode((480, 240))

    # Load an image to draw. Substitute your own.
    # PyGame handles gif, jpg, png, etc. image types.
    ball = pygame.image.load("pygame/ball.png")
    ball = pygame.transform.scale(ball, [20, 20])
    # Create a font for rendering text
    my_font = pygame.font.SysFont("Courier", 16)

    frame_count = 0
    frame_rate = 0
    t0 = time.clock()

    while True:

        # Look for an event from keyboard, mouse, joystick, etc.
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:   # Window close button clicked?
            break                    # Leave game loop

        # Do other bits of logic for the game here
        frame_count += 1
        if frame_count % 500 == 0:
            t1 = time.clock()
            frame_rate = 500 / (t1-t0)
            t0 = t1

        # Completely redraw the surface, starting with background
        main_surface.fill((0, 200, 255))

        # Put a red rectangle somewhere on the surface
        main_surface.fill((255,0,0), (300, 100, 150, 90))

        # Copy our image to the surface, at this (x,y) posn
        main_surface.blit(ball, (100, 120))

        # Make a new surface with an image of the text
        the_text = my_font.render("Frame = {0},  rate = {1:.2f} fps"
                  .format(frame_count, frame_rate), True, (0,0,0))
        # Copy the text surface to the main surface
        main_surface.blit(the_text, (10, 10))

        # Now that everything is drawn, put it on display!
        pygame.display.flip()

    pygame.quit()


main()
```

    pygame 1.9.4
    Hello from the pygame community. https://www.pygame.org/contribute.html


    /Users/rbasnet/miniconda3/lib/python3.7/site-packages/ipykernel_launcher.py:18: DeprecationWarning: time.clock has been deprecated in Python 3.3 and will be removed from Python 3.8: use time.perf_counter or time.process_time instead
    /Users/rbasnet/miniconda3/lib/python3.7/site-packages/ipykernel_launcher.py:30: DeprecationWarning: time.clock has been deprecated in Python 3.3 and will be removed from Python 3.8: use time.perf_counter or time.process_time instead



```python

```
