import os
import random
import math
import spgl
import turtle
import time

#Size of things
	#Columns = 10
	#Rows = 20
	#CANVAS PIXELS
		#Width 530/398/265
		#Height 265/133

#Game Setup
game = spgl.Game(800, 1000, "black", "Tetris", 0)

#Set up screen

#Classes
class Grid(object):
	def __init__(self):
		self.width = 10
		self.height = 20
		self.grid = []
		
		for grid_y in range(self.height):
			self.grid.append([])
		
		for grid_y in range(self.height):
			
			for grid_x in range(self.width):
				self.grid[grid_y].append("B")
				
	def print_grid(self):
		for grid_y in range(self.height):
			line = ""
			for grid_x in range(self.width):
				line += self.grid[grid_y][grid_x]
			print(line)	


class Block(spgl.Sprite):
	def __init__(self, shape, colour, x, y):
		spgl.Sprite.__init__(self, shape, colour, x, y)
		self.grid_x = 5
		self.grid_y = 0
		
	def tick(self):
		self.move()
	
	def move(self):
	
		self.grid_y += 1
	
		screen_x = (self.grid_x * 20) - 100
		screen_y = 200 - (self.grid_y * 20) 
		
		self.goto(screen_x, screen_y)
		
		#Check if it's at the bottom
		if self.grid_y == 19:
			self.stamp()
			grid.grid[self.grid_y][self.grid_x] = "G"
			self.grid_x = 5
			self.grid_y = 0
		# Check if the next block is filled
		elif grid.grid[self.grid_y + 1][self.grid_x] == "G":
			self.stamp()
			grid.grid[self.grid_y][self.grid_x] = "G"
			self.grid_x = 5
			self.grid_y = 0			
			

			
	def move_left(self):
		self.grid_x -= 1
		
	def move_right(self):
		self.grid_x += 1
		
	def rotate_block(self):
		self.right(90)
		
	def block_under(self):
		#if self.grid_y
		pass
		
class Next(spgl.Sprite):
	def __init__(self, shape, colour):
		pass
		
	def choose_next(self):
		next_block = random.randint(1, 7)
		pass
		
	def show_next(self):
		#find a way to display the next block
		#(make a folder of all the shapes and choose them at random)
		#random.randint
		#spgl.Sprite.__init__(self, shape, colour, x, y)
		#self.shape("SINGLE_BLOCK_OUTLINE.gif")
		pass
	
	
class Player(object):
	def __init__(self):
		self.speed = 1
	
	def move_down(self):
		self.speed += 1
		
	def outline(self):
		#match the movement of the outline with the keyboard commands
		#directly onto the block pile at the bottom
		pass
		
	def hold(self):
		#hold current block for future use
		pass
	
	def instadrop(self):
		#immediately puts block down
		#lower y coordinates to highest point thats directly underneath?
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



#Instance

block = Block("SINGLE_BLOCK_OUTLINE.gif", "green", 133, 133)

grid = Grid()
grid.print_grid()


#Highscore
game.highscore = 0

#Loading Highscore
highscore = game.load_data("highscore")

if highscore:
    game.highscore = highscore
else:
    game.highscore = 0

#Labels
#score_label = spgl.Label("Score: 0 Highscore: {}".format(highscore), "white", -380, 280)
#lines_label = spgl.Label("Lines: {}".format(lines), "white", -380, 280)


#Collision checking
#def isCollision(t1, t2):	
#	a = t1.xcor()-t2.xcor()
#	b = t1.ycor()-t2.ycor()
#	distance = math.sqrt((a ** 2) + (b ** 2))

#Check to make sure it works ^^	

player = Player()

#Commands
game.set_keyboard_binding(spgl.KEY_UP, block.rotate_block)
game.set_keyboard_binding(spgl.KEY_LEFT, block.move_left)
game.set_keyboard_binding(spgl.KEY_RIGHT, block.move_right)
game.set_keyboard_binding(spgl.KEY_DOWN, player.move_down)
game.set_keyboard_binding(spgl.KEY_SPACE, player.instadrop)
game.set_keyboard_binding(spgl.KEY_ESCAPE, player.pause)
game.set_keyboard_binding(spgl.KEY_SHIFT_LEFT, player.hold)

while True:
	game.tick()
	time.sleep(0.1)