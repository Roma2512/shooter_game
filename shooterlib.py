from pygame import transform,display,sprite,image,font,time,event,QUIT,key,K_SPACE,K_w,K_s,K_a,K_d,K_UP,K_DOWN,K_RIGHT,K_LEFT
from random import randint
from os import path
from json import loads
class Entity(sprite.Sprite):
    def __init__(self, p_image, x, y, size, speed):
        super().__init__()
        self.object = transform.scale(image.load(p_image),size)
        self.speed = speed
        self.rect = self.object.get_rect()
        self.rect.x = x
        self.rect.y = y
    def update(self):
        win.blit(self.object,(self.rect.x,self.rect.y))
    def get_x(self):
        return self.rect.x
    def get_y(self):
        return self.rect.y
class Player(Entity):
    def k_update(self):
        key_p = key.get_pressed()
        if (key_p[K_LEFT] or key_p[K_a]) and self.rect.x > 5:
            self.rect.x-=5
        if (key_p[K_RIGHT] or key_p[K_d]) and self.rect.x < settings()['width']-80:
            self.rect.x+=5
        if (key_p[K_UP] or key_p[K_w]) and self.rect.y > 5:
            self.rect.y-=5
        if (key_p[K_DOWN] or key_p[K_s]) and self.rect.y < settings()['height']-80:
            self.rect.y+=5
class Player_H(Entity):
    def k_update(self):
        key_p = key.get_pressed()
        if (key_p[K_LEFT] or key_p[K_a]) and self.rect.x > 5:
            self.rect.x-=5
        if (key_p[K_RIGHT] or key_p[K_d]) and self.rect.x < settings()['width']-80:
            self.rect.x+=5
class Player_V(Entity):
    def k_update(self):
        key_p = key.get_pressed()
        if (key_p[K_UP] or key_p[K_w]) and self.rect.y > 5:
            self.rect.y-=5
        if (key_p[K_DOWN] or key_p[K_s]) and self.rect.y < settings()['height']-80:
            self.rect.y+=5
class Monster(Entity):
    def load(self):
        if self.rect.y <=settings()['height']+100:
            self.rect.y += self.speed
            win.blit(self.object,(self.rect.x,self.rect.y))
        else:
            self.rect.x =  randint(0 ,round(settings()['width']-100))
            self.rect.y = randint(-1500,-100)
            win.blit(self.object,(self.rect.x,self.rect.y))
    def reset(self):
        self.rect.x =  randint(0 ,round(settings()['width']-100))
        self.rect.y = randint(-1500,-100)
        win.blit(self.object,(self.rect.x,self.rect.y))
class Bullet(Entity):
    def load(self):
        self.rect.y += self.speed
        win.blit(self.object,(self.rect.x,self.rect.y))
    def reset(self):
        self.rect.y = 500
        self.rect.x = -100
        win.blit(self.object,(self.rect.x,self.rect.y))
def settings():
    try:
        if path.exists('settings.json'):
            file = open('settings.json', 'r')
            settings = file.read()
            settings = loads(settings)
            file.close()
        else:
            file = open('settings.json', 'w')
            file.write('{"width":800,"height": 600,"fps":60,"music": false, "title":"test"}')
            settings = {"width":800,"height": 600,"fps":60,"music": False, "title":"test"}
            file.close()
    except:
        file = open('settings.json', 'w')
        file.write('{"width":800,"height": 600,"fps":60,"music": false, "title":"test"}')
        settings = {"width":800,"height": 600,"fps":60,"music": False, "title":"test"}
        file.close()
    return settings
win = display.set_mode((settings()['width'],settings()['height']))
display.set_caption(settings()['title'])
lose = 0