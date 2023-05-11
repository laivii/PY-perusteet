class Player:
	"""Player-class: stores data on team colors and points."""
		
	def __init__( self, teamcolor):
		self.teamcolor = teamcolor
		self.points = 0
	
	def tellscore( self ):
		print( "I am", self.teamcolor, ", we have", self.points, "points!" )
		
	def goal( self ):
		self.points += 1
		
color1 = input( "What color do I get?: " )
player1 = Player( color1 )

color2 = input( "What color do I get?: " )
player2 = Player( color2 )

for i in range(2):
	player1.goal()
	
player2.goal()

player1.tellscore()
player2.tellscore()