# Joey Maalouf
# a more advanced physics simulation with a bouncing ball

import sys
import time
import pygame
pygame.init()

# objects
myfont = pygame.font.SysFont("monospace", 16)
size = width, height = 640, 480
screen = pygame.display.set_mode(size)
diameter = 8
startx = 0
starty = 0
ballrect = pygame.Rect(startx, starty, diameter, diameter)
trace = []

# colors
black = 0, 0, 0
white = 255, 255, 255
red = 255, 0, 0
green = 0, 255, 0

# forces
friction = 0.02
gravity = 4

# velocity
Vx = 6.5
Vy = 0

# acceleration
Ax = 0
Ay = gravity

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    time.sleep(0.05)

    # ground friction
    if ballrect.bottom >= height:
        if abs(Vx) <= friction:
            Ax = 0
            break
        elif Vx < -friction:
            Ax = friction
        elif Vx > friction:
            Ax = -friction
    else:
        Ax = 0

    Vx += Ax
    Vy += Ay

    ballrect.centerx += Vx
    ballrect.centery += Vy

    if ballrect.left < 0:
        Vx = -Vx
    if ballrect.right > width:
        Vx = -Vx
    if ballrect.top < 0:
        Vy = -Vy
    if ballrect.bottom > height:
        Vy = -Vy + Ay
        ballrect.bottom = height

    screen.fill(black)
    trace.append(ballrect.center)
    for dot in trace:
        pygame.draw.circle(screen, red, dot, 1)
    vtext = "Vx: %06.2f Vy: %06.2f" % (Vx, Vy)
    atext = "Ax: %06.2f Ay: %06.2f" % (Ax, Ay)
    vlabel = myfont.render(vtext, 1, white)
    alabel = myfont.render(atext, 1, white)
    screen.blit(vlabel, (0, 0))
    screen.blit(alabel, (0, 16))
    pygame.draw.circle(screen, white, ballrect.center, round(ballrect.width/2))
    pygame.display.flip()

dtext = "done in %03d frames" % len(trace)
dlabel = myfont.render(dtext, 1, green)
screen.blit(dlabel, (width/2-65, height/2-6))
pygame.display.flip()
time.sleep(2)
