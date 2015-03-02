#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pwn import *

username = 'bandit2'
host = 'bandit.labs.overthewire.org'
password = args['PASSWORD']  # CV1DtqXWVFXTvM2F0k09SHz0YwRINYA9

shell = ssh(username, host, password=password)
sh = shell.run('sh')
sh.sendline("""find -type f ! -iname ".*" -exec cat '{}' \;""")
print sh.recvline(timeout=5)
