from pygame import *
from random import randint

#создай окно игры
w = display.set_mode((700, 500))
display.set_caption("Догонялки")

#задай фон сцены
background = transform.scale(image.load("background.png"), (700, 500))

#создай 2 спрайта и размести их на сцене
sp1_widht, sp1_height = 50, 50
x1, y1 = 100, 300
speed = 1
sprite_1 = transform.scale(image.load("sprite1.png"), (100, 100))
sp2_widht, sp2_height = 50, 50
x2, y2 = 300, 400
new_x2, new_y2 = x2, y2
speed2 = 2
sprite_2 = transform.scale(image.load("sprite2.png"), (100, 100))
final = transform.scale(image.load("ea.jpg"), (700, 500))


clock = time.Clock()
FPS = 80

def is_touching():
    if abs(x1- x2) < sp1_widht + 14 and abs(y1 - y2) < sp1_height + 14:
        return True
    return False

def get_new_pos_sp2():
    global new_x2, new_y2
    if new_x2 == x2 and new_y2 == y2:
       new_x2, new_y2 = randint(1, 65) * 10, randint(1, 45) * 10

def enemy_move():
    global x2, y2, new_x2, new_y2
    if x2 in tuple(range(new_x2 - 10, new_x2 + 10)) and y2 in tuple(range(new_y2 - 10, new_y2 + 10)):
             get_new_pos_sp2()
    get_new_pos_sp2()
    if x2 > new_x2:
       x2 -= speed2
    elif x2 < new_x2:
       x2 += speed2
    if y2 > new_y2:
       y2 -= speed2
    elif y2 < new_y2:
       y2 += speed2

# def enemy_move():
#     global x2, y2, new_x2, new_y2
#     if x2 in tuple(range(new_x2 - 10, new_x2 + 10)) and y2 in tuple(range(new_y2 - 10, new_y2 + 10)):
#         get_new_pos_sp2()
#     x, y = x2, y2
#     dist_x = abs(x1 - x2)
#     dist_y = abs(y1 - y2)
#     if x2 > new_x2:
#        x2 -= speed2
#     if x2 < new_x2:
#        x2 += speed2
#     if y2 > new_y2:
#        y2 -= speed2
#     if y2 < new_y2:
#        y2 += speed2
#     if dist_x >= abs(x1 - x2) and dist_y >= abs(y1 - y2):
#         x2, y2 = x, y
#         get_new_pos_sp2()

def control():
    global x1, y1
    keys_pressed = key.get_pressed()
    if keys_pressed[K_LEFT] and x1 > 5:
        x1 -= speed
    if keys_pressed[K_RIGHT] and x1 < 595:
        x1 += speed
    if keys_pressed[K_UP] and y1 > 5:
        y1 -= speed
    if keys_pressed[K_DOWN] and y1 < 450:
        y1 += speed

# def control_2():
#     global x2, y2
#     keys_pressed = key.get_pressed()
#     if keys_pressed[K_a] and x2 > 5:
#         x2 -= speed
#     if keys_pressed[K_d] and x2 < 595:
#         x2 += speed
#     if keys_pressed[K_w] and y2 > 5:
#         y2 -= speed
#     if keys_pressed[K_s] and y2 < 450:
#         y2 += speed

game = True
#обработай событие «клик по кнопке "Закрыть окно"»
while game:
    for i in event.get():
        if i.type == QUIT:
            game = False
    
    w.blit(background, (0, 0))
    w.blit(sprite_1, (x1, y1))
    w.blit(sprite_2, (x2, y2))
    if is_touching():
        w.blit(final, (0, 0))
    else:
        control()
        # control_2()
        enemy_move()

    clock.tick(FPS)
    display.update()