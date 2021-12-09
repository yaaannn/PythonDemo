def index_iter(str):
    yield 0
    count = 0
    for i in str:
        count += 1
        if i == ' ':
            yield count


indices = index_iter('Life is short, you need Python')
for i in indices:
    print(i, end=' ')
