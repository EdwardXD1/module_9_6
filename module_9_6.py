from itertools import combinations
def all_variants(text):
    list_ = []
    for i in range(1, len(text)+1):
        list_ = []
        b = combinations(text, i)
        list_.extend(b)
        for j in list_:
            j = list(j)
            yield (''.join(j))

a = all_variants("abc")
for i in a:
    if i == 'ac':
        continue
    print(i)