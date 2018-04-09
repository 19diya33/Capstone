import os
import random
import math
import spgl


#Size of things
	#Columns = 10
	#Rows = 20
	#

#Game Setup
game = spgl.Game(800, 1600, "black", "Tetris")


#Classes
class Grid(object):
	def __init__(self):
		grid = ["B", "B", "B", "B", "B", "B", "B", "B", "B", "B"]
		
		
class Block(spgl.Sprite):
	def __init__(self, shape, colour):
		pass

	def tick(self):
		self.move()
	
	def move(self):
		#self.setheading(270)
		pass
	
class Next(spgl.Sprite):
	def __init__(self, shape, colour):
		pass
		
	def choose_next(self):
		next_block = random.randint(1, 7)
		pass
		
	def show_next(self):
		#find a way to display the next block
		pass
	
class Tetris(object):
	def __init__(self):
		self.speed = 1
	
	def rotate_block(self):
		self.right(90)
		
	def move_left(self):
		#self.setheading(180)
		self.forward(-10)
		
	def move_right(self):
		#self.setheading(0)
		self.forward(10)
		
	def move_down(self):
		self.speed += 1
		
	def hold(self):
		#hold current block for future use
		pass
	
	def instadrop(self):
		#immediately puts block down
		#lower x coordinates to highest point thats directly underneath?
		pass
		
	def pause(self):
		#quit or resume
		pass
			
class Border(object):
	def __init__(self):
		pass
	
	def draw_border(self):
		pass
			
#class Red_block(Block):

#class Green_block(Block):

#class Orange_block(Block):

#class Blue_block(Block):

#class Cyan_block(Block):

#class Purple_block(Block):

#class Yellow_block(Block):


#Highscore
game.highscore = 0

#Loading Highscore
highscore = game.load_data("highscore")
if highscore:
    game.highscore = highscore
else:
    game.highscore = 0


def isCollision(t1, t2):	
	a = t1.xcor()-t2.xcor()
	b = t1.ycor()-t2.ycor()
	distance = math.sqrt((a ** 2) + (b ** 2))

#Check to make sure it works ^^	

player = Tetris()

#Commands
game.set_keyboard_binding(spgl.KEY_UP, player.rotate_block)
game.set_keyboard_binding(spgl.KEY_LEFT, player.move_left)
game.set_keyboard_binding(spgl.KEY_RIGHT, player.move_right)
game.set_keyboard_binding(spgl.KEY_DOWN, player.move_down)
game.set_keyboard_binding(spgl.KEY_SPACE, player.instadrop)
game.set_keyboard_binding(spgl.KEY_ESCAPE, player.pause)
game.set_keyboard_binding(spgl.KEY_SHIFT_LEFT, player.hold)

while True:
	game.tick()
