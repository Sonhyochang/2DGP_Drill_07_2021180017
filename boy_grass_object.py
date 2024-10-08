from cgitb import small

from pico2d import *
import random

# Game object class here
class Grass:
    # 생성자 함수 : 객체의 초기 상태를 설정
    def __init__(self):
        # 모양없는 남작한 붕어빵의 초기 모습 결정
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400,30)

    def update(self): pass

class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100,700), 90
        self.frame = random.randint(0,7)
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)

class Small:
    def __init__(self):
        self.x, self.y = random.randint(0,800), 599
        self.image = load_image('ball21x21.png')

    def update(self):
        if self.y >= 30:
            self.y -= random.randint(5, 20)

    def draw(self):
        if self.y >= 60:
            self.image.draw(self.x, self.y)
        else:
            self.image.draw(self.x, 60)

class Big:
    def __init__(self):
        self.x, self.y = random.randint(0,800), 599
        self.image = load_image('ball41x41.png')

    def update(self):
        if self.y >= 30:
            self.y -= random.randint(5,20)

    def draw(self):
        if self.y >= 70:
            self.image.draw(self.x,self.y)
        else:
            self.image.draw(self.x, 70)

# 객체 이름 = 클래스(Class 대부분 대문자 시작)
def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

def reset_world():
    global running
    global grass
    global team
    global small_team
    global big_team
    global world

    running = True
    world = []

    grass = Grass() # 잔디를 찍어 낸다, 생성한다
    world.append(grass)

    team = [Boy() for i in range(10)]
    world += team


    small_team = [Small() for i in range(10)]
    world += small_team

    big_team = [Big() for i in range(10)]
    world += big_team

running  = True


def update_world():
    for o in world:
        o.update()

def render_world():
    clear_canvas()
    for o in world:
        o.draw()
    update_canvas()

open_canvas()

# initialization code

reset_world()

# game main loop code
while running:
    # game logic
    handle_events()
    update_world() # 상호작용을 시물레이션
    render_world() # 그 결과를 보여줌
    delay(0.05)


# finalization code

close_canvas()
