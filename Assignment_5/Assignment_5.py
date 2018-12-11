import time


up_bounds = 3200
low_bounds = 2000

if __name__ == '__main__':
	time_start = time.time()
	arr = []
	for num in range(low_bounds, up_bounds + 1):
		if num % 7 == 0 and num % 5 != 0:
			arr.append(num)
	
	print(arr)
	print("the time used is : " + str(time.time() - time_start))
