#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pwn import ssh

username = 'bandit10'
host = 'bandit.labs.overthewire.org'
password = 'truKLdjsbJ5g7yyJ2X2R0o3a5HQJFuLk'

shell = ssh(username, host, password=password)
sh = shell.run('bash')
sh.sendline("base64 -d data.txt")
print sh.recvline(timeout=5)
