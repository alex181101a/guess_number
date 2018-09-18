import random

r = random.randint(1, 20)
print(r)
times = 5
while times <= 5:
	number = input('請輸入數字: ')
	number = int(number)
	if r == number:
		print ('Bingo!')
		break
	elif number > r:
		print('Too large!')
		times = times - 1
		print('you have', times, 'left')
		if times == 0:
			print('no chance!')
			break
	else:
		print('Too small!')
		times = times - 1
		print('you have', times, 'left')
		if times == 0:
			print('no chance!')
			break
