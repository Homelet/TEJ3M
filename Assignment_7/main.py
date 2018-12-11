import random


def bubble_sort(ls):
	# to start the algorithm, we start a loop
	while True:
		# the swapped counter is reset in every loop,
		# if we didn't change anything in current loop
		# we break, because we are done sorting
		swapped = 0
		# the index is used for the current place in the loop
		index = 1
		while index < ls.__len__():
			# if the indexed value is smaller than the previous value, then swap them
			if ls[index] < ls[index - 1]:
				ls[index], ls[index - 1] = ls[index - 1], ls[index]
				# accumulate the swapped counter
				swapped += 1
			index += 1
		# if no swapped occurs then break
		if swapped == 0:
			break


def gen_random_nums(size, lower=0, upper=100):
	return [random.randint(lower, upper) for _ in range(size)]


ls = gen_random_nums(100)

bubble_sort(ls)

print(ls)
