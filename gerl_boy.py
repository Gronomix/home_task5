import itertools
import numpy as np
import random

old_gerl = 0
both_gerl = 0
either_girl = 0
boy = 0
kids = ['boy', 'girl']

for i in range(10000):
    younger = random.choice(kids)
    older = random.choice(kids)

    if older == 'girl':
        old_gerl += 1
    if older == 'girl' and younger == 'girl':
        both_gerl += 1
    if older == 'girl' or younger == ' girl':
        either_girl += 1
    if older == 'boy':
        boy += 1


print(old_gerl)
print(both_gerl)
print(either_girl)
print(boy)

