#checkhw.py for Linux

import psutil, py_cpuinfo, platform, getmac, shutil
import socket

cpu_name = 0
cpu_cores = 0
cpu_physic_cores = 0
cpu_normal_clock = 0
arch_type = 0
def cpu():
	global cpu_name, cpu_cores, cpu_physic_cores
	global cpu_normal_clock, arch_type
	cpu = cpuinfo.get_cpu_info()
	try:
		cpu_name = cpu['brand']
	except:
		cpu_name = '알 수 없는 CPU'
	
	try:
		cpu_cores = psutil.cpu_count()
	except:
		cpu_cores = '알 수 없음'
	
	try:
		cpu_physic_cores = psutil.cpu_count(logical=False)
	except:
		cpu_physic_cores = '알 수 없음'
	
	try:
		cpu_normal_clock = cpu['hz_actual']
	except:
		cpu_normal_clock = '알 수 없음'
	
	try:
		arch_type = platform.machine()
	except:
		arch_type = '알 수 없음'
	return cpu_name, cpu_cores, cpu_physic_cores
	return cpu_normal_clock, arch_type

total_ram = 0
def ram():
	global total_ram
	total_ram = str(round(psutil.virtual_memory().total / 1024))
	return total_ram

disk_size = 0
disk_used = 0
disk_free = 0
def disk():
	global disk_size, disk_used, disk_free
	disk_size, disk_used, disk_free = shutil.disk_usage('/')
	return disk_size, disk_used, disk_free

internal_ip = 0
external_ip = 0
mac_add = 0
def network():
	global internal_ip, external_ip, mac_add
	internal_ip = socket.gethostbyname(socket.gethostname())
	external_ip = socket.gethostbyname(socket.getfqdn())
	mac_add = getmac.get_mac_address()
	return internal_ip, external_ip, mac_add

def writefile():
	global cpu_name, cpu_cores, cpu_physic_cores
	global cpu_normal_clock, arch_type
	global ip, internal_ip, external_ip, mac_add
	global total_ram, disk_size, disk_used, disk_free
	
	hwlist = [cpu_name, cpu_cores, cpu_physic_cores, cpu_normal_clock, arch_type,  internal_ip, external_ip, mac_add,  total_ram, disk_size, disk_used, disk_free]
	
	cpu()
	ram()
	disk()
	network()
	with open('/storage/emulated/0/OS_Android/sys/hwconfig.txt', 'w') as hw:
		s = 0
		for i in hwlist:
			hw.write(str(hwlist[s]))
			hw.write('\n')
			s += 1