#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pwn import *

username = 'bandit4'
host = 'bandit.labs.overthewire.org'
password = args['PASSWORD']  # pIwrPrtPN36QITSp3EQaw936yaFoFgAB

shell = ssh(username, host, password=password)
sh = shell.run('bash')
sh.sendline('cd inhere')
sh.sendline("""find -type f -exec file '{}' \; 2>/dev/null| grep  ASCII | awk 'BEGIN{FS=":"}{print "cat "$1}'|sh""")
print sh.recvline(timeout=5)
