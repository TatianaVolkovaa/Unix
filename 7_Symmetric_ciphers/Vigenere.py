def incript(s, key):
    n1 = [i for i in s]
    n2 = [key[i % len(key)] for i in range(len(n1))]
    n3 = [chr((ord(n1[i]) + ord(n2[i]))) for i in range(len(n1))]
    return ''.join(n3)


def decript(s, key):
    n1 = [i for i in s]
    n2 = [key[i % len(key)] for i in range(len(n1))]
    n3 = [chr((ord(n1[i]) - ord(n2[i]))) for i in range(len(n1))]
    return ''.join(n3)


source = 'The dream will not come true without difficulty'
key = 'password'
inc_source = incript(source, key)
dec_source = decript(inc_source, key)
print(inc_source)
print(dec_source)
