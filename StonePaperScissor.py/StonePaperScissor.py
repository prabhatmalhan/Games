import turtle
import random

class run :
	def __init__(self) :
		self.gameon=True
		self.score=[0]*2

r=run()

#SCREEN setup
src = turtle.Screen()
src.setup(width=1.0,height=1.0)
src.bgcolor("black")
src.title("STONE PAPER SCISSORS")
src.register_shape("player/stone.gif")
src.register_shape("player/paper.gif")
src.register_shape("player/scissor.gif")
src.register_shape("computer/stone.gif")
src.register_shape("computer/paper.gif")
src.register_shape("computer/scissor.gif")
src.register_shape("icon/ico1.gif")
src.register_shape("icon/ico2.gif")
src.register_shape("icon/ico3.gif")


#player : computer defined
computer = turtle.Turtle()
computer.penup()
computer.speed(0)
computer.setposition(-225,0)


#player : user defined
player = turtle.Turtle()
player.penup()
player.speed(0)
player.setposition(225,0)


#headings
pen = turtle.Turtle()
penx = turtle.Turtle()
dec = turtle.Turtle()

pen.hideturtle()
pen.color("red")
pen.penup()
pen.speed(0)
pen.pensize(7)
pen.setposition(-250,300)
pen.pendown()
pen.write('Computer', False, align="center", font=("mv boli", 40, "bold"))
pen.penup()
pen.setposition(220,300)
pen.pendown()
pen.write('Player', False, align="center", font=("mv boli", 40, "bold"))


#scores
scor = turtle.Turtle()
scor.hideturtle()
scor.color("white")
scor.penup()
scor.speed(0)
scor.pensize(8)
scor.setposition(-250,240)
scor.pendown()
scor.write(f'{r.score[0]}', False, align="center", font=("mv boli", 40, "bold"))
scor.penup()
scor.setposition(220,240)
scor.pendown()
scor.write(f'{r.score[1]}', False, align="center", font=("mv boli", 40, "bold"))


#CHOICE box
pen.color("white")
pen.penup()
pen.pensize(5)
pen.setposition(550,150)
pen.pendown()
pen.forward(100)
for i in range(3) :
	pen.penup()
	pen.setposition(650,150-i*100)
	pen.pendown()
	for j in range(3) :
		pen.right(90)
		pen.forward(100)
	pen.right(90)


#choices
stone = turtle.Turtle()
stone.penup()
stone.speed(0)
stone.shape("icon/ico1.gif")
stone.setposition(610,100)
paper = turtle.Turtle()
paper.penup()
paper.speed(0)
paper.shape("icon/ico2.gif")
paper.setposition(603,-7)
scissor = turtle.Turtle()
scissor.penup()
scissor.speed(0)
scissor.shape("icon/ico3.gif")
scissor.setposition(605,- 105)


#to display the choices on screen
def printcho(p,c) :
	plc=['stone','paper','scissor']	
	computer.shape("computer/"+plc[c-1]+".gif")	
	player.shape("player/"+plc[p-1]+".gif")	
	computer.showturtle()
	player.showturtle()
	iswin(p,c)
	

def score_update() :
	scor.clear()
	scor.penup()
	scor.setposition(-250,240)
	scor.pendown()
	scor.write(f'{r.score[0]}', False, align="center", font=("mv boli", 40, "bold"))
	scor.penup()
	scor.setposition(220,240)
	scor.pendown()
	scor.write(f'{r.score[1]}', False, align="center", font=("mv boli", 40, "bold"))

#updation of score
def result(x):
	r.score[x]+=1
	score_update()
	if(r.score[x]==5) :
		r.gameon=False
		declare_win(x)
		restart()


#declaring winner
def declare_win(x) :
	winner=['COMPUTER','PLAYER']
	dec.hideturtle()
	dec.color("gold")
	dec.penup()
	dec.setposition(0,-250)
	dec.pendown()
	dec.write(winner[x]+' wins !!!', False, align="center", font=("Agency FB", 60, "bold"))


#declaration of winner
def iswin(p,c) :
	if(p==c) :
		pass
	elif ((p==1 and c==2) or (p==2 and c==3) or (p==3 and c==1)) :
		result(0)
	else :
		result(1)


#checking choice
def check (x,y) :
	if 550<=x<=650 and -150<=y<150 and r.gameon==True: 
		printcho(int(3-(y+150)//100),random.randint(1,3))


def restart() :
	penx.hideturtle()
	penx.pensize(20)
	penx.penup()
	penx.speed(0)
	penx.color("red")
	penx.setposition(0,-300)
	penx.pendown()
	penx.write("!!! PRESS ENTER TO REPLAY !!!", False, align="center", font=("Comic Sans MS", 20, "bold"))
	penx.penup()
	penx.setposition(0,-340)
	penx.pendown()
	penx.write("!!! PRESS Space TO EXIT !!!", False, align="center", font=("Comic Sans MS", 20, "bold"))
	src = turtle.Screen()
	src.listen()
	src.onkeypress(src.bye,"space")
	src.onkeypress(cleaning,"Return")


def cleaning() :
	r.score[0]=0
	r.score[1]=0
	r.gameon=True
	penx.clear()
	dec.clear()
	computer.hideturtle()
	player.hideturtle()
	score_update()


#start game
src.listen()
src.onclick(check)
src.mainloop()