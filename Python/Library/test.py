import itertools 


# for i in itertools.count(10):
#     print(i)

# for i in itertools.cycle('ABCD'):
    # print(i)

# for i in itertools.repeat(10):
#     print(i)

# for i in itertools.chain('ABC', 'DEF'):
#     print(i)


# for i in itertools.chain('ABC','DEF'):
#     print(i)

# for i in itertools.islice('ABCDEFG', 2, 4):

#     print(i)
# a = 'ABCDEFG'
# print(a[2:4])

for i in itertools.product('ABCD', repeat = 2):
    print(*i)
for i in itertools.permutations('ABCD', 2):
    print(i)