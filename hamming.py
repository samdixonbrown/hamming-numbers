def hamming(n):
    bases = [2, 3, 5]
    exps = [0, 0, 0]
    hamms = [1]
    for _ in range(1, n):
        next_hamms = [bases[i] * hamms[exps[i]] for i in range(3)]
        next_hamm = min(next_hamms)
        hamms.append(next_hamm)
        for i in range(3):
            exps[i] += int(next_hamms[i] == next_hamm)
    return hamms[-1]
