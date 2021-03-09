#bios.py by Android

import subprocess as sp

def boot(boot):
	try:
		file = boot.split(' ')
		btcmd = 'python3' + ' ' + file[1]
		sp.run([btcmd], shell=True)
	except:
		print('boot failed')

def title():
	print('===CLI BIOS===')

def main():
	title()
	while True:
		ans = str(input('Bios>'))
		if 'boot' in ans:
			boot(ans)
			quit()
		else:
			print('Invalid command!')

main()