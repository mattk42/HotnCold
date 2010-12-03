#!/usr/bin/python
from socket import *
from sys import *
import struct
import random
import select
import objects

GRID_SIZE = 20

class user():
	def __init__(self):
		self.posx = 0
		self.posy = 0
		self.health = 100
		self.heat = 127
	def setName(self,nname):
		self.name = nname
	def setPos(self,x,y):
		self.posx = x
		self.posy = y
	def move(self,x,y):
		self.posx += x
		self.posy += y

class server():

	def __init__(self):
		#set up the recieving socket on specified port	
		self.objects = []
		self.users = {}
		#for i in range(200):
		#	self.objects.append(objects.Fish(random.randint(00,255),random.randint(0,24),random.randint(0,24)))
			
		#self.objects.append(objects.Bomb(255,10,10))
		#self.objects.append(objects.Bomb(0,10,10))
		#self.objects.append(objects.Fish(127,0,0))
		port = int(argv[1])
		host = ""
		self.rcv_sock = socket(AF_INET,SOCK_DGRAM)
		self.rcv_sock.bind((host,port))
		self.mypoll = select.poll()
		self.mypoll.register(self.rcv_sock.fileno(),select.POLLIN)

		#separate socket for sending data (why?) - self.x[i][j]
		self.snd_sock = socket(AF_INET,SOCK_DGRAM)
#		#set up the port		
#		port = int(argv[1])
#		host = "localhost"
#		self.sock = socket(AF_INET,SOCKif data[0] == 'k':
#				for i in range(10):
#					self.x[random.randint(0,24)][random.randint(0,24)] = random.randint(127,255)_DGRAM)
#		self.sock.bind((host,port))
		
		#initialize client table and map		
		self.clients = set([])
		self.x = [[ random.randint(0,255) for i in range(GRID_SIZE)] for x in range(GRID_SIZE)]#random.randint(0,255)
		for i in range(len(self.x)):
			for j in range(len(self.x[0])):
				self.x[i][j] = i*(255/GRID_SIZE) +j%(GRID_SIZE/2)
		for i in range(10):
			self.x[random.randint(0,GRID_SIZE-1)][random.randint(0,GRID_SIZE-1)] = random.randint(0,255)
		self.xtwo = self.x
		print "Server listening on ", port
	
	#method to generate the map	
	def asstring(self):
		self.xstr = ''
		for j in self.x:
			for i in j:
				if(i<=255):
					self.xstr += chr(i)
				else:
					self.xstr += chr(0)
					print "ERROR I: ",i
		return self.xstr + (" " * GRID_SIZE**2)
	
	def update(self):
		self.xstr = ''
		
		for i in range(GRID_SIZE):
			for j in range(GRID_SIZE):
				sumdiff = 0
				numdiff = 0
				if i != 0:
					numdiff += 1
					sumdiff += self.x[i-1][j] - self.x[i][j]
					if j != 0:
						numdiff += 1
						sumdiff += self.x[i-1][j-1] - self.x[i][j]
					if j != GRID_SIZE-1:
						numdiff += 1
						sumdiff += self.x[i-1][j+1] - self.x[i][j]

				if i != GRID_SIZE-1:
					numdiff += 1
					sumdiff += self.x[i+1][j] - self.x[i][j]
					if j != 0:
						numdiff += 1
						sumdiff += self.x[i+1][j-1] - self.x[i][j]
					if j != GRID_SIZE-1:
						numdiff += 1
						sumdiff += self.x[i+1][j+1] - self.x[i][j]

				if j != 0:
					numdiff += 1
					sumdiff += self.x[i][j-1] - self.x[i][j]
				if j != GRID_SIZE-1:
					numdiff += 1
					sumdiff += self.x[i][j+1] - self.x[i][j]

				
				diff = float(sumdiff) / float(numdiff)
				if diff > 5:
					diff = 5
				if diff < -5:
					diff = -5
				self.xtwo[i][j] = int(min(self.x[i][j] + round(diff),255))
		self.x = self.xtwo
		for user in self.users:
			print self.users[user].name
			self.x[self.users[user].posx][self.users[user].posy]=self.users[user].heat
	
	def listen(self):
		while(1):
			buf = GRID_SIZE**2*2

			#Add client to client table when message recieved

			if len(self.mypoll.poll(50)) != 0:		
				data,addr = self.rcv_sock.recvfrom(buf,0)
				print(data)	
				# create user for all new connections.
				if addr not in self.users:
					print "NEW USER ", addr				
					self.users[addr] = user()
					self.users[addr].setName(addr)
					self.users[addr].setPos(0,0)

				#self.clients.add(addr)
				if data[0] == 'k':
					for i in range(1):
						a = random.randint(0,GRID_SIZE-1)
						b = random.randint(0,GRID_SIZE-1)
						self.x[a][b] =255# max(random.randint(self.x[a][b],255),random.randint(200,255))
				if data[0] == 'j':
					for i in range(1):
						a = random.randint(0,GRID_SIZE-1)
						b = random.randint(0,GRID_SIZE-1)
						self.x[a][b] =0 #min(random.randint(0,self.x[a][b]),random.randint(0,55))
				if data[0] == 'd':
					if self.users[addr].posx < GRID_SIZE-1:
						self.users[addr].move(1,0)
				if data[0] == 'a':
					if self.users[addr].posx > 0:
						self.users[addr].move(-1,0)
				if data[0] == 'w':
					if self.users[addr].posy > 0:
						self.users[addr].move(0,-1)
				if data[0] == 's':
					if self.users[addr].posy < GRID_SIZE-1:
						self.users[addr].move(0,1)
				if data[0] == 'u':
					if self.users[addr].heat < 247:
						self.users[addr].heat += 8
				if data[0] == 'i':
					if self.users[addr].heat > 8:
						self.users[addr].heat -= 8
				#if data[0] == 'r':
				#	self.users[addr].ready = True

				print self.users[addr].name, " : ", self.users[addr].posx, "," , self.users[addr].posy

				#print addr
	
				#print data
	
				self.clients.add(addr)
				#print "We have " + str(len(self.clients)) + " clients connected"	
			
			#send map to all of the cients
			self.objects = [x for x in self.objects if x.Affect(self) != 0]
			self.update();

			self.xstr = self.asstring()
			for client in self.clients:
				#if self.users[client].ready:
				self.snd_sock.sendto(self.xstr,client)
				#self.users[client].ready = False
				

#	def listen(self):
#		while(1):
#			buf = 1250

#			#Add client to client table when message recieved			
#			data,addr = self.sock.recvfrom(buf,0)
#			self.clients.add(addr)
#	
#			print data
#	
#			print "We have " + str(len(self.clients)) + " clients connected"	
#			
#			#send map to all of the cients
#			self.update();
#			for client in self.clients:
#				self.sock.sendto(self.xstr,client)
							
j = [str(x)[0] for x in range(GRID_SIZE**2*2)]
x= ''
for i in j:
	x += i	

#start the server
serv = server()
serv.listen()
