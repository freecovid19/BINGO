'''
installer.py v0.2
참여하셨다면 이름을 입력해주세요
1. 진성민
2. forgot09

지원 OS
Windows, Linux. Android(선택)
'''

import subprocess
try:
	import requests, os, platform, time, zipfile, shutil
except:
	pip('requests')

def download(url, file_name = None):
	if not file_name:
		file_name = url.split('/')[-1]
	with open(file_name, "wb") as file:   
		response = requests.get(url)               
		file.write(response.content) 

def extrec(zfile, path):
	file = zipfile.ZipFile(zfile)
	file.extractall(path)
	file.close()

def pip(module):
	cmd = 'pip install ' + module
  print(module, '을(를) 설치합니다.')
	subprocess.run([cmd], shell=True)

print('===[BINGO 설치 프로그램]===')
print('사용자의 컴퓨터에 자동으로 BINGO를 설치합니다.')
print('주의! 설치되어있던 BINGO는 자동삭제됩니다!')
print('관리자권한(Root)으로 실행하세요.\n')

useros = platform.system()

if useros == 'Linux':
	while True:
		print('Android에 설치하실건가요? (y/n)')
		ans = str(input('Installer>'))
		if ans == 'y':
			useros = 'Android'
			path = '/storage/emulated/0/OS_Android'
			break
		elif ans == 'n':
			useros = 'Linux'
			break
      
if useros == 'Windows':
	path = 'C:\\'
elif useros == 'Linux':
	print('사용자이름을 입력하세요.')
	user = str(input('Installer>'))
	path = '/home' + '/' + user
elif useros == 'Darwin':
	print('죄송합니다, macOS는 지원하지 않습니다.')
	time.sleep(5)
	quit()
elif useros == 'Android':
	pass

if useros == 'Windows':
	print('초기화중...')
	try:
		shutil.rmtree('C:\\BINGO-Windows')
	except:
		pass
	try:
		shutil.rmtree('C:\\OS_Windows')
	except:
		pass
	print('다운로드중...')
	download('https://github.com/kty0205/BINGO/archive/Windows.zip', path+'\\Windows.zip')
	file = path + '\\Windows.zip'
	print('압축해제중...')
	extrec(file, path)
	os.rename('C:\\BINGO-Windows', 'C:\\OS_Windows')
	os.remove('C:\\Windows.zip')
  print('필요한 모듈 설치중...')
elif useros == 'Linux':
	try:
		shutil.rmtree(path+'/BINGO-Linux')
	except:
		pass
	try:
		shutil.rmtree(path+'/OS_Linux')
	except:
		pass
	print('다운로드중...')
	download('https://github.com/kty0205/BINGO/archive/Linux.zip', path+'/Linux.zip')
	file = path + '/Linux.zip'
	print('압축해제중...')
	extrec(file, path)
	os.rename(path+'/BINGO-Linux', path+'/OS_Linux')
	with open(path+'/OS_Linux/sys/direc.txt', 'w') as direc:
		direc.write(path+'/OS_Linux')
	os.remove(path+'/Linux.zip')
elif useros == 'Android':
	print('초기화중...')
	try:
		shutil.rmtree('/storage/emulated/0/OS_Android')
	except:
		pass
	try:
		shutil.rmtree('/storage/emulated/0/BINGO-Android')
	except:
		pass
	print('다운로드중...')
	download('https://github.com/kty0205/BINGO/archive/Android.zip', path+'/Android.zip')
	file = path + '/Android.zip'
	print('압축해제중...')
	extrec(file, path)
	os.rename('/storage/emulated/0/BINGO-Android', '/storage/emulated/0/OS_Android')
	os.remove('/storage/emulated/0/Android.zip')

print('다운로드가 완료되었습니다. Main.py를 실행해주세요.')
print('설치된 디렉터리 :', path)
time.sleep(3)