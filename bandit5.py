#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pwn import ssh

username = 'bandit4'
host = 'bandit.labs.overthewire.org'
password = 'pIwrPrtPN36QITSp3EQaw936yaFoFgAB'

shell = ssh(username, host, password=password)
sh = shell.run('bash')
sh.sendline("""find inhere -type f -exec file '{}' \; 2>/dev/null|"""
            """grep  ASCII | awk 'BEGIN{FS=":"}{print "cat "$1}'|sh""")
print sh.recvline(timeout=5)
