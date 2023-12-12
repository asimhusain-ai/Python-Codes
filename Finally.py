def divide(x, y): 
	try: 
		result = x // y 
	except ZeroDivisionError: 
		print("Sorry ! You are dividing by zero ") 
	finally: 
		print('This is always executed') 

divide(3, 2) 

