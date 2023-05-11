print( "Calculator" )

num1 = int( input( "Give the first number: " ) )
num2 = int( input( "Give the second number: " ) )

print( "(1) +\n(2) -\n(3) *\n(4) /\n(5)Change numbers\n(6)Quit" )
print( "Current numbers: ", num1, num2 )

selection = int( input( "Please select something (1-6): " ) )

while selection > 0 and selection < 6:
	if selection == 1:
		print( "The result is: ", num1+num2 )
	elif selection == 2:
		print( "The result is: ", num1-num2 )
	elif selection == 3:
		print( "The result is: ", num1*num2 )
	elif selection == 4:
		print( "The result is: ", num1/num2 )
	elif selection == 5:
		num1 = int( input( "Give the first number: " ) )
		num2 = int( input( "Give the second number: " ) )
	elif selection == 6:
		break
	print( "(1) +\n(2) -\n(3) *\n(4) /\n(5)Change numbers\n(6)Quit" )
	print( "Current numbers: ", num1, num2 )
	selection = int( input( "Please select something (1-6): " ) )
	
print( "Thank you!" )