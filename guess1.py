import random

r = random.randint(1, 20)
print(r)
times = 0
while True:
	number = input('請輸入數字: ')
	number = int(number)
	if r == number:
		print ('Bingo!')
		times = times + 1
		print('妳總共猜了', times, '次')
		if times >= 5:
			print('Too bad')
		else:
			print('Good')
		break
	elif number > r:
		print('Too large!')
		times = times + 1

	else:
		print('Too small!')
		times = times + 1

