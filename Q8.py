def pipeline(*funcs):
    def helper(arg):
        sum = arg
        for func in funcs:
            sum = func(sum)
        return sum
    return helper


fun = pipeline(lambda x: x * 3, lambda x: x + 1, lambda x: x / 2)
print(fun(3))  # should print 5.0