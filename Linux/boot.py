#boot.py for Linux

import time, random

def clear():
	for i in range(1, 71):
		print('\n')

def main():
	print('운영체제 시작하는중...')
	time.sleep(random.randrange(3, 8))
	clear()