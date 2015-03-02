#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pwn import ssh

username = 'bandit8'
host = 'bandit.labs.overthewire.org'
password = 'cvX2JJa4CFALtqS87jk27qwqGhBM9plV'

shell = ssh(username, host, password=password)
sh = shell.run('bash')
sh.sendline("cat data.txt | sort | uniq -c | sort -nr|tail -n1|"
            "awk '{print $2}'")
print sh.recvline(timeout=5)
