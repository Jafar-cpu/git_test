a = [1,2,3,4,5,6,7,8,9]


def al(A):
    for v in A:
        for x in A:
            if v < x:
                break
        else:
            return v
    return None
print(al(a))