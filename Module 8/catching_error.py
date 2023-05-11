filename = input( "Give the file name: " )

try:
	sourcefile = open( filename, "r" )
	content = sourcefile.read()
	content = int( content )
	result = 1000 / content
	print( "The result was", result )
except IOError:
	print( "There seems to be no file with that name." )
except Exception:
	print( "The file contents were unsuitable." )