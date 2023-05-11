print( "(1) Read the notebook\n(2) Add note\n(3) Empty the notebook\n(4) Quit\n" )
select = int( input( "Please select one: " ) )
notebook = ""

while True:
	if select == 1:
		sourcefile = open( "notebook.txt", "r" )
		content = sourcefile.read()
		print( content )
		sourcefile.close()
	elif select == 2:
		note = input( "Write a new note: " )
		note += "\n"
		
		sourcefile = open( "notebook.txt", "a" )
		content = sourcefile.write( note )
		sourcefile.close()
	elif select == 3:
		sourcefile = open( "notebook.txt", "w" ).close()
		print( "Notes deleted." )
	elif select == 4:
		print( "Notebook shutting down, thank you." )
		break
		
	print( "(1) Read the notebook\n(2) Add note\n(3) Empty the notebook\n(4) Quit\n" )
	select = int( input( "Please select one: " ) )