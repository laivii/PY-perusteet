number1 = int( input( "Give a number: " ) )
number2 = int( input( "Give another number: " ) )

if number1%2 == 0 and number2%2 == 0:
	print( "Both numbers are even." )
elif number1%2 == 0 and number2%2 != 0 or number1%2 != 0 and number2%2 == 0:
	print( "One of the numbers is even." )
else:
	print( "Both numbers are odd." )