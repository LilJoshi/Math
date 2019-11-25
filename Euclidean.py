# Euclidean Algorithm

def gcd(a, b):
    if a < b:
        return gcd(b, a)
    if b < 0:
        return gcd(a, -b)
    if b == 0:
        return a
    return gcd(a-b, b)

# Now we will do the extended Euclidean algorithm
# The idea is to consider the "augmented" identity matrix
# 1 0 | a
# 0 1 | b
# and to perform row operations, till we get
# ? ? | gcd(a, b)
# ? ? | 0
# In other words, we consider the matrix equation Ix = x, where x = [a, b]
# and multiple the left by row-operation matrices to make the right side
# the vector [gcd(a, b) 0]

# In the function below, think
# a_1 a_2 | a
# b_1 b_2 | b
#

def extended(a, b, a_1, a_2, b_1, b_2):
    if a < b:
        return extended(b, a, b_1, b_2, a_1, a_2)
    if b < 0:
        return extended(a, -b, a_1, a_2, b_1, b_2)
    if b == 0:
        return (a, a_1, a_2)
    return extended(a-b, b, a_1-b_1, a_2-b_2, b_1, b_2)

def extended_gcd(a, b):
    arr = extended(a, b, 1, 0, 0, 1)
    # print("{:d} * {:d} + {:d} * {:d} = {:d}".format(a, arr[1], b, arr[2], arr[0]))
    return arr
