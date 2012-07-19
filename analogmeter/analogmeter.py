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
height = 500
screen = pygame.display.set_mode((width, height))
linecolor = 255,100,100
bgcolor = 0, 0, 0
degree =0


print "Program Start" 
ser = serial.Serial('/dev/ttyACM0', 9600)

print "Connected" 
ser.flushInput()
time.sleep(5)
degree4=0
degree3=0
degree2=0
degree=0

def hello():
	buffer = ''
	done = 0
	while(done == 0):
		buffer = buffer + ser.read(1)
		if '\n' in buffer:
			done = 1
    	return buffer



ser.write('1')
index = 0
while running:
	event = pygame.event.poll()
	if event.type == pygame.QUIT:
		running = 0

	screen.fill(bgcolor)

	
	test = hello()
	degree4 = degree3
	degree3 = degree2
	degree2 = degree	
	degree = int(test)

	degree= (degree+degree2+degree3+degree4)/4
	print degree
	pygame.draw.line(screen, linecolor, ((width/2)-5, height-1), ((350*math.cos(degree*-1*(3.14/180)))+(width/2),height-1-350*math.sin(degree*(3.14/180))))
	pygame.draw.line(screen, linecolor, ((width/2)+5, height-1), ((350*math.cos(degree*-1*(3.14/180)))+(width/2),height-1-350*math.sin(degree*(3.14/180))))



	pygame.draw.circle(screen, (30,144,255), ((width/2), height-1), 375, 5)
	
	for angle in [0,15,30,45,60,75,90,105,120,135,150,165,180]:
		pygame.draw.line(screen, (240,255,255), ((360*math.cos(angle*-1*(3.14/180)))+(width/2),height-1-360*math.sin(angle*(3.14/180))), ((375*math.cos(angle*-1*(3.14/180)))+(width/2),height-1-375*math.sin(angle*(3.14/180))))	


	pygame.display.flip()








ser.close()
