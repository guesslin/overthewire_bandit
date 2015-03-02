#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pwn import ssh

username = 'bandit6'
host = 'bandit.labs.overthewire.org'
password = 'DXjZPULLxYr17uwoI01bNLQbtFemEgo7'

shell = ssh(username, host, password=password)
sh = shell.run('bash')
sh.sendline("find / -type f -user bandit7 -group bandit6 "
            "-size 33c -exec cat '{}' \; 2>/dev/null")
print sh.recvline(timeout=5)
