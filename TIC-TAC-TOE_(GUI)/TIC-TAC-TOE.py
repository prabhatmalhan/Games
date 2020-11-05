import turtle
import random
import pygame

def start_game() :

	#music initialization
	pygame.mixer.init()
	pygame.mixer.music.load('back.mp3')
	pygame.mixer.music.play(100)
	
	#setting up screen
	sc=turtle.Screen()
	sc.setup(width=1.0,height=1.0)
	sc.bgcolor("black")
	sc.title("TIC-TAC-TOE")
	sc.bgpic("back.gif")

	#configuring pen to draw
	pen_draw = turtle.Turtle()
	pen_draw.hideturtle()
	pen_draw.speed(0)
	pen_draw.pensize(6)

	#drawing grids
	pen_draw.color("gold")
	pen_draw.left(90)
	pen_draw.penup()

	#vertical lines
	a=-300
	for i in range(2) :
		a+=200
		pen_draw.setposition(a,-300)
		pen_draw.pendown()
		pen_draw.forward(600)
		pen_draw.penup()

	#horizontal lines
	a=-300
	pen_draw.right(90)
	for i in range(2) :
		a+=200
		pen_draw.setposition(-300,a)
		pen_draw.pendown()
		pen_draw.forward(600)
		pen_draw.penup()

	#drawing container box
	pen_draw.color("white")
	pen_draw.setposition(-300,-300)
	pen_draw.pendown()
	for i in range(4) : 
	    pen_draw.forward(600)
	    pen_draw.left(90)
	pen_draw.penup()

	#input in game

	b = Board(random.choice((-1,1)))
	Drawing.markactive(b.ac)
	sc.onclick(b.checkcoor)
	sc.mainloop()


class Board :
	
	def __init__ (self,ac) :
		self.board = [""]*9
		self.player = ['','X','O']
		self.ind = 1
		self.ac = ac
		self.onRun = True

	def fill(self,x,y) :
		if(self.board[x*3+y] == "") :

			self.board[x*3+y] = self.player[self.ind]
			self.display(x,y)
			des = Decision()
			if des.iswin(self.board,self.player[self.ind]) :
				Drawing.printres(self.player[self.ind])
				self.onRun = False
				restart()
				return
			elif des.isdraw(self.board) :
				Drawing.printres("draw")
				restart()
				return

			self.ac = -self.ac
			self.ind = -self.ind
			Drawing.markactive(self.ac)


	def checkcoor(self,y,x) :
		if -300<=x<=300 and -300<=y<=300 and self.onRun : 
			x=int(2-(x+300)//200)
			y=int((y+300)//200)
			self.fill(x,y)
			Drawing.markactive(self.ac)

	def display(self,x,y) : 
		a = -300+y*200+10
		b = -100+(2-x)*200-10
		dr = Drawing()
		if(self.ind==1):
			dr.drawX(a,b)
		else : 
			dr.drawC(a,b)


class Drawing : 
	def drawX(self,a,b) :
		markX = turtle.Turtle()
		markX.pensize(10)
		markX.speed(0)
		markX.hideturtle()
		markX.color("green")
		f=180
		for i in range(2) :
			markX.penup()
			markX.setposition(a,b)
			markX.pendown()
			markX.setposition(a+f,b-180)
			a+=180
			f=-f
	def drawC(self,a,b) :
		markC = turtle.Turtle()
		markC.pensize(10)
		markC.speed(0)
		markC.hideturtle()
		markC.color("green")
		markC.penup()
		markC.setposition(a+90,b-175)
		markC.pendown()
		markC.circle(85)

	def printres(mark) :
		markR = turtle.Turtle()
		markR.hideturtle()
		markR.pensize(30)
		markR.penup()
		markR.speed(0)
		markR.color("red")
		markR.setposition(0,-80	)
		markR.pendown()
		if mark == "draw" :
			markR.write("Game Draw", False, align="center", font=("Comic Sans MS", 80, "bold"))
		else :
			markR.write("{} wins".format(mark), False, align="center", font=("Comic Sans MS", 90, "bold"))

	def markactive(mark) :
		markA = turtle.Turtle()
		markA.clear()
		markA.hideturtle()
		markA.pensize(30)
		markA.speed(0)
		color = ["blue","white"]
		al = ["","right","left"]
		a = 1
		for col in color[::-mark] :
			markA.penup()
			markA.color(col)
			markA.setposition(-400*a,0)
			markA.pendown()
			markA.write("PLAYER {}".format(int(-0.5*a+1.5)), False, align=al[a], font=("Comic Sans MS", 30 , "bold"))
			a = -a



class Decision :

	def iswin(self,board,mark) :
		return ((board[0] ==  board[1] ==  board[2] == mark) or 
			    (board[3] ==  board[4] ==  board[5] == mark) or 
			    (board[6] ==  board[7] ==  board[8] == mark) or
			    (board[0] ==  board[3] ==  board[6] == mark) or 
			    (board[1] ==  board[4] ==  board[7] == mark) or
			    (board[2] ==  board[5] ==  board[8] == mark) or
			    (board[0] ==  board[4] ==  board[8] == mark) or
			    (board[2] ==  board[4] ==  board[6] == mark))

	def isdraw(self,board) :
		for i in range(9) :
			if board[i]=='' :
				return False
		return True


def restart() :
	pen = turtle.Turtle()
	pen.hideturtle()
	pen.pensize(20)
	pen.penup()
	pen.speed(0)
	pen.color("red")
	pen.setposition(-300,-350)
	pen.pendown()
	pen.write("!!! PRESS ENTER TO REPLAY !!!", False, align="center", font=("Comic Sans MS", 20, "bold"))
	pen.penup()
	pen.setposition(300,-350)
	pen.pendown()
	pen.write("!!! PRESS Space TO EXIT !!!", False, align="center", font=("Comic Sans MS", 20, "bold"))
	src = turtle.Screen()
	src.listen()
	src.onkeypress(src.bye,"space")
	src.onkeypress(cleaning,"Return")

def cleaning() :
	turtle.Screen().clear()
	start_game()

if __name__ == "__main__" : 
	start_game()