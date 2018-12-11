def sum(m, n, f):
	accum = 0
	for i in range(m, n + 1):
		accum = accum + f(i)
	return accum


def id(x):
	return x


def cube(x):
	return x ** 3


print sum(1, 100, id)
print sum(1, 5, cube)
