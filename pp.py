from pygame import *

FPS = 90
clock = time.Clock()

window = display.set_mode((700,700))
display.set_caption('PP Betka')

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        self.image = transform.scale(image.load(player_image), (size_x, size_y))    
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    def move_player(self):
        if key_pressed[K_s] and self.rect.y <= 599:
            self.rect.y += self.speed
        if key_pressed [K_w] and self.rect.y >= 1:
            self.rect.y -= self.speed
    def move_player2(self):
        if key_pressed[K_DOWN] and self.rect.y <= 699:
            self.rect.y += self.speed
        if key_pressed [K_UP] and self.rect.y >= 1:
            self.rect.y -= self.speed
class Ball(GameSprite):
    def update():
        if game != True:
            if ball.rect.y > 450:
                ball.rect.y += self.speed
            if ball.rect.x > 650:
                ball.rect.x += self.speed

speed = 1           
speed_x = 1
speed_y = 1

game = True

police_station = GameSprite('police-station.png',0,0,700,700,0)
player1 = GameSprite('s.png', 30, 20, 160, 160, 3)
player2 = GameSprite('s2.png', 500, 20, 160, 160, 3)
ball = Ball('b.png', 150,0, 50,50,5)
while game:

    police_station.reset()
    key_pressed = key.get_pressed()
    player1.reset()
    player2.reset()
    ball.reset()

    if game != False:
        ball.rect.x += speed_x
        ball.rect.y += speed_y
    if ball.rect.y > 650 or ball.rect.y < 0:
        speed_y *= -1
    if sprite.collide_rect(player1, ball) or sprite.collide_rect(player2, ball):
        speed_x *= -1


    for e in event.get():
        if e.type == QUIT:
            game = False
    player1.move_player()
    player2.move_player2()
    display.update()
    clock.tick(FPS)