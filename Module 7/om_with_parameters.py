# -*- coding: cp1252 -*-

import inspector

def testme( password ):
    chars = False
    nums = False
    result = False
    
    for i in password:
        if i.isdigit() == True:
            nums = True
        else:
            chars = True
    
    if len( password ) <= 5:
        result = False
    
    if chars == True and nums == False or chars == False and nums == True:
        result = False
    
    if len( password ) > 5 and chars == True and nums == True:
        result = True
        
    return result

def main():
	userinput = input( "Give a string for testing: " )
	tulos = inspector.testme( userinput )
	while True:
		if tulos == True:
			print( "This string fits for a password!" )
			break
		else:
			print( "The module says no." )
			userinput = input( "Give a string for testing: " )
			tulos = inspector.testme( userinput )
			
if __name__ == "__main__":
	main()