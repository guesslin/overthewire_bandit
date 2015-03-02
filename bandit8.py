#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pwn import ssh

username = 'bandit7'
host = 'bandit.labs.overthewire.org'
password = 'HKBPTKQnIay4Fw76bEy8PVxKEDQRKTzs'

shell = ssh(username, host, password=password)
sh = shell.run('bash')
sh.sendline("grep millionth data.txt | awk '{print $2}'")
print sh.recvline(timeout=5)
