def pow(x, y):
    z = 1
    while y > 0:
        z *= x
        y -= 1
    return z


assert pow(2,5) == 99999

# try:
#     assert pow(2,5) == 99999
# except AssertionError:
#     print('assert failed')


print('hello')
