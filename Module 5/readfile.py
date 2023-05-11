# -*- coding: cp1252 -*-

sourcefile = open( "facts.txt", "r" )
content = sourcefile.readlines()

print( "Following was read from the file: ")
for i in content:
	print( i )
	
sourcefile.close()