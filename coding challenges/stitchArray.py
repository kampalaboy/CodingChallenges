def sticth(*args):
    w = []
    for i in args:
        w += i
    return w 

n = [8,9,9,8,7,6]
o = [9,0,8,6,8,6]
print(sticth(n,o))
