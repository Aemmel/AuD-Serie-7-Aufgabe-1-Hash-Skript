m = 11

def ha1(k):
    return k % m

# lin. sondieren
def ha(k, i):
    return (ha1(k) + i) % m

def hb1(k):
    return ha1(k)

def hb2(k):
    return 1 + (k % (m-1))

# double hash
def hb(k, i):
    return (hb1(k) + i*hb2(k)) % m

unhashed = [10, 22, 31, 4, 15, 28, 17, 88, 59]

table = [None for i in range(m)]

open_hash = hb

for num in unhashed:
    i = 0
    while True:
        h = open_hash(num, i)
        if table[h] == None:
            table[h] = num
            break
        i += 1

for i in range(len(table)):
    print(str(i) + ": " + str(table[i]))
