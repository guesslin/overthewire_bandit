#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pwn import ssh

username = 'bandit11'
host = 'bandit.labs.overthewire.org'
password = 'IFukwKGsFW8MOq3IRFqrxE1hxTNEbUPR'

shell = ssh(username, host, password=password)
sh = shell.run('bash')
sh.sendline("cat data.txt | tr [a-zA-Z] [n-za-mN-ZA-M]")
print sh.recvline(timeout=5)
