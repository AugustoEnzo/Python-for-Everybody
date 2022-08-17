from random import randint

fp = open('GEO_DATA/where.data')
l_data = list()

count = int()

for line in fp:
    d_line = line.strip()
    l_data.append(d_line)
    count += 1

r_ind = randint(1, count)

print(l_data[r_ind])
