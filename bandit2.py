#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pwn import ssh

username = 'bandit1'
host = 'bandit.labs.overthewire.org'
password = 'boJ9jbbUNNfktd78OOpsqOltutMc3MY1'

shell = ssh(username, host, password=password)
sh = shell.run('sh')
sh.sendline('cat ./-')
print sh.recvline(timeout=5)
