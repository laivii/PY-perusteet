# -*- coding: cp1252 -*-

filename = input( "Give a file name: " )
text = str( input( "Write something: " ) )

writefile = open(filename, "w")
writefile.write(text)
writefile.close()

readfile = open(filename, "r")
content = readfile.read()  # change readline() to read()
readfile.close()

print( "Wrote", content, "to the file", filename )