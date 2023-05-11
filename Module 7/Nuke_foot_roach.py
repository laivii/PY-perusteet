import random

def randomhand():
	num = random.randint(1,3)
	computer = ""

	if num == 1:
		computer = "Foot"
	elif num == 2:
		computer = "Nuke"
	else:
		computer = "Cockroach"
	
	return computer

player = input( "Foot, Nuke or Cockroach? (Quit ends): " )
games = 0
won = 0
tie = 0

while True:
	computer = randomhand()
	
	if player == "Quit":
		print( "You played ", games, "rounds, and won ", won, "rounds, playing tie in ", tie, " rounds." )
		break
	
	if player != "Nuke" and player != "Foot" and player != "Cockroach" and player != "Quit":
		print( "Incorrect selection." )
		player = input( "Foot, Nuke or Cockroach? (Quit ends): " )
		continue
	
	print( "You chose: ", player )
	print( "Computer chose: ", computer )
	
	if computer == "Nuke":
		if player =="Foot":
			print( "You LOSE!" )
		elif player == "Nuke":
			print( "Both LOSE!")
			tie += 1
		else:
			print( "You WIN!")
			won += 1
			
	if computer == "Foot":
		if player == "Foot":
			print( "It is a tie!" )
			tie += 1
		elif player == "Cockroach":
			print( "You LOSE!")
		else:
			print( "You WIN!")
			won += 1
		
	if computer == "Cockroach":
		if player == "Cockroach":
			print( "It is a tie!" )
			tie += 1
		elif player == "Nuke":
			print( "You LOSE!" )
		else:
			print( "You WIN!" )
			won += 1
			
	games += 1
	player = input( "Foot, Nuke or Cockroach? (Quit ends): " )