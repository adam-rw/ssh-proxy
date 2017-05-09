#!/usr/bin/env python3

import os
import sys
import getpass
import pexpect
import time
import signal
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

user = config.get('SSH Host', 'User')
host = config.get('SSH Host', 'Host')

ssh_command = 'ssh -C2qTnN -D 8080 -f %s@%s' % (user, host)

def printer(message):
	print('%s' % message)

def run_command(arg):
	if '--start' == arg:
		start()
	elif '--stop' == arg:
		stop()
	elif '--restart' == arg:
		restart()
	elif '--status' == arg:
		status()
	else:
		print('USAGE: %s [--start,--stop,--restart, --status]' % sys.argv[0])

def get_pids():
	ps = pexpect.run('ps -ax')
	pids = []

	for line in ps.splitlines():
		if str(line).find(ssh_command) > 0:
			line_split = str(line).split(' ')
			pids.append(line_split[0][2:])

	if len(pids) > 0:
		return pids
	
	return False

def start():
	if not (get_pids()):
		printer('SSH Proxy starting...')
		password = getpass.getpass(prompt='SSH password for %s: ' % user)
		
		try:
			ssh_tunnel = pexpect.spawn (ssh_command % globals())
			ssh_tunnel.expect ('password:')
			time.sleep (0.1)
			ssh_tunnel.sendline (password)
			time.sleep (0.1)
			ssh_tunnel.expect (pexpect.EOF)

		except Exception as e:
			print('Error: Unable to create tunnel. Try running the command manually for details:')
			printer(ssh_command)
	else:
		printer('SSH Proxy is already running')

def stop():
	printer('SSH Proxy stopping...')
	pids = get_pids()
	if pids:
		for pid in pids:
			os.kill(int(pid), signal.SIGTERM)

	if get_pids():
		printer('Error: Unable to stop SSH Proxy. Please try again')

def restart():
	stop()
	start()
	pass

def status():
	if get_pids():
		printer('SSH Proxy is currently connected, via %s' % host)
	else:
		printer('SSH Proxy is not connected')
	pass


try:
	if len(sys.argv) == 2:
		command = run_command(sys.argv[1])
	else:
		command = run_command('--help')
except KeyboardInterrupt:
	print('')
	exit(1)