import turtle
import math
import random
import winsound
import pygame
pygame.mixer.init()
pygame.mixer.music.load('sounds/intro.mp3')
pygame.mixer.music.play(100)
# intro


front = turtle.Screen()
front.bgcolor("black")
front.title("KNIGHT BATTLEGROUND")
front.bgpic("images/back.gif")
front.register_shape("images/sword.gif")
front.register_shape("images/enemy.gif")
front.register_shape("images/ZCi.gif")

intro = turtle.Turtle()
intro.speed(0)
intro.color("white")
intro.penup()
intro.setposition(-315, -315)
intro.pendown()
intro.pensize(3)
for i in range(4):
    intro.forward(630)
    intro.left(90)
intro.hideturtle()
swordstate="passive"
intro.penup()
intro.speed(0.5)
intro.color("turquoise")
intro.setposition(0, 150)
intro.write("KNIGHT", True, align="center", font=("Comic Sans MS", 50, "bold", "underline"))
intro.penup()
intro.setposition(0, 60)
intro.write("BATTLEGROUND", True, align="center", font=("Comic Sans MS", 52, "bold", "underline"))
intro.penup()
intro.color("gold")
intro.setposition(280, -20)
intro.write("-By PRABHAT MALHAN", True, align="right", font=("Comic Sans MS", 30, "bold", "italic"))
intro.penup()
intro.color("red")
intro.setposition(0, -130)
intro.write("!!!press enter to play!!!", True, align="center", font=("Comic Sans MS", 25, "normal"))
# Game Begins

def game_begin():
    try :
        global swordstate
        pygame.mixer.music.stop()
        pygame.mixer.music.load('sounds/back.mp3')
        pygame.mixer.music.play(100)

        front.clear()

        si = turtle.Screen()
        si.register_shape("images/sword.gif")
        si.register_shape("images/enemy.gif")
        si.register_shape("images/ZCi.gif")
        si.bgpic("images/back.gif")
        si.bgcolor("black")

        border_pen = turtle.Turtle()
        border_pen.speed(0)
        border_pen.color("white")
        border_pen.penup()
        border_pen.setposition(-315, -315)
        border_pen.pendown()
        border_pen.pensize(3)
        for i in range(4):
            border_pen.forward(630)
            border_pen.left(90)
        border_pen.hideturtle()

        knight = turtle.Turtle()
        knight.shape("images/ZCi.gif")
        knight.penup()
        knight.speed(0)
        knight.setposition(0, -219)
        knight.setheading(90)
        knight.speed = 0

        score = 0
        score_pen = turtle.Turtle()
        score_pen.speed(0)
        score_pen.color("white")
        score_pen.penup()
        score_pen.setposition(-290, 280)
        scorestring = "Score: {}".format(score)
        score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
        score_pen.hideturtle()

        def move_left():
            knight.speed = -10

        def move_right():
            knight.speed = 10 

        def move_knight():
            x = knight.xcor()
            x += knight.speed
            if x > 278:
                x = 278
            if x < -278:
                x = -278
            knight.setx(x)

        def fire():
            global swordstate
            if swordstate == "passive":
                swordstate = "active"
                winsound.PlaySound("sounds/fire.wav", winsound.SND_ASYNC)
                sword.setposition(knight.xcor(), knight.ycor() + 10)
                sword.showturtle()

        def isCollision(t1, t2):
            dist = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2))
            if dist < 25:
                return True
            else:
                return False

        si.listen()
        si.onkeypress(move_left, "Left")
        si.onkeypress(move_right, "Right")
        si.onkeypress(fire, "space")
        si.onclick(lambda x,y : move_left(),1)
        si.onclick(lambda x,y : move_right(),3)
        si.onclick(lambda x,y : fire(),2)

        enemy_number = 5
        enemies = []
        for i in range(enemy_number):
            enemies.append(turtle.Turtle())
        for enemy in enemies:
            enemy.penup()
            enemy.speed(0)
            enemy.shape("images/enemy.gif")
            enemy.setposition(random.randint(-250, 250), random.randint(180, 260))
        enemyspeed = 1

        sword = turtle.Turtle()
        sword.shape("images/sword.gif")
        sword.penup()
        sword.speed(0)
        sword.setposition(0, -400)
        sword.hideturtle()
        swordspeed = 30


        while True:
            flag = 0
            move_knight()
            for enemy in enemies:
                x = enemy.xcor()
                x += enemyspeed
                enemy.setx(x)

                if x < -280 or x > 280:
                    enemyspeed *= -1
                    for e in enemies:
                        e.sety(e.ycor() - 40)
                        if e.ycor() < knight.ycor():
                            flag = 1
                            si.clear()
                            break
                if isCollision(sword, enemy):
                    winsound.PlaySound("sounds/kill.wav", winsound.SND_ASYNC)
                    sword.hideturtle()
                    swordstate = "passive"
                    sword.setposition(0, -400)
                    enemy.setposition(random.randint(-200, 200), random.randint(200, 280))
                    score += 10
                    scorestring = "Score: {}".format(score)
                    score_pen.clear()
                    score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
                    score_pen.hideturtle()
                    enemyspeed += 0.25 if enemyspeed > 0 else -0.25

                if isCollision(knight, enemy):
                    knight.hideturtle()
                    flag = 1
                    si.clear()
                    break

            if swordstate == "active":
                sword.sety(sword.ycor() + swordspeed)

            if sword.ycor() > 280:
                sword.hideturtle()
                swordstate = "passive"

            if flag == 1:
                break
        pygame.mixer.music.stop()
        pygame.mixer.music.load("sounds/end.mp3")
        pygame.mixer.music.play(100)
        pygame.mixer.music.set_volume(10)
        # game stop

        si.bgcolor("black")
        si.bgpic("images/back.gif")
        border_pen.penup()
        border_pen.setposition(-315, -315)
        border_pen.pendown()
        for i in range(4):
            border_pen.forward(630)
            border_pen.left(90)
        border_pen.hideturtle()
        score_pen.penup()
        score_pen.color("yellow")
        score_pen.setposition(0, -30)
        score_pen.write("!!!GAME OVER!!!", False, align="center", font=("Times", 50, "normal"))
        score_pen.penup()
        score_pen.color("gold")
        score_pen.setposition(0, 100)
        score_pen.write(scorestring, False, align="center", font=("Courier", 40, "normal"))
        score_pen.hideturtle()
        si.mainloop()
    except :
        pass

front.listen()
front.onkeypress(game_begin, "Return")
front.mainloop()
