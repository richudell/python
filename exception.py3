def askint():
	while True:
		try:
			val = int(input('Please enter an integer: '))
		except:
			print('Looks like you did not enter an integer')
			continue
		else: 
			print ('Correct that is an integer')
			break
		finally:
			print('Finally block executed!')

askint()