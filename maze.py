#создай игру "Лабиринт"!
from pygame import *

#МЕГАКЛАСС
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < 690:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 440:
            self.rect.y += self.speed
class Enemy(GameSprite):
    direction = "left"
    def update(self):
        if self.rect.x <= 500:
            self.direction = "right"
        if self.rect.x >= 660:
            self.direction = 'left'

        if self.direction == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed
class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height
        self.image = Surface((self.width, self.height))
        self.image.fill((color_1, color_2, color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
        draw.rect(window, (self.color_1, self.color_2, self.color_3), (self.rect.x, self.rect.y, self.width, self.height))





#создай окно игры
window = display.set_mode((700, 500))
display.set_caption('Лабиринт')
#задай фон сцены
background = transform.scale(image.load('background.jpg'), (700, 500))
#создай 2 спрайта и размести их на сцене
heros = Player('hero.png', 10, 400, 7)
cyber = Enemy('cyborg.png', 620, 250, 2)
gold = GameSprite('treasure.png', 620, 420, 0)
#создай стены
w1 = Wall(0, 0, 0, 1, 120, 380, 10)#чёрная
w2 = Wall(255, 0, 0, 1, 350, 380, 10)#красная
w4 = Wall(255, 255, 255, 500, 110, 10, 500)#белая
w3 = Wall(0, 0, 255, 100, 230, 400, 10)#синяя 
speed = 10
#Подключение в игру
game = True
finish = False
clock = time.Clock()
FPS = 60
#МУЗЫКА
mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()
money = mixer.Sound('money.ogg')
kick = mixer.Sound('kick.ogg')
font.init()
font = font.Font(None, 70)
win = font.render('YOU WIN!!', True, (255, 215, 0))
loss = font.render('YOU LOSE', True, (255, 215, 0))
while game:
#обработай событие «клик по кнопке "Закрыть окно"»
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.blit(background, (0, 0))
        heros.update()
        cyber.update()
        heros.reset()
        cyber.reset()
        gold.reset()
        w1.draw_wall()
        w2.draw_wall()
        w3.draw_wall()
        w4.draw_wall()
        if sprite.collide_rect(heros, w1) or sprite.collide_rect(heros, w2) or sprite.collide_rect(heros, w3) or sprite.collide_rect(heros, w4) or sprite.collide_rect(heros, cyber) :
            finish = True
            window.blit(loss, (200, 200))
            kick.play()
        if sprite.collide_rect(heros, gold):
            finish = True
            window.blit(win, (200, 200))
            money.play()

    display.update()
    clock.tick(FPS)