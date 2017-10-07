#! /usr/bin/env python3
# strongPassword.py - Detects if password entered is 'strong' or not.

import re

lowRegex = re.compile(r'[a-z]+')
upRegex = re.compile(r'[A-Z]+')
numRegex = re.compile(r'[0-9]+')

print("Enter a password: ")
password = input()
if len(password) < 8 or not lowRegex.search(password) or not upRegex.search(password) or not numRegex.search(password):
    print("Password is weak AF")
else:
    print("Password is lit fam")
