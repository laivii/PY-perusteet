import time
import pickle

try:
	sourcefile = open( "notebook.dat", "r" )
except IOError:
	sourcefile = open( "notebook.dat", "w+" ).close()
	print( "No default notebook was found, created one." )

notebook = []

print( "(1) Read the notebook\n(2) Add note\n(3) Edit a note\n(4) Delete a note\n(5) Save and quit\n" )
select = int( input( "Please select one: " ) )

while True:
	if select == 1:
		if len( notebook ) == 0:
			continue
		for i in range( len( notebook ) ):
			print( notebook[ i ] )
	elif select == 2:
		note = input( "Write a new note: " )
		note += ":::" + time.strftime("%X %x")
		notebook.append( note )
		
	elif select == 3:
		print( "The list has", len( notebook ), "notes." )
		edited = int( input( "Which of them will be changed? " ) )
		note = notebook[ edited ]
		print( note )
		new_note = input( "Give the new note: " )
		new_note += ":::" + time.strftime("%X %x")
		notebook[ edited ] = new_note
		
	elif select == 4:
		print( "The list has", len( notebook ), "notes." )
		deleted = int( input( "Which of them will be deleted? " ) )
		print( "Deleted note", notebook[ deleted ] )
		notebook.pop( deleted )
		
	elif select == 5:
		filename = open( "notebook.dat", "wb" )
		pickle.dump( notebook, "notebook.dat" )
		filename.close()
		print( "Notebook shutting down, thank you." )
		break
	print( "(1) Read the notebook\n(2) Add note\n(3) Edit a note\n(4) Delete a note\n(5) Save and quit\n" )
	select = int( input( "Please select one: " ) )