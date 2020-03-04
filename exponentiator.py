def exponentiate(a,b):
	'''
	a,b numbers
	returns a**b
	'''
	return a**b

def raise_to_fourth_power(x):
	'''ddjd
	x integer
	Runs exponentiate with b = 2
	'''
	return exponentiate(x,4)

print(raise_to_fourth_power(2))

square = lambda y : exponentiate(y,2)
print(square(2))

cube = lambda z : exponentiate(z,3)
print(cube(2))

print('The print statments can be placed in the following order\n to get the output you desired.')

print(square(2))
print(cube(2))
print(raise_to_fourth_power(2))