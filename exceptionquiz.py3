def GetANumber():
	num = -1
	while True:
		try:
			num = int(input('Enter an integer: '))
		except:
			print ('That is not a valid Integer')
			continue
		else:
			print (str(num) + ' is indeed an integer.')
			break
		finally:
			print('Finally')

def ForEx():
	try:
		for i in ['a','b','c']:
			print (i**2)
	except:
		print ('An error has occurred.')


GetANumber()
ForEx()