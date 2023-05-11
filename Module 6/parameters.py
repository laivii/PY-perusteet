def main():
	number = int( input( "Give a number: " ) )
	print( "The result is ", poweroftwo( number ) )

def poweroftwo( num ):
	result = 2
	for i in range( num-1 ):
		result = result*2
	
	return result

if __name__ == "__main__":
	main()