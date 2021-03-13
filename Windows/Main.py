#Main.py for Windows

try:
	import time, os
	from pgm import command as com
	import subprocess as sp
except:
	print('오류가 발생했습니다. errorlog.txt를 봐주세요.')
	with open('errorlog.txt', 'w') as errorlog:
		errorlog.write('오류가 발생했습니다.\n')
		errorlog.write('에러코드 : 001C\n')
		errorlog.write('에러코드 읽는 방법을 참조해 주세요.\n')

#메인
while True:
	import boot
	boot.main()
	from pgm import wordpad as wpad
	from pgm import calc
	from pgm import checkhw as chw
	
	chw.writefile()

	while True:
		locate = os.getcwd()
		ans = input('\n' + locate + '>')
		
		#명령어
		if ans == 'clear':
			com.clear()
		elif ans == 'help':
			com.help()
		elif ans == 'info':
			com.info()
		elif ans == 'hwinfo':
			com.hwinfo()
		elif 'cd' in ans:
			com.cd(ans)
		elif 'rmdir' in ans:
			com.rmdir(ans)
		elif 'mkdir' in ans:
			com.mkdir(ans)
		elif ans == 'shutdown':
			com.shutdown()
		elif 'rename' in ans:
			com.rename(ans)
		elif 'rmfile' in ans:
			com.rmfile(ans)
		elif ans == 'JSM_easter':
			com.easter()
		elif ans == 'filelist':
			com.filelist()
		elif ans == 'delcache':
			com.delcache()
		elif 'jpio' in ans:
			com.jpio(ans)
		
		#문서편집기 실행
		elif 'wpad ' in ans:
			if 'new' in ans:
				wpad.new()
			else:
				wpad.file_load(ans)
		elif ans == 'wpad':
			wpad.main()
		
		#계산기 실행
		elif 'calc ' in ans:
			calc.comcalc(ans)
		elif ans == 'calc':
			calc.main()
		
		#프로그램 실행
		elif ans in os.listdir():
			try:
				cmd = 'python3'+ ' ' + ans
				sp.run([cmd], shell=True)
			except:
				print('오류가 일어났습니다.')

		else:
			print(ans, '은(는) 명령어 또는 프로그램이 아닙니다.')
