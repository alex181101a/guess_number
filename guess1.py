import random
min = input('請輸入最小範圍')   #input 為字串
max = input('請輸入最大範圍')
r = random.randint(int(min), int(max))   #字串轉整數
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
	print('這是第', times, '次')

