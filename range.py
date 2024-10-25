def ranger(*args):

    if len(args) == 1:
        r =list(range(args[0]+1))
    elif len(args) == 2 :
        r = list(range(args[0], args[1]+1))
    return r

print(ranger(4, 10))