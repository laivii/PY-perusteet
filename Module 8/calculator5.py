import math

def getnumber():
    while True:
        number = input( "Give a number: " )
        try:
            number = int( number )
            return number
        except Exception:
            print( "This input is invalid." )

print( "Calculator" )

num1 = getnumber()
num2 = getnumber()

print( "(1) +\n(2) -\n(3) *\n(4) /\n(5)sin(number1/number2)\n(6)cos(number1/number2)\n(7)Change numbers\n(8)Quit" )
print( "Current numbers: ", num1, num2 )

selection = int( input( "Please select something (1-6): " ) )

while selection > 0 and selection < 8:
	if selection == 1:
		print( "The result is: ", num1+num2 )
	elif selection == 2:
		print( "The result is: ", num1-num2 )
	elif selection == 3:
		print( "The result is: ", num1*num2 )
	elif selection == 4:
		print( "The result is: ", num1/num2 )
	elif selection == 5:
		print( "The result is: ", math.sin( num1/num2 ) )
	elif selection == 6:
		print( "The result is: ", math.cos( num1/num2 ) )
	elif selection == 7:
		num1 = getnumber()
		num2 = getnumber()
	elif selection == 8:
		break
	print( "(1) +\n(2) -\n(3) *\n(4) /\n(5)sin(number1/number2)\n(6)cos(number1/number2)\n(7)Change numbers\n(8)Quit" )
	print( "Current numbers: ", num1, num2 )
	selection = int( input( "Please select something (1-6): " ) )
	
print( "Thank you!" )