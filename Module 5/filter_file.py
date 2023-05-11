sourcefile = open( "strings.txt","r" )
content = sourcefile.readlines()

for i in range( len( content ) ):
	string = content[i]
	string = string.replace( "\n", "" )
	
	if string.isalnum() == True:
		print( string, "was ok." )
	else:
		print( string, "was invalid." )


sourcefile.close()