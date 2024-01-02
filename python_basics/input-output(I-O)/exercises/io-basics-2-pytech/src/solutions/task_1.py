"""Convert a file to binary"""

with open('../data/task1.txt') as source:
    content = source.read()
    with open('../data/task1.bin', mode='wb') as target:
        target.write(content.encode('utf-8'))
