import itertools

color = ['grin', 'yelow', 'blak', 'red']

for i in itertools.combinations(color, 3):
    print(' '.join(i))

for i in itertools.permutations(color, 3):
    print(' '.join(i))