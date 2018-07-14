# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 06:49:57 2017

@author: Sandbox999
"""
#this is Sandbox's Python Code
# regular expressions

import re
m = re.search('ab..e', 'abcdef')
print(m.group(0))

re.match("c", "abcdef")  # No match
re.search("c", "abcdef") # Match
