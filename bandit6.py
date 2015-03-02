#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pwn import ssh

username = 'bandit5'
host = 'bandit.labs.overthewire.org'
password = 'koReBOKuIDDepwhWk7jZC0RTdopnAYKh'

shell = ssh(username, host, password=password)
sh = shell.run('bash')
sh.sendline("""find inhere -type f -readable -size 1033c """
            """! -executable -exec cat '{}' \;""")
print sh.recvline(timeout=5)
