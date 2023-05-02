from shooterlib import *
bg = transform.scale(image.load('resources/textures/galaxy.jpg'),(settings()['width'],settings()['height']))
player = Player_H("resources/textures/rocket.png", round(settings()['width']/2), 400,(70,100), 10)
monsters = []
spaceship = []
bullets = []
bullet_enable = True
bullet_enable2 = True
collide = False
score = 0
missed = 0
health = 10
kd = 10
kd2 = 0
for i in range(30):
    monsters.append(Monster("resources/textures/asteroid.png", randint(0 ,round(settings()['width']-100)),randint(-1500,-100),(100,100), randint(1,2)))
for i in range(5):
    spaceship.append(Monster("resources/textures/ufo.png", randint(0 ,round(settings()['width']-100)),randint(-1500,-100),(100,100), randint(2,3)))
font.init()
score_text = font.Font("resources/font.ttf", 32)
missed_text = font.Font("resources/font.ttf", 32)
health_text = font.Font("resources/font.ttf", 32)
kd_text = font.Font("resources/font.ttf", 32)
kd_render = kd_text.render('',True, (255,255,255))
game=True
run=True
clock = time.Clock()
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    if game:
        win.blit(bg,(0,0))
        key_p = key.get_pressed()
        kd2 +=1
        if kd==0 and kd2==200:
            kd = 10
            kd_render = kd_text.render('',True, (255,255,255))
        if key_p[K_SPACE]:
            if bullet_enable and bullet_enable2 and kd !=0:
                bullet_enable = False
                bullet_enable2 = False 
                bullets.append(Bullet("resources/textures/bullet.png", player.get_x()+20,player.get_y(),(30,30), -10))
                kd -=1
            elif kd==0:
                kd2 = 0
                kd_render = kd_text.render('Вы сбили перезарядку!',True, (255,255,255))
        else:
            bullet_enable2 = True
        player.update()
        player.k_update()
        for i in monsters:
            i.load()
            if sprite.collide_rect(player,i):
                health -=1
                i.reset()
        for i in spaceship:
            i.load()
            if i.get_y()>=settings()['height']+100:
                missed +=1
            if sprite.collide_rect(player,i):
                health -=1
                i.reset()
        for i in bullets:
            i.update()
            i.load()
            for b in spaceship:
                if sprite.collide_rect(i,b):
                    b.reset()
                    score += 1
                    if i.get_y()<=300:
                        bullet_enable = True
            for b in monsters:
                if sprite.collide_rect(i,b):
                    b.reset()
            if i.get_y() == 300:
                bullet_enable = True
            if i.get_y() <= -300:
                bullets.remove(i)
        if health <= 0:
            game = False
            kd_render = kd_text.render('Вы проиграли',True, (255,0,0))
    score_render = score_text.render('Счёт: '+str(score),True, (255,255,255))
    missed_render = missed_text.render('Пропущено: '+str(missed),True, (255,255,255))
    health_render = missed_text.render('Жизней: '+str(health),True, (255,255,255))
    win.blit(score_render, (0,0))
    win.blit(missed_render, (0,30))
    win.blit(health_render, (0,60))
    win.blit(kd_render,(settings()['width']/2,settings()['height']/2))
    display.update()
    clock.tick(settings()['fps'])