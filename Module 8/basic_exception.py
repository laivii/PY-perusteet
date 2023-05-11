value = input( "Give a number: " )

try:
	value = int( value )
	print( "The input was suitable!" )
except Exception:
	print( "The input was malformed." )