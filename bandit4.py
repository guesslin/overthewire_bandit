#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pwn import ssh

username = 'bandit3'
host = 'bandit.labs.overthewire.org'
password = 'UmHadQclWmgdLOKQ3YNgjWxGoRMb5luK'

shell = ssh(username, host, password=password)
sh = shell.run('sh')

sh.sendline('cat ./inhere/.hidden')
print sh.recvline(timeout=5)
