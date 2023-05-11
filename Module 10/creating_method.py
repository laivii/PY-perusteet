class Player:
	def __init__( self, teamcolor, points ):
		self.teamcolor = teamcolor
		self.points = points
	
	def tellscore( self ):
		print( "I am", self.teamcolor, ", we have", self.points, "points!" )
		
	def goal( self ):
		self.points += 1
		
p1 = Player("Blue", 0)

p1.goal()
p1.tellscore()