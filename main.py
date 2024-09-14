import sys
import random as r
import pygame as py
from constant import *

py.mixer.init()
py.mixer.music.set_volume(1.0)
py.mixer.pre_init(44100, 16, 2, 4096)
py.init()
py.time.delay(1000)

# constant

jump = 0
dups = 0
send = 1
drun = 1
game = 0
miss = 1
score = 0
speed = 10
record = 0
cactus_hit = 0
first_shot = 0
cactus_shot = 0

# screen set

py.display.set_caption("Stop those Dinosaur!!!")

# rect set

dinosaur_rect = py.Rect(50,400,50,50)
send_rect = py.Rect(800,400,50,50)
sight1_rect = py.Rect(800,500,50,10)
cactus_shot_rect = py.Rect(800,600,25,50)
heart_rect = py.Rect(20,70,20,20)

# music

bgmusic = py.mixer.Sound("file\music.mp3")
click = py.mixer.Sound("file\switch_004.ogg")
hit = py.mixer.Sound("file\select_005.ogg")
bgmusic.play(loops = -1)

#anime

def main():
    global drun,send

    screen.fill(color["bg"])
    py.draw.rect(screen,color["gr"],ground_rect)
    
    if game == 0:
        startscreen()
    elif game == 1:
        gamemode()
    elif game == 2:
        gameover()
    elif game == 3:
        information()

def information():

    # info

    screen.blit(info_image,info_rect)

    #button

    xmark.draw()

def startscreen():
    global drun

    # button

    start.draw()
    info.draw()

    # dinosaur

    if drun < 3:
        screen.blit(dinosaur_image_run2,dinosaur_rect)
        drun += 1
    else:
        screen.blit(dinosaur_image_run1,dinosaur_rect)
        drun += 1
        if drun > 4:
            drun = 1
    
    # cactus

    screen.blit(cactus_shot_image,cactus_shot_rect_0)

    #title

    screen.blit(title_image,title_rect)

def gamemode():

    global cactus_shot,drun,send,dups,jump,cactus_hit,first_shot,score,speed,miss,game,record

    # send

    send_rect.x -= speed+5
    screen.blit(send_image[send],send_rect)
    if send_rect.x < -100:
        send_rect.x = 800
        send = r.randrange(0,3)

    # dinosaur

    # move

    if drun < 3:
        screen.blit(dinosaur_image_run2,dinosaur_rect)
        drun += 1
    else:
        screen.blit(dinosaur_image_run1,dinosaur_rect)
        drun += 4
        if drun > 8:
            drun = 1

    # jump

    if sight1_rect.x < 200 and first_shot >= 200 and jump == 0 and cactus_shot:
        jump = 1
        dups = 20
    
    if jump:
        if dinosaur_rect.y - dups < 400:
            dinosaur_rect.y -= dups
        else:
            dinosaur_rect.y = 400
        dups -= 1
        if 400 < sight1_rect.x < 600:
            dups -= 10
    
    if 200 < sight1_rect.x < 400:
        jump = 0
        dinosaur_rect.y = 400

    # hit

    if sight1_rect.x < 200 and 60 < first_shot < 200 and cactus_shot_rect.y < 500:
        if cactus_hit == 0:
            score += 1
            speed += 1
            miss = 0
            cactus_hit += 1
            if score > record:
                record = score
            hit.play()
            screen.blit(dinosaur_image_hit1,dinosaur_rect)
            cactus_hit += 1
            send_rect.x += 10
        elif cactus_hit == 1:
            screen.blit(dinosaur_image_hit2,dinosaur_rect)
            cactus_hit += 1
            send_rect.x += 10

    if sight1_rect.x < 400 and sight1_rect.x > 200:
        cactus_hit = 0
        
    # signt

    sight1_rect.x -= speed
    if cactus_shot == 0:
        py.draw.rect(screen,color["sight"],sight1_rect)
    if sight1_rect.x < -150:
        sight1_rect.x = 800

    # cactus

    cactus_shot_rect.x = sight1_rect.x

    if cactus_shot == 1:
        if cactus_shot_rect.y > 400:
            cactus_shot_rect.y -= 50
            py.draw.rect(screen,color["sight"],sight1_rect)
        screen.blit(cactus_shot_image,cactus_shot_rect)

    if cactus_shot_rect.x == 800:
        cactus_shot_rect.y = 600
        cactus_shot = 0
        first_shot = 0
        miss += 1
    
    # score

    score_image = txt_font.render("score "+str(score),True,color['score'],color['bg'])
    score_rect = score_image.get_rect()
    score_rect.x = 20
    score_rect.y = 20
    screen.blit(score_image,score_rect)
    
    # heart

    for i in range(2,5):
        if i > miss:
            heart_rect.x = possion[i-2]
            screen.blit(heart_image,heart_rect)
    
    # break

    if miss > 3:
        game = 2
        dinosaur_rect.y = 400

    # ground

    py.draw.rect(screen,color["gr"],ground_rect)
    if cactus_shot == 0 or cactus_shot_rect.y > 400:
        py.draw.rect(screen,color["sight"],sight1_rect)

    # tip

    if miss > 1 and score == 0:
        screen.blit(tip_image,tip_rect)

def gameover():
    global drun

    # button

    again.draw()
    back.draw()

    # dinosaur

    if drun < 3:
        screen.blit(dinosaur_image_run2,dinosaur_rect)
        drun += 1
    else:
        screen.blit(dinosaur_image_run1,dinosaur_rect)
        drun += 1
        if drun > 4:
            drun = 1

    # cactus

    screen.blit(cactus_shot_image,cactus_shot_rect_0)

    # game over

    screen.blit(gameover_image,gameover_rect)

    # score

    score_image = txt_font.render("score "+str(score),True,color['score'],color['bg'])
    score_rect = score_image.get_rect()
    score_rect.centerx = screen_rect.centerx-100
    score_rect.y = 200
    screen.blit(score_image,score_rect)

    #record

    record_image = txt_font.render("record "+str(record),True,color['score'],color['bg'])
    record_rect = record_image.get_rect()
    record_rect.centerx = screen_rect.centerx+100
    record_rect.y = 200
    screen.blit(record_image,record_rect)

# main loop

while 1:
    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            sys.exit()
        if event.type == py.KEYDOWN or event.type == py.MOUSEBUTTONDOWN:
            mouse = py.mouse.get_pressed()
            keys_pressed = py.key.get_pressed()
            if keys_pressed[py.K_SPACE] or mouse == (True, False, False):
                if cactus_shot == 0 and game == 1:
                    cactus_shot = 1
                    first_shot = cactus_shot_rect.x
        if event.type == py.MOUSEBUTTONDOWN:
            if start.out_rect.collidepoint(event.pos) and game == 0:
                click.play()
                game = 1
            if info.out_rect.collidepoint(event.pos) and game == 0:
                click.play()
                game = 3
            if xmark.out_rect.collidepoint(event.pos) and game == 3:
                click.play()
                game = 0
            if again.out_rect.collidepoint(event.pos) and game == 2:
                click.play()
                miss = 1
                game = 1
                score = 0
                speed = 10
            if back.out_rect.collidepoint(event.pos) and game == 2:
                click.play()
                miss = 1
                game = 0
                score = 0
                speed = 10

    main()
    py.display.update()
    clock.tick(framerate)