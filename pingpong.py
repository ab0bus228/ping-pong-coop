from pygame import *

#класс-родитель для других спрайтов
class GameSprite(sprite.Sprite):
    #конструктор класса
    def init(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        #вызываем конструктор класса (Sprite):
        sprite.Sprite.init(self)

        #каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed

        #каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
 #метод, отрисовывающий героя на окне
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

#класс главного игрока
class Player(GameSprite):
   #метод для управления спрайтом стрелками клавиатуры
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed

#создаем окошко
back_color = (200, 255, 255)
win_width = 700
win_height = 500
display.set_caption("Ping-Pong")
window = display.set_mode((win_width, win_height))
window.fill(back_color)
# background = transform.scale(image.load(img_back), (win_width, win_height))

#!создание игрока и мяча

racket1 = Player('racket.png', 30, 200, 50, 150, 4)
racket2 = Player('racket.png', 520, 200, 50, 150, 4)
ball = GameSprite('tenis_ball.png', 200, 200, 50, 50, 4)

#переменная "игра закончилась": как только там True, в основном цикле перестают работать спрайты
finish = False
FPS = 60
clock = time.Clock()

#основной цикл игры:
run = True #флаг сбрасывается кнопкой закрытия окна
while run:
    #событие нажатия на кнопку Закрыть
    for e in event.get():
        if e.type == QUIT:
            run = False

    if not finish:
        racket1.reset()
        racket2.reset()
        ball.reset()

    display.update()
    clock.tick(FPS)