'''
installer.py v0.1
참여하셨다면 이름을 입력해주세요
1. 진성민
2. forgot09

지원 OS
Windows, Linux. Android(선택)
'''

import requests, os, platform, time, zipfile

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

print('===[설치 프로그램]===')
print('사용자의 컴퓨터에 자동으로 BINGO를 설치합니다.')
print('관리자권한(Root)으로 실행하세요.\n')

os = platform.system()

if os == 'Linux':
	while True:
		print('Android에 설치하실건가요? (y/n)')
		ans = str(input('Installer>'))
		if ans == 'y':
			os = 'Android'
			path = '/storage/emulated/0/OS_Android'
			break
		elif ans == 'n':
			os = 'Linux'
			break
      
if os == 'Windows':
	ospath = 'C:\\OS_Windows'
  downloadpath = 'C:\\'
elif os == 'Linux':
	print('사용자이름을 입력하세요.')
	user = str(input('Installer>'))
	ospath = '/home/' + user + '/OS_Linux'
  downloadpath = '/home' + user
elif os == 'Darwin' or 'darwin':
	print('죄송합니다, macOS는 지원하지 않습니다.')
	time.sleep(5)
	quit()

if os == 'Windows':
	print('다운로드중...')
	download('https://github.com/kty0205/BINGO/archive/Windows.zip', path+'\\Windows.zip')
	file = path + '\\Windows.zip'
	print('압축해제중...')
	extrec(file, path)
elif os == 'Linux':
	print('다운로드중...')
	download('https://github.com/kty0205/BINGO/archive/Linux.zip', path+'/Linux.zip')
	file = path + '/Linux.zip'
	print('압축해제중...')
	extrec(file, path)
elif os == 'Android':
	print('다운로드중...')
	download('https://github.com/kty0205/BINGO/archive/Android.zip', path+'/Android.zip')
	file = path + '/Android.zip'
	print('압축해제중...')
	extrec(file, path)

print('다운로드가 완료되었습니다. Main.py를 실행해주세요.')
print('설치된 디렉터리 :', path)
time.sleep(5)
