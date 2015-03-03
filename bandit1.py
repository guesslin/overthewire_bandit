#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pwn import ssh

shell = ssh('bandit0', 'bandit.labs.overthewire.org', password='bandit0')
print 'Way 1'
cat = shell.run('cat readme')
print cat.recvall()
cat.close()
print 'Way 2'
sh = shell.run('sh')
sh.sendline('cat readme')
print sh.recvline()
sh.close()
