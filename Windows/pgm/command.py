#command.py for Android

try:
	import cpuinfo, platform, psutil, os, shutil
	import random, time, socket
except:
	with open('errorlog.txt', 'w') as errorlog:
		errorlog.write('오류가 발생했습니다.\n')
		errorlog.write('에러코드 : 001C\n')
		errorlog.write('에러코드 읽는 방법을 참조해 주세요.\n')

path = '/storage/emulated/0/OS_Android/sys'

#지우기
def clear():
	for i in range(1, 71):
		print('\n')
		
#도움말
def help():
	global path
	help_path = path + '/help.txt'
	with open(help_path, 'r') as help:
		line = help.readline()
		while line != '':
			print(line, end='')
			line = help.readline()

#정보
def info():
	print('BINGO For Android')
	print('리눅스 정보 :', platform.platform())
	print('v0.2')

#하드웨어정보
def hwinfo():
	arch = platform.machine()
	ram_mb = round(psutil.virtual_memory().total / 1024)
	print('아키텍처 :', arch)
	print('RAM 크기 :', round(ram_mb / 1024), 'MB')

#디렉터리 이동
def cd(dir):
	try:
		path = dir.split(' ')
		os.chdir(path[1])
	except:
		print('잘못된 구문입니다.')

#디렉터리 삭제
def rmdir(direc):
	if '-f' in direc:
		dir = direc[9:]
		shutil.rmtree(dir)
	else:
		try:
			dir = direc[6:]
			os.rmdir(dir)
		except:
			print('없는 디렉터리 이거나 디렉터리 내 파일이 있습니다. -f 옵션을 추가해 시도해보세요.')

#디렉터리 생성
def mkdir(direc):
	dir = direc.split(' ')
	try:
		os.makedirs(dir[1])
	except:
		print('잘못된 구문입니다.')

#종료
def shutdown():
	print('운영체제 종료중...')
	time.sleep(random.randrange(3, 6))
	quit()

#파일이름 변경
def rename(dir):
	try:
		com = dir.split(' ')
		before = com[1]
		after = com[2]
		os.rename(before, after)
	except:
		print('잘못된 구문 또는 없는 파일입니다.')

#파일 삭제
def rmfile(direc):
	try:
		file = direc.split(' ')
		os.remove(file[1])
	except:
		print('잘못된 구문 또는 없는 파일입니다.')

#나랏말싸미
def easter():
	global path
	easter_path = path + '/Naratmalsami.txt'
	with open(easter_path, 'r') as easter:
		line = easter.readline()
		while line != '':
			print(line)
			line = easter.readline()

#파일리스트
def filelist():
	print(os.listdir())

#캐쉬 삭제
def delcache():
	rmdir('rmdir -f /storage/emulated/0/OS_Android/__pycache__')
	rmdir('rmdir -f /storage/emulated/0/OS_Android/pgm/__pycache__')

#그거 그냥 출력해(Just Print It Out)
def jpio(com):
	try:
		cmd = com.split(' ')
		file_name = cmd[1]
		file = open(file_name, 'r')
		line = file.readline()
		while line != '':
			print(line, end='')
			line = file.readline()
		file.close()
	except:
		print('잘못된 구문 또는 없는 파일입니다.')