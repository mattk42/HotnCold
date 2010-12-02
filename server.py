#!/usr/bin/python
from socket import *
from sys import *
import struct
import random


class server():

	def __init__(self):
		#set up the recieving socket on specified port		
		port = int(argv[1])
		host = ""
		self.rcv_sock = socket(AF_INET,SOCK_DGRAM)
		self.rcv_sock.bind((host,port))

		#separate socket for sending data (why?)
		self.snd_sock = socket(AF_INET,SOCK_DGRAM)
#		#set up the port		
#		port = int(argv[1])
#		host = "localhost"
#		self.sock = socket(AF_INET,SOCK_DGRAM)
#		self.sock.bind((host,port))
		
		#initialize client table and map		
		self.clients = set([])
		self.x = [[ random.randint(0,255) for i in range(50)] for x in range(25)]#random.randint(0,255)
		self.x[8][12] = 200
		self.x[20][16] = 230
		self.xtwo = self.x
		print "Server listening on ", port
	
	#method to generate the map	
	def asstring(self):
		self.xstr = ''
		for j in self.x:
			for i in j:
				self.xstr += chr(i)
		return self.xstr
	
	def update(self):
		self.xstr = ''
		
		for i in range(25):

			for j in range(50):
				DIV_EQUAL = 1
				temp = self.x[i][j]
				todiv = 1
				if i != 0:
					temp += self.x[i-1][j]
					todiv += 1
					if j != 0:
						temp += self.x[i-1][j-1]
						todiv += 1
					if j != 49:
						temp += self.x[i-1][j+1]
						todiv += 1
				if i != 24:
					temp += self.x[i+1][j]
					todiv += 1
					if j != 0:
						temp += self.x[i+1][j-1]
						todiv += 1
					if j != 49:
						temp += self.x[i+1][j+1]
						todiv += 1
				if j != 0:
					temp += self.x[i][j-1]
					todiv += 1
				if j != 49:
					temp += self.x[i][j+1]
					todiv += 1
				temp /= todiv
				temp = temp * .3 + self.x[i][j] * .7
				self.xtwo[i][j] = int(temp)
		print self.xtwo[8][8]
		self.x = self.xtwo
		self.xstr = self.asstring()
	
	def listen(self):
		while(1):
			buf = 1250

			#Add client to client table when message recieved			
			data,addr = self.rcv_sock.recvfrom(buf,0)
			#self.clients.add(addr)


			print addr
	
			print data
	
			self.clients.add(addr)
			print "We have " + str(len(self.clients)) + " clients connected"	
			
			#send map to all of the cients
			self.update();
			for client in self.clients:
				self.snd_sock.sendto(self.xstr,client)

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
							
j = [str(x)[0] for x in range(1250)]
x= ''
for i in j:
	x += i	

#start the server
serv = server()
serv.listen()
