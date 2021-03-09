#문서편집기 for Linux
#v1.0

#지우기
def clear():
	for i in range(1, 71):
		print('\n')

#새로 만들기
def new():
	clear()
	file = open('New_file.txt', 'w')
	while True:
		line = str(input())
		if line == 'new':
			new()
			break
		elif line == 'load':
			load()
			break
		elif line == 'quit':
			file.close()
			break
		else:
			file.write(line + '\n')

#불러오기
def load():
	clear()
	print('불러올 파일의 이름을 입력하세요.')
	file_name = str(input('Wordpad>'))
	try:
		file = open(file_name, 'r')
		line = file.readline()
		while line != '':
			print(line, end='')
			line = file.readline()
		file.close()
		file = open(file_name, 'a+')
		while True:
			line = str(input())
			if line == 'new':
				new()
				break
			elif line == 'load':
				load()
				break
			elif line == 'quit':
				file.close()
				break
			else:
				file.write(line + '\n')
			
	except:
		print('없는 파일입니다.')

#명령어로 불러오기
def file_load(com):
	file_name = com[5:]
	try:
		file = open(file_name, 'r')
		line = file.readline()
		while line != '':
			print(line, end='')
			line = file.readline()
		file.close()
		file = open(file_name, 'a+')
		while True:
			line = str(input())
			if line == 'new':
				new()
				break
			elif line == 'load':
				load()
				break
			elif line == 'quit':
				file.close()
				break
			else:
				file.write(line + '\n')
	except:
		print('잘못된 구문 또는 없는 파일입니다.')

#제목
def title():
	clear()
	print('===[문서편집기]===')
	print('문서편집기에 오신걸 환영합니다!')
	print('명령어')
	print('- new : 새로 만들기')
	print('- load : 불러오기')
	print('- quit : 나가기')

#메인
def main():
	title()
	while True:
		ans = input('Wordpad>')
		if ans == 'new':
			new()
		elif ans =='load':
			load()
		elif ans == 'quit':
			break