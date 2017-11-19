#! /usr/bin/env python3
# Project: Adding Bullets to Wiki Markup
# bulletPointadder.py - Adds Wikipedia bullet points to the start
# of each line of text on the clipboard.

import pyperclip
text = pyperclip.paste()

# Separate lines and add stars.
lines = text.split('\n')
# for i in range(len(lines)):     # loop through all indexes in the "lines" list
#     lines[i] = '* ' + lines[i]  # add star to each string in "lines" list

# A more pythonic way to approach the for loop.
for item in lines:
    item = '* ' + item

text = '\n'.join(lines)
pyperclip.copy(text)
