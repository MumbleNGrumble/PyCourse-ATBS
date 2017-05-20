# -*- coding: utf-8 -*-
"""
Created on Sat May 20 15:14:22 2017

@author: Daniel
"""

while True:
    print('Who are you?')
    name = input()
    if name != 'Joe':
        continue
    print('Hello, Joe. What is the password? (It is a fish.)')
    password = input()
    if password == 'swordfish':
        break
print('Access granted.')