from turtle import Turtle,Screen
import random
import time

KEY_UP, KEY_DOWN, KEY_LEFT, KEY_RIGHT, KEY_PAUSE = "Up", "Down", "Left", "Right", 'space'
g_snake = None
g_monster = None
g_pen = None
g_screen = None
g_move = None

snake_pos = None # coordinates of the snake
monster_xcor = None # x coordinate of monster
monster_ycor = None # y coordinate of monster
isWinner = False
g_pause = False

food_list = [] # store food objects
position = [[]] # store food coordinates
stamp_pos = []
length = 5 # lenght of stamp size
g_contacted = 0 # number of contacted moment
i_list = [] # store consumed food items

def configureScreen(w=500,h=500):
    s = Screen()
    s.setup(w,h)
    s.title('Snake')
    s.tracer(0)
    return s

def configureTurtle(shape="square",color="red",x=0,y=0):
    t = Turtle(shape)
    t.up()
    t.color(color)
    t.goto(x,y)
    return t

def configureMonster(shape="square",color="purple"):
    global monster_xcor,monster_ycor
    m = Turtle(shape)
    m.up()
    m.color(color)

    monster_xcor = random.uniform(-230,230)
    monster_ycor = random.uniform(-210,-230)
    print(monster_xcor,monster_ycor)
    m.goto(monster_xcor,monster_ycor)
    return m

def writeIntro(x=-200):
    global g_pen
    g_pen = Turtle()
    g_pen.up()
    g_pen.hideturtle()
    s1 = "Welcome to the snake game."
    s2 = "You are going to use 4 arrow keys to move the snake around the screen,"
    s20 = "trying to consume all the food items before the monster catches you."
    s3 = "Click anywhere on the screen to start the game. Have fun!!!"
    g_pen.goto(x,200)
    g_pen.write(s1,False,'left',('Arial',10,'normal'))
    g_pen.goto(x,180)
    g_pen.write(s2,False,'left',('Arial',10,'normal'))
    g_pen.goto(x,160)
    g_pen.write(s20,False,'left',('Arial',10,'normal'))
    g_pen.goto(x,120)
    g_pen.write(s3,False,'left',('Arial',10,'normal'))

def moveUp():
    global g_move,g_pause
    g_pause = False
    g_move = KEY_UP

def moveDown():
    global g_move,g_pause
    g_pause = False
    g_move = KEY_DOWN

def moveRight():
    global g_move,g_pause
    g_pause = False
    g_move = KEY_RIGHT

def moveLeft():
    global g_move,g_pause
    g_pause = False
    g_move = KEY_LEFT

def isPause():
    global g_pause
    g_pause = not g_pause

def configureKey(s):
    s.onkey(moveUp,KEY_UP)
    s.onkey(moveDown,KEY_DOWN)
    s.onkey(moveLeft,KEY_LEFT)
    s.onkey(moveRight,KEY_RIGHT)
    s.onkey(isPause,KEY_PAUSE)

def moveSnake():
    global snake_pos,length
    snake_pos = g_snake.pos()
    endTime = time.time()
    if isWinner:
        print_winner()
    elif g_snake.distance(g_monster) > 20 and not g_pause:
        eatFood()
        if g_move == "Right":
            if validMove_right(snake_pos):
                crawl(g_snake.stampItems,length)
                extend(length)
                g_snake.setheading(0)
                g_snake.forward(20)
        elif g_move == "Up":
            if validMove_up(snake_pos):
                crawl(g_snake.stampItems,length)
                extend(length)
                g_snake.setheading(90)
                g_snake.forward(20)
        elif g_move == "Left":
            if validMove_left(snake_pos):
                print('valid')
                crawl(g_snake.stampItems,length)
                extend(length)
                g_snake.setheading(180)
                g_snake.forward(20)
        elif g_move == "Down":
            if validMove_down(snake_pos):
                crawl(g_snake.stampItems,length)
                extend(length)
                g_snake.setheading(270)               
                g_snake.forward(20)    
        g_screen.title("Snake: \t\t\t Contacted: {} \t\t Time: {}".format(g_contacted,int(endTime-startTime)))
        print(g_snake.pos())
        g_screen.update()
        # If snake is extending, the rate will decrease
    if len(g_snake.stampItems)==length or (len(g_snake.stampItems)<=5):
        g_screen.ontimer(moveSnake,300)
    else:
        g_screen.ontimer(moveSnake,400)
                    
def moveMonster():
    global monster_xcor,monster_ycor,snake_pos,isWinner
    snake_pos = g_snake.pos()
    monster_xcor = g_monster.pos()[0]
    monster_ycor = g_monster.pos()[1]

    contacted()
    if len(g_snake.stampItems)==50:
        isWinner = True
    choice = random.randint(0,1)
    move_distance = random.randint(18,22)
    print(monster_xcor,monster_ycor)

    if g_snake.distance(g_monster) < 20:
        print_gameOver()
    elif not isWinner:
        if (monster_xcor<=snake_pos[0]) and (monster_ycor<snake_pos[1]):
            if monster_xcor == snake_pos[0]:
                g_monster.setheading(90)
                g_monster.fd(move_distance)
            else:
                if choice == 0:
                    g_monster.setheading(0)
                    g_monster.fd(move_distance)
                else:
                    g_monster.setheading(90)
                    g_monster.fd(move_distance)
        elif (monster_xcor<snake_pos[0]) and (monster_ycor>=snake_pos[1]):
            if monster_ycor==snake_pos[1]:
                g_monster.setheading(0)
                g_monster.fd(move_distance)
            else:
                if choice == 0:
                    g_monster.setheading(0)
                    g_monster.fd(move_distance)
                else:
                    g_monster.setheading(270)
                    g_monster.fd(move_distance)
        elif (monster_xcor>=snake_pos[0]) and (monster_ycor>snake_pos[1]):
            if monster_xcor==snake_pos[0]:
                g_monster.setheading(270)
                g_monster.fd(move_distance)
            else:
                if choice == 0:
                    g_monster.setheading(180)
                    g_monster.fd(move_distance)
                else:
                    g_monster.setheading(270)
                    g_monster.fd(move_distance)
        elif (monster_xcor>snake_pos[0]) and (monster_ycor<=snake_pos[1]):
            if monster_ycor==snake_pos[1]:
                g_monster.setheading(180)
                g_monster.fd(move_distance)
            else:
                if choice == 0:
                    g_monster.setheading(90)
                    g_monster.fd(move_distance)
                else:
                    g_monster.setheading(180)
                    g_monster.fd(move_distance)
        g_screen.update()
        g_screen.ontimer(moveMonster,300)
               
def extend(length=5):
    global stamp_pos
    if len(g_snake.stampItems) < length:
        g_snake.color("blue","black")
        g_snake.stamp()
        stamp_pos.append(snake_pos)
        g_snake.color("red")

def crawl(item,length=5):
    global stamp_pos
    if len(item) == length:
        g_snake.color("blue","black")
        g_snake.stamp()
        stamp_pos.append(snake_pos)   
        g_snake.color("red")
        g_snake.clearstamp(g_snake.stampItems[0])
        stamp_pos.remove(stamp_pos[0])

def setFood():
    global food_list
    g_food1 = Turtle()
    g_food2 = Turtle()
    g_food3 = Turtle()
    g_food4 = Turtle()
    g_food5 = Turtle()
    g_food6 = Turtle()
    g_food7 = Turtle()
    g_food8 = Turtle()
    g_food9 = Turtle()
    food_list = [0,g_food1,g_food2,g_food3,g_food4,g_food5,g_food6,g_food7,g_food8,g_food9]

def configureFood(number=9):
    global position
    position = [[]]
    for i in range(1,number+1):
        food_list[i].hideturtle()
        food_list[i].up()
        coordinates = []
        while True:
            x = random.randint(-240,240)
            y = random.randint(-240,240)
            coordinates = [x,y]
            if (x!=0 and y!=0) and (x!=-200 and y!=-200) \
                and (coordinates not in position) and (x!=monster_xcor and y!=monster_ycor):
                position.append(coordinates)
                break
        food_list[i].goto(x,y)
        food_list[i].write(i)      
    print(position)

def eatFood(nunber=9):
    global i_list,length,isWinner
    for i in range(1,nunber+1):
        if (g_snake.distance(food_list[i]) < 20) and (i not in i_list):   
            i_list.append(i)
            food_list[i].clear()
            # move to a remote region so that next time snake passes through 
            # the previous coordinates, it will not extend
            position[i] = [600,600]
            length += i

def print_gameOver():
    g_pen = Turtle()
    g_pen.hideturtle()
    g_pen.up()
    g_pen.goto(snake_pos)
    g_pen.color('red')
    g_pen.write("Game Over!!!",False,"left",("Arial",20,"normal"))

def print_winner():
    g_pen = Turtle()
    g_pen.hideturtle()
    g_pen.up()
    g_pen.goto(snake_pos)
    g_pen.color('red')
    g_pen.write("Winner!!!",False,"left",("Arial",20,"normal"))

def validMove_left(snake_pos):
    return snake_pos[0] > -240
def validMove_right(snake_pos):
    return snake_pos[0] < 240
def validMove_up(snake_pos):
    return snake_pos[1] < 240
def validMove_down(snake_pos):
    return snake_pos[1] > -240

def contacted():
    global g_contacted
    monster_xcor,monster_ycor=g_monster.pos()
    for x,y in stamp_pos:
        if (x-monster_xcor)**2 + (y-monster_ycor)**2 < 400:
            g_contacted += 1

if __name__ == "__main__":
    g_screen = configureScreen()
    g_snake = configureTurtle()
    g_monster = configureMonster()
    writeIntro()

    def nextFrame(x,y):
        global startTime
        g_pen.clear()
        setFood()
        configureFood()
        startTime = time.time()
        moveMonster()
        moveSnake()

    configureKey(g_screen)
    g_screen.onclick(nextFrame)
    g_screen.update()
    g_screen.listen()
    g_screen.mainloop()
