sourcefile = open( "words.txt", "r" )
content = sourcefile.readlines()

content.sort()

print( "Words in an alphabetical order: " )
for i in range( len( content ) ):
	value = content[i]
	value = value.replace( "\n", "" )
	print( value )


sourcefile.close()