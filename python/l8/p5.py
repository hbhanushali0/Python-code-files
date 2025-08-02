# multiple inheritance

class pcm:
	def __init__(self, phy, chem, math):
		self.phy = phy
		self.chem = chem
		self.math = math

	def show(self):
		print("phy = ", self.phy)
		print("chem = ", self.chem)
		print("math = ", self.math)

class nonpcm:
	def __init__(self, eng, bio):
		self.eng = eng
		self.bio = bio
	
	def show(self):
		print("eng = ", self.eng)
		print("bio = ", self.bio)

class marks(pcm, nonpcm):
		def __init__(self, phy, chem, math, eng, bio):
			pcm.__init__(self, phy, chem, math)
			nonpcm.__init__(self, eng, bio)

		def show(self):
			pcm.show(self)
			nonpcm.show(self)

M = marks(99, 88, 77, 48, 99)
M.show()

				
