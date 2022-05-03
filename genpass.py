# -*- coding:utf -8 -*-
# !/usr/bin/python3

import random

chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
password = ''
for i in range(10):
    password += random.choice(chars)
print(password)
