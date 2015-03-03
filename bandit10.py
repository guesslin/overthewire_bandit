#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pwn import ssh

username = 'bandit9'
host = 'bandit.labs.overthewire.org'
password = 'UsvVyFSfZZWbi6wgC7dAFyFuR6jQQUhR'

shell = ssh(username, host, password=password)
sh = shell.run('bash')
sh.sendline("strings data.txt |grep ^= | awk '{print $2}'")
print sh.recvlines(10, timeout=5)
