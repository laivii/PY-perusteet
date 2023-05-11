import time

def checkFile( filename ):
    try:
        sourcefile = open( filename, "r")
        sourcefile.close()
    except Exception:
        sourcefile = open( filename, "w+" ).close()
        print( "No default notebook was found, created one." )

filename = "notebook.txt"
checkFile( filename )

print( "Now using file " + filename )
print( "(1) Read the notebook\n(2) Add note\n(3) Empty the notebook\n(4) Change the notebook\n(5) Quit\n" )
select = int( input( "Please select one: " ) )

while True:
	if select == 1:
		sourcefile = open( filename, "r" )
		content = sourcefile.readlines()
		
		for i in content:
			print( i )
		
		sourcefile.close()
	elif select == 2:
		note = input( "Write a new note: " )
		note += ":::" + time.strftime("%X %x") + "\n"
		
		sourcefile = open( filename, "w" )
		content = sourcefile.write( note )
		sourcefile.close()
	elif select == 3:
		sourcefile = open( filename, "w" ).close()
	elif select == 4:
		filename = input( "Give the name of the new file: " )
		try:
			sourcefile = open( filename, "r" )
		except IOError:
			sourcefile = open( filename, "w+" ).close()
			print( "No notebook with that name detected, created one." )
			
	elif select == 5:
		print( "Notebook shutting down, thank you." )
		break
	print( "Now using file " + filename )
	print( "(1) Read the notebook\n(2) Add note\n(3) Empty the notebook\n(4) Change the notebook\n(5) Quit\n" )
	select = int( input( "Please select one: " ) )