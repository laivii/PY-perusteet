def main():
	text = input( "Write something (quit ends): " )
	print( tester( text ) )
	
	while True:
		text = input( "Write something (quit ends): " )
		
		if text == "quit":
			break
		
		print( tester( text ) )

def tester( str ):
	givenstring = "Too short"
	
	if len( str ) > 10:
		givenstring = str
		
	if "X" in str:
		givenstring += "\nX spotted!"
		
	return givenstring

if __name__ == "__main__":
	main()