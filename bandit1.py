#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pwn import *

shell = ssh('bandit0', 'bandit.labs.overthewire.org', password='bandit0')
sh = shell.run('sh')
sh.sendline('cat readme')
print sh.recvline()
