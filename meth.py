#!/path/to/venv/bin/python

import sys, os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
import pygame
from datetime import datetime
from PIL import Image

# Constants (edit these to your liking)
SCREENSHOTS = '/home/tox/Math/METH/screenshots'
WIDTH = 800
HEIGHT = 600
BLACK = (30, 30, 46)
WHITE = (205, 214, 244)
PINK = (245, 194, 231)
YELLOW = (249, 226, 175)
RED = (243, 139, 168)
BLUE = (137, 180, 250)
GREEN = (166, 227, 161)

def main():

    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
    pygame.display.set_caption("Meth - a simple drawing program")
    canvas = pygame.Surface((WIDTH, HEIGHT))
    canvas.fill(BLACK)
    draw_radius = 2.5
    erase_radius = 10
    selected_color = WHITE
    
    drawing = False
    erasing = False
    clock = pygame.time.Clock()
    resize_flag = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: # LMB
                    drawing = True
                elif event.button == 3: # RMB
                    erasing = True
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:  
                    drawing = False
                elif event.button == 3:
                    erasing = False
            elif event.type == pygame.MOUSEMOTION:
                if drawing:
                    pygame.draw.circle(canvas, selected_color, event.pos, draw_radius)
                elif erasing:
                    pygame.draw.circle(canvas, BLACK, event.pos, erase_radius)

            elif event.type == pygame.KEYDOWN:
                match event.key:
                    case pygame.K_c:
                        canvas.fill(BLACK)
                    case pygame.K_s:
                        imgpath = os.path.join(SCREENSHOTS, f"DRAW-{datetime.now()}.png")
                        pygame.image.save(canvas, imgpath)
                    case pygame.K_p:
                        selected_color = PINK
                    case pygame.K_y:
                        selected_color = YELLOW
                    case pygame.K_r:
                        selected_color = RED
                    case pygame.K_g:
                        selected_color = GREEN
                    case pygame.K_b:
                        selected_color = BLUE
                    case pygame.K_w:
                        selected_color = WHITE
            
            elif event.type == pygame.VIDEORESIZE:
                resize_flag = True

        if resize_flag:
            new_width, new_height = pygame.display.get_surface().get_size()
            new_canvas = pygame.Surface((new_width, new_height))
            new_canvas.fill(BLACK)
            new_canvas.blit(canvas, (0, 0))
            canvas = new_canvas

            pygame.display.flip()
            resize_flag = False

        screen.fill(BLACK)
        screen.blit(canvas, (0, 0))
        pygame.display.flip()
        clock.tick(300)

if __name__ == "__main__":
    main()