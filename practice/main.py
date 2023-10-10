def find_it(seq):
    m = seq[0]
    for i in list(set(seq)):
        print(f'i={i}, m={m}')
        if (seq.count(i) % 2 != 0 and seq.count(m) % 2 == 0) or (seq.count(i) % 2 != 0 and seq.count(i) > seq.count(m)):
            m = i
    return m

if __name__ == '__main__':
    print(find_it([int(i) for i in input().split(',')]))