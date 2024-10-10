# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 19:58:27 2024

@author: josey
"""

#!/usr/bin/env python3

def to_c(f):
    c = (f - 32) * 5 / 9
    return c

def to_f(c):
    f = (c * 9 / 5) + 32
    return f
    