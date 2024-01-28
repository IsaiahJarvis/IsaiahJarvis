#developed in pygame 2.1.3.dev8 (SDL 2.0.22, Python 3.11.0) with with IDLE
#had to install "pip install pygame --pre" version of pygame to use it with 3.11.0
#also ran on pygame 2.1.0 on python 3.10.0
import sys, pygame, math, random, ctypes
pygame.init()

#variables
random.seed()
size = width, height = 800, 500
mid = (400, 250)
game_over_sound = pygame.mixer.Sound("gameover.wav")

#scoreboard
font = pygame.font.Font(None, 64)
pscore = font.render("0", True, (255, 255, 255))
cscore = font.render("0", True, (255, 255, 255))
pscore_pos = (600, 10)
cscore_pos = (200, 10)
pscore_num = 0
cscore_num = 0

#system clock
clock = pygame.time.Clock()

#rects
screen = pygame.display.set_mode(size)
ball = pygame.draw.circle(screen, 'brown', mid, 7)
paddleL = pygame.Rect(15, 1, 10, 90)
paddleR = pygame.Rect(775, 1, 10, 90)

def mouse():
    if pygame.mouse.get_pos()[1] < 455:
        x, y = pygame.mouse.get_pos()
        if not y < 45: 
            paddleR.top = y - 45
        return None

def end_box(title, text):
    return ctypes.windll.user32.MessageBoxW(0, text, title, 4)

def get_speed():
    speed = [math.cos(random.uniform(5, 10)) * 10, math.sin(random.uniform(5, 10)) * 10]
    while abs(speed[0]) < 1 or abs(speed[1]) < 1:
        speed = speed = [math.cos(random.uniform(5, 10)) * 10, math.sin(random.uniform(5, 10)) * 10]
    return speed

ballspeed = get_speed()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    if (cscore_num >= 5):
        pygame.mixer.Sound.play(game_over_sound)
        pygame.mixer.music.stop()
        if end_box("Game Over", "Do you wish to countinue?") == 6:
            ball.center = mid
            pscore_num = 0
            cscore_num = 0
            cscore = font.render(str(cscore_num), True, 'white')
            screen.blit(cscore, cscore_pos)
            pygame.display.flip()
        else:
            pygame.quit()
            sys.exit()

    #mouse control
    mouse()

    #ball move + bounce
    ball = ball.move(ballspeed)
    if ball.top < 0 or ball.bottom > height:
        ballspeed[1] = -ballspeed[1]
    if pygame.Rect.colliderect(ball, paddleL):
        ballspeed[0] = -ballspeed[0]
    if pygame.Rect.colliderect(ball, paddleR):
        ballspeed[0] = -ballspeed[0]

    #reset location
    if (ball.left < 0):
        pscore_num = pscore_num + 1
        pscore = font.render(str(pscore_num), True, 'white')
        ball.center = mid
        ballspeed = get_speed()

    if (ball.left > 790):
        cscore_num = cscore_num + 1
        cscore = font.render(str(cscore_num), True, 'white')
        ball.center = mid
        ballspeed = get_speed()

    #follow ball
    if ball.top > 45 and ball.top < 455:
        paddleL.top = ball.top -45

    #drawing
    screen.fill('black')
    screen.blit(cscore, cscore_pos)
    screen.blit(pscore, pscore_pos)
    pygame.draw.rect(screen, 'red', paddleL)
    pygame.draw.rect(screen, 'red', paddleR)
    pygame.draw.circle(screen, 'brown', ball.center, ball.width / 2) 
    pygame.display.flip()
    clock.tick(60)


