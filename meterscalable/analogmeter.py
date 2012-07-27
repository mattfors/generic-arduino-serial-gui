#!/path/to/python 
import serial
import io
import time
import pygame
import math

y = 0
dir = 1
running = 1
width = 800
height = 600
screen = pygame.display.set_mode((width, height))
bgcolor = 0, 0, 0


degree =0
black=0,0,0
darkblue=0,51,102
darkbrown=51,0,0
red=255,0,0
yellow=255,255,0
green=0,255,0
white=255,255,255
lightgrey=192,192,192
verylightgrey=224,224,224
grey=160,160,160
darkgrey=128,128,128

print "Program Start" 
#ser = serial.Serial('/dev/ttyACM0', 9600)

#print "Connected" 
#ser.flushInput()
#time.sleep(5)
degree4=0
degree3=0
degree2=0
degree=0

#def hello():
#	buffer = ''
#	done = 0
#	while(done == 0):
#		buffer = buffer + ser.read(1)
#		if '\n' in buffer:
#			done = 1
#    	return buffer



#ser.write('1')
index = 0






def needle(color, origin, angle, length, thickness):
	endpoint= ((length*math.cos((angle)*(3.14/180)))+origin[0], (length*math.sin((angle)*(3.14/180)))+origin[1] )
	corner0 = ((thickness*math.cos((angle+90)*(3.14/180)))+origin[0], (thickness*math.sin((angle+90)*(3.14/180)))+origin[1] )
	corner1 = ((thickness*math.cos((angle-90)*(3.14/180)))+origin[0], (thickness*math.sin((angle-90)*(3.14/180)))+origin[1] )
	pygame.draw.polygon(screen, color, (corner0, corner1, endpoint), 0)
	pygame.draw.circle(screen, (245,245,245), origin, thickness, 0)

def bezel(origin, radius):
	color=[255,255,255]
	for i in range(2,8):
		pygame.draw.circle(screen, color, origin, radius+i, 1)
		color[:] = [x - 20 for x in color]

def tickmark(origin, radius, length, color, width,angle):
	endpoint1 = endpoint(origin, angle, radius)
	endpoint2 = endpoint(origin, angle, radius-length)
	pygame.draw.line(screen, color, endpoint1, endpoint2, width)


def ticksat3(origin,radius, length, width, color,startangle,stopangle):
	for i in range(startangle,stopangle,3):
		tickmark(origin, radius, length, color, width,i)

def ticksat15(origin,radius, length, width, color,startangle,stopangle):
	for i in range(startangle,stopangle,15):
		tickmark(origin, radius, length, color, width,i)

def ticksat30(origin,radius, length, width, color,startangle,stopangle):
	for i in range(startangle,stopangle,30):
		tickmark(origin, radius, length, color, width,i)

def endpoint(origin, angle, length):
	point = ((length*math.cos((angle)*(3.14/180)))+origin[0], (length*math.sin((angle)*(3.14/180)))+origin[1] )
	return point

def meter(origin, angle, radius, needlelength, needlethickness, facecolor, needlecolor):
	pygame.draw.circle(screen, facecolor, origin, radius, 0)
	needle(needlecolor, origin, angle, needlelength, needlethickness)


def style1(origin, radius, degree):
	meter(origin, degree, radius, radius-5, 2, darkblue, yellow)
	bezel(origin, radius)
	ticksat3(origin,radius, 2, 2, grey,0,360)
	ticksat15(origin,radius, 5, 2, lightgrey,0,360)
	ticksat30(origin,radius, 8, 2, verylightgrey,0,360)


def style2(origin, radius, degree):
	meter(origin, degree, radius, radius-5, 2, darkbrown, red)
	bezel(origin, radius)
	ticksat3(origin,radius, 2, 2, grey,0,360)
	ticksat15(origin,radius, 5, 2, lightgrey,0,360)
	ticksat30(origin,radius, 8, 2, verylightgrey,0,360)

def style3(origin, radius, degree):
	meter(origin, degree, radius, radius-5, 4, white, green)
	ticksat15(origin,radius, 5, 2, black ,0,360)
	ticksat30(origin,radius, 8, 2, black,0,360)
	pygame.draw.circle(screen, black, origin, radius, 1)
	
while running:
	event = pygame.event.poll()
	if event.type == pygame.QUIT:
		running = 0

	screen.fill(bgcolor)


	origin=(150,150)
	degree = 40
	radius=100
	style1(origin, radius, degree)
	style1((75,75), 40, 75)
	style2((425,175), 150, 64)
	style3((375,125), 30, 190)

	pygame.display.flip()

	



#ser.close()
