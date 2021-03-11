#calc.py for Android
#v1.0

result = 0

def clear():
	for i in range(1, 71):
		print('\n')

def divis(num1, num2):
	global result
	result = int(num1) / int(num2)
	print(int(result))

def multi(num1, num2):
	global result
	result = int(num1) * int(num2)
	print(int(result))

def minus(num1, num2):
	global result
	result = int(num1) - int(num2)
	print(int(result))

def plus(num1, num2):
	global result
	result = int(num1) + int(num2)
	print(int(result))

def comcalc(com):
	global result
	list = com.split(' ')
	num1 = list[1]
	num2 = list[3]
	type = list[2]
	try:
		if type == '+':
			plus(num1, num2)
		elif type == '-':
			minus(num1, num2)
		elif type == '*':
			multi(num1, num2)
		elif type == '/':
			divis(num1, num2)
	except:
		print('오류가 발생했습니다.')

def title():
	clear()
	print('===[계산기]===')
	print('계산식을 입력하세요. 중간에 띄어쓰기를 해야합니다.')
	print('나가려면 quit을 눌러주세요.')

def main():
	global result
	title()
	while True:
		ans = input('Calculator>')
		if ans == 'quit':
			break
		else:
			list = ans.split(' ')
			num1 = list[0]
			num2 = list[2]
			type = list[1]
			try:
				if type == '+':
					plus(num1, num2)
				elif type == '-':
					minus(num1, num2)
				elif type == '*':
					multi(num1, num2)
				elif type == '/':
					divis(num1, num2)
			except:
				print('오류가 발생했습니다.')