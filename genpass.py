# -*- coding:utf -8 -*-
# !/usr/bin/python3

import random

from open_file_json import open_file_json
from save_file_json import save_file_json

passfile = open_file_json('', 'password')
chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
password = ''
for i in range(15):
    password += random.choice(chars)
print(password)

passfile['passwords'].append(password)
save_file_json('', 'password', passfile)
