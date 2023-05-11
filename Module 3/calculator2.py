print( "Calculator" )

number1 = int( input( "Give the first number: " ) )
number2 = int( input( "Give the second number: " ) )

print( "(1) +\n(2) -\n(3) *\n(4) /\n" )
calculation = int( input( "Please select something (1-4): " ) )


if calculation == 1:
	print( "The result is: ", number1+number2 )
elif calculation == 2:
	print( "The result is: ", number1-number2 )
elif calculation == 3:
	print( "The result is: ", number1*number2 )
elif calculation == 4:
	print( "The result is: ", number1/number2 )
else:
	print( "Selection was not correct." )