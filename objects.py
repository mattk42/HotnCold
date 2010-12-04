import random
class Tower:
	def __init__(self,ishot,thex,they):
		self.x = thex
		self.y = they
		
		if ishot > 0:
			self.temp = 255
		else:
			self.temp = 0
			
	def Affect(self,myserver):
		myserver.x[self.x][self.y] = self.temp
		return self
		
class Fish:
	def __init__(self,tempa,thex,they):
		self.x = thex
		self.y = they
		self.health = 10
		self.temp = tempa
			
	def Affect(self,myserver):
		self.x = min(max(0,self.x + random.randint(-1,1)),20)
		self.y = min(max(0,self.y + random.randint(-1,1)),20)
		if (self.temp > 127 and myserver.x[self.x][self.y] < 127):
			self.health -= 1
		if (self.temp < 127 and myserver.x[self.x][self.y] > 127):
			self.health -= 1
			
		if self.health < 1:
			return 0
		
		if(self.temp < 127 and myserver.x[self.x][self.y] > self.temp):
			myserver.x[self.x][self.y] = self.temp
		elif(self.temp > 127 and myserver.x[self.x][self.y] < self.temp):
			myserver.x[self.x][self.y] = self.temp
		elif self.temp == 127:
			myserver.x[self.x][self.y] = 127
		return self
		
class Bomb:
	def __init__(self,tempa,thex,they):
	
		self.temp = tempa
		self.x = thex
		self.y = they
		self.health = 1000
		self.temp = tempa
		
	def Affect(self,myserver):
		if self.health > 0:
			self.x = min(max(0,self.x + random.randint(-1,1)),20)
			self.y = min(max(0,self.y + random.randint(-1,1)),20)
			diff = abs(myserver.x[self.x][self.y] - 127)
			myserver.x[self.x][self.y] = 127
			if diff > 5:
				self.health -= diff - 5
		if self.health <= 0:
			for i in range(10):
				self.x = random.randint(0,20)
				self.y = random.randint(0,20)
				myserver.x[self.x][self.y] = self.temp
			self.health = 1000
			
		if self.health < -10000:
				return 0
		#print self.health
		
		return self
