# -*- coding: utf-8 -*-
"""
Created on Sat May 20 15:28:31 2017

@author: Daniel
"""

import sys

while True:
    print('Type exit to exit.')
    response = input()
    if response == 'exit':
        sys.exit()
    print('You typed ' + response + '.')