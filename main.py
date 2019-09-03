import pgzrun
import random
import time
import os

WIDTH = 640
HEIGHT = 480
apple = Actor('apple')
orange = Actor('orange')
pineapple = Actor('pineapple')
start_time = time.time()
now_time = 0
time_O = 0
END = False
end_time = 0
def draw():
    global end_time
    if END == False:
        screen.fill((174, 255, 182))
        apple.draw()
        orange.draw()
        pineapple.draw()
        screen.draw.text(str(time_O),topleft=(10,10),fontsize=30)
        end_time = time_O 
    else:
        end_game()
        #os.system("pause")

def on_mouse_down(pos):
    if apple.collidepoint(pos):
        print("Good Chot!(Apple)")
        place_apple()
    elif orange.collidepoint(pos):
        print("Good Chot!(Orange)")
        place_orange()
    elif pineapple.collidepoint(pos):
        print("Good Chot!(Pineapple)")
        place_pineapple()
    else:
        print("You Missed")

def update():
    global END
    if time_O <= 5:
        apple.y += 1
        orange.y += 1
        pineapple.y += 1
    elif (int(time_O)%3) == 0 or (int(time_O)%2) == 0 :
        apple.y += 6
        orange.y += 6
        pineapple.y += 6
    elif time_O >= 30:
        apple.y += 8
        orange.y += 8
        pineapple.y += 8
    else:
        apple.y += 3
        orange.y += 3
        pineapple.y += 3
    if apple.y > HEIGHT:
        END = True
        #place_apple()
        #quit()
    
    if orange.y > HEIGHT :
        END = True
        #place_orange()
        #quit()
    
    if pineapple.y > HEIGHT:
        END = True
        #place_pineapple()
        #quit()
    update_time()

def place_apple():
    apple.x = random.randint(40,600)
    apple.y = -60
def place_orange():
    orange.x = random.randint(40,600)
    orange.y = -60
def place_pineapple():
    pineapple.x = random.randint(40,600)
    pineapple.y = -60

def update_time():
    global time_O
    now_time = time.time()
    time_O = now_time-start_time

def end_game():
    screen.clear()
    screen.draw.text("Your Time : "+str(end_time),topleft=(10,10),fontsize=30)
    
    
place_apple()
place_orange()
place_pineapple()
start_time = time.time()
pgzrun.go()