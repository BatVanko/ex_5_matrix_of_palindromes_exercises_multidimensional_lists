def get_alphabetic_nums():
    alphabetic_nums = {}
    asci_index = 97
    for i in range( 26):
        alphabetic_nums[i] = chr(asci_index)
        asci_index += 1
    return alphabetic_nums


rows, cols =[int(x) for x in input().split()]
matrix = []

for i in range(rows):
    matrix.append([])
    for j in range(cols):
        first = get_alphabetic_nums()[i]
        middle = get_alphabetic_nums()[i + j]
        last = get_alphabetic_nums()[i]
        word = first + middle + last
        matrix[i].append(word)
for row in matrix:
    print(' '.join(row))

