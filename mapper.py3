def fahrenheit(T):
	return (9.0/5)*T+32

print(fahrenheit(100))

temp = [0,22.5,40,100]
l = []
l = list(map(fahrenheit,temp))
for i in l:
	print(str(i))

map(lambda T: (9.0/5)*T+32,temp)

a = [1,2,3]
b = [4,5,6]
c = [7,8,9]

l = map(lambda x,y,z: x+y+z,a,b,c)
for i in l:
	print(str(i))

l = map(lambda num: num*-1,a)

for i in l:
	print(str(i))
	