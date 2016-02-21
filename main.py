#! /usr/bin/python
# -*- coding: utf-8 -*-

import random

# Random utilities
def uniform(a, b):
    return random.uniform(a, b)

def randint(a, b):
    return random.randint(a, b)

def bit():
    return random.randint(0, 1)

def bool():
    if bit() == 0: return True
    else: return False

def sign():
    if bool(): return -1
    else: return 1

def probability( prob ):
    if prob == 0: return False
    if uniform(0, 100) <= prob: return True
    else: return False
