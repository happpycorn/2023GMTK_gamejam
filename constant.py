import pygame as py

py.init()

framerate = 30
size = (800, 600)
width, height = size
clock = py.time.Clock()

# image

image = {
    'drun1' : "file\dinosaur_run1.png",
    'drun2' : "file\dinosaur_run2.png",
    'dhit1' : "file\dinosaur_hit1.png",
    'dhit2' : "file\dinosaur_hit2.png",
    'send1' : "file\send1.png",
    'send2' : "file\send2.png",
    'send3' : "file\send3.png",
    'cshot' : "file\cactus_shot.png",
    'heart' : "file\heart.png",
    'info' : "file\info.png"
}

# color

color = {
    'bg' : (255, 191, 0),
    'gr' : (244, 164, 96),
    'sight' : (255, 0, 0),
    'score' : (139, 69, 19)
}

# screen

screen = py.display.set_mode(size,py.DOUBLEBUF,16)
screen_rect = screen.get_rect()

# ground

ground_rect = py.Rect(0,500,width,100)

# send

send1_image = py.image.load(image['send1']).convert_alpha()
send2_image = py.image.load(image['send2']).convert_alpha()
send3_image = py.image.load(image['send3']).convert_alpha()
send_image = [send1_image,send2_image,send3_image]

# heart

heart_image = py.image.load(image['heart']).convert_alpha()
possion = [80,50,20]

# txt

txt_font = py.font.SysFont(None,48)

# title

title_txt_font = py.font.SysFont(None,88)
title_image = title_txt_font.render("Stop those Dinosaur!!!",True,color['score'],color['bg'])
title_rect = title_image.get_rect()
title_rect.centerx = screen_rect.centerx
title_rect.y = 100

# gameover

gameover_image = title_txt_font.render("Game Over",True,color['score'],color['bg'])
gameover_rect = gameover_image.get_rect()
gameover_rect.centerx = screen_rect.centerx
gameover_rect.y = 100

# tip

tip_font = py.font.SysFont(None,30)
tip_image = tip_font.render("Press spacebar or click to make the cacti emerge",True,color['score'],color['gr'])
tip_rect = tip_image.get_rect()
tip_rect.x = 20
tip_rect.y = 520

# info

info_image = py.image.load(image['info']).convert_alpha()
info_rect = info_image.get_rect()
info_rect.center = screen_rect.center

# dinosaur

dinosaur_image_run1 = py.image.load(image['drun1']).convert_alpha()
dinosaur_image_run2 = py.image.load(image['drun2']).convert_alpha()
dinosaur_image_hit1 = py.image.load(image['dhit1']).convert_alpha()
dinosaur_image_hit2 = py.image.load(image['dhit2']).convert_alpha()

# cactus

cactus_shot_image = py.image.load(image['cshot']).convert_alpha()
cactus_shot_rect_0 = py.Rect(700,400,25,50)

# button

class button:
    def __init__(self,txt = "button",left = 0,top = 0,width = 100,height = 50):
        self.txt = txt
        self.rect = py.Rect(left,top,width,height)
        self.out_rect = py.Rect(left-5,top-5,width+10,height+10)
        self.font = py.font.SysFont(None,48)
        self.txt_image = txt_font.render(txt,True,color['score'],color['bg'])
        self.txt_rect = self.txt_image.get_rect()
        self.txt_rect.center = self.rect.center
        self.active = False
    def draw(self,screen = screen):
        py.draw.rect(screen,color["gr"],self.out_rect)
        py.draw.rect(screen,color["bg"],self.rect)
        screen.blit(self.txt_image,self.txt_rect)

info = button("info",350,400)
back = button("back",350,400)
start = button("start",350,300)
again = button("again",350,300)
xmark = button("X",700,50,50,50)