# Charles Weng
# SoftDev2   pd7
# K #15: Do You Even List?
# 2018-4-25

################################################################################
#                                   Defined Sets                               #
################################################################################

A = [1, 2, 3, 4, 5, 6, 7, 8, 9]
B = [0]
C = []
D = [2, 4, 6, 8, 10]


################################################################################
#                                   Functions                                  #
################################################################################

def union(a, b):
    temp = list(a)
    [temp.append(x) for x in b if x not in a]
    return temp


def intersection(a, b):
    return [x for x in b if x in a]


def setDif(a, b):
    return [x for x in a if x not in b]


def sysDif(a, b):
    temp = [x for x in a if x not in b]
    [temp.append(x) for x in b if x not in a]
    return temp


def cartProd(a, b):
    return [(x, y) for x in a for y in b]


def test(a, b):
    print a
    print b
    print union(a, b)
    print intersection(a, b)
    print setDif(a, b)
    print sysDif(a, b)
    print cartProd(a, b)
    print "\n\n"


################################################################################
#                                   Testing                                    #
################################################################################

test(A, B)
test(A, D)
test(B, C)
