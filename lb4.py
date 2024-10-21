import random
import numpy as np


#Метод 1: использование random.randint()
def met1(n):
	rand_list=[]
	for i in range(n):
		rand_list.append(random.randint(3,9))
	return rand_list
print(met1(20))

#Метод 2: использование random.sample()
def met2():
	res = random.sample(range(1, 50), 7)
	return "Random number list is : " + str(res)
print(met2())

#Способ 3: использование понимания списков + randrange()
def met3():
	# using list comprehension + randrange()
	# to generate random number list
	res = [random.randrange(1, 50, 1) for i in range(7)]

	# printing result
	return "Random number list is : " + str(res)
print(met3())

#Метод 4: использование цикла + randint()
def met4(n):
	# Method 3: For Loop Random Int List [0, 51]
	lis = []
	for _ in range(n):
		lis.append(random.randint(0, 51))
	return lis
print(met4(10))

#Способ 1: Создание списка случайных целых чисел с помощью функции numpy.random.randint
def met5():
	# importing numpy module
	# print the list of 10 integers from 3 to 7
	return list(np.random.randint(low = 3, high = 8, size = 10))

	# print the list of 5 integers from 0 to 2
	# if high parameter is not passed during
	# function call then results are from [0, low)
	return list(np.random.randint(low = 3, size = 5))
print(met5())

#Способ 2. Создание списка случайных чисел с плавающей точкой с помощью функции numpy.random.random_sample
def met6():

	# generates list of 4 float values
	return np.random.random_sample(size = 4)

	# generates 2d list of 4*4
	return np.random.random_sample(size = (4, 4))
print(met6())


