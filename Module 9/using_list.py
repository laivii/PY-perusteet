list1 = []

select = int( input( "Would you like to\n(1)Add or\n(2)Remove items or\n(3)Quit?: " ) )

while True:
	if select == 1:
		added = input( "What will be added?: " )
		list1.append( added )
	elif select == 2:
		print( "There are", len( list1 ), "items in the list." )
		removed = int( input( "Which item is deleted?: " ) )
		if removed >= len( list1 ):
			print( "Incorrect selection." )
		else:
			list1.pop( removed )
	elif select == 3:
		print( "The following items remain in the list:" )
		
		for i in list1:
			print( i )
			
		break
	else:
		print( "Incorrect selection." )
		
	select = int( input( "Would you like to\n(1)Add or\n(2)Remove items or\n(3)Quit?: " ) )